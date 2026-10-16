import logging
from functools import reduce

import talib.abstract as ta
from pandas import DataFrame

from freqtrade.strategy import DecimalParameter, IStrategy, informative


logger = logging.getLogger(__name__)


class FreqaiLgbmRegime(IStrategy):
    """
    FreqAI spot long-only strategy used with `--freqaimodel LightGBMRegressor`
    and `user_data/config_freqai.json`.

    Predicts a forward return (`&-fwd_ret`) and enters long when the prediction
    exceeds a hyperoptable threshold and BTC trades above its daily EMA200.
    """

    INTERFACE_VERSION = 3

    timeframe = "1h"
    can_short = False

    process_only_new_candles = True
    startup_candle_count = 4900

    stoploss = -0.05
    trailing_stop = False
    minimal_roi = {"0": 0.10, "720": 0.04, "1440": 0.01}

    entry_thr = DecimalParameter(0.002, 0.03, decimals=3, default=0.01, space="buy")
    exit_thr = DecimalParameter(-0.02, 0.0, decimals=3, default=-0.003, space="sell")

    def feature_engineering_expand_all(
        self, dataframe: DataFrame, period: int, metadata: dict, **kwargs
    ) -> DataFrame:
        dataframe["%-rsi-period"] = ta.RSI(dataframe, timeperiod=period)
        dataframe["%-adx-period"] = ta.ADX(dataframe, timeperiod=period)
        dataframe["%-atr_pct-period"] = ta.ATR(dataframe, timeperiod=period) / dataframe["close"]
        dataframe["%-roc-period"] = ta.ROC(dataframe, timeperiod=period)
        return dataframe

    def feature_engineering_expand_basic(
        self, dataframe: DataFrame, metadata: dict, **kwargs
    ) -> DataFrame:
        dataframe["%-pct-change"] = dataframe["close"].pct_change()
        dataframe["%-ret_4"] = dataframe["close"].pct_change(4)
        dataframe["%-volume_z"] = dataframe["volume"] / dataframe["volume"].rolling(48).mean()
        return dataframe

    def feature_engineering_standard(
        self, dataframe: DataFrame, metadata: dict, **kwargs
    ) -> DataFrame:
        dataframe["%-hour_of_day"] = dataframe["date"].dt.hour
        dataframe["%-day_of_week"] = dataframe["date"].dt.dayofweek
        return dataframe

    def set_freqai_targets(self, dataframe: DataFrame, metadata: dict, **kwargs) -> DataFrame:
        label_period_candles = self.freqai_info["feature_parameters"]["label_period_candles"]
        dataframe["&-fwd_ret"] = (
            dataframe["close"].shift(-label_period_candles) / dataframe["close"] - 1
        )
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe = self.freqai.start(dataframe, metadata, self)
        return dataframe

    @informative("1d", "BTC/USDT")
    def populate_indicators_btc_1d(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        enter_long_conditions = [
            dataframe["do_predict"] == 1,
            dataframe["&-fwd_ret"] > self.entry_thr.value,
            dataframe["btc_usdt_close_1d"] > dataframe["btc_usdt_ema200_1d"],
            dataframe["volume"] > 0,
        ]
        if enter_long_conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, enter_long_conditions), ["enter_long", "enter_tag"]
            ] = (1, "fwd_ret_long")
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        exit_long_conditions = [
            dataframe["do_predict"] == 1,
            dataframe["&-fwd_ret"] < self.exit_thr.value,
        ]
        if exit_long_conditions:
            dataframe.loc[reduce(lambda x, y: x & y, exit_long_conditions), "exit_long"] = 1
        return dataframe
