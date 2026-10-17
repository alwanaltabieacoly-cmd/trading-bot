import logging
from functools import reduce
from pathlib import Path

import numpy as np
import pandas as pd
import talib.abstract as ta
from pandas import DataFrame

from freqtrade.strategy import DecimalParameter, IStrategy, informative


logger = logging.getLogger(__name__)


class FreqaiClfRegime(IStrategy):
    """
    FreqAI spot long-only classifier strategy used with
    `--freqaimodel LightGBMClassifier` and `user_data/config_freqai_clf.json`.

    Predicts whether the +2% target (`close * 1.02`) is hit before the -5% stop
    (`close * 0.95`) within the label period and enters long when the predicted
    probability exceeds a hyperoptable threshold and BTC trades above its daily
    EMA200.
    """

    INTERFACE_VERSION = 3

    timeframe = "1h"
    can_short = False

    process_only_new_candles = True
    startup_candle_count = 4900

    stoploss = -0.05
    trailing_stop = False
    minimal_roi = {"0": 0.02}

    entry_prob = DecimalParameter(0.50, 0.85, decimals=2, default=0.60, space="buy")

    _fng = None

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

        if self._fng is None:
            path = Path(self.config["user_data_dir"]) / "external" / "fng.csv"
            fng = pd.read_csv(path)
            fng["avail"] = pd.to_datetime(fng["date"], utc=True) + pd.Timedelta(days=1)
            fng["chg7"] = fng["fng"].diff(7)
            self._fng = fng[["avail", "fng", "chg7"]].sort_values("avail")

        merged = dataframe.copy()
        merged["_orig_order"] = range(len(merged))
        merged = merged.sort_values("date")
        merged = pd.merge_asof(
            merged,
            self._fng.assign(avail=self._fng["avail"].astype(merged["date"].dtype)),
            left_on="date",
            right_on="avail",
            direction="backward",
        )
        merged = merged.sort_values("_orig_order")

        dataframe["%-fng"] = merged["fng"].fillna(50).to_numpy()
        dataframe["%-fng_chg7"] = merged["chg7"].fillna(0).to_numpy()
        return dataframe

    def set_freqai_targets(self, dataframe: DataFrame, metadata: dict, **kwargs) -> DataFrame:
        self.freqai.class_names = ["down", "up"]
        n = self.freqai_info["feature_parameters"]["label_period_candles"]

        close = dataframe["close"].to_numpy()
        up_price = close * 1.02
        dn_price = close * 0.95
        first_up = np.full(len(dataframe), n + 1, dtype=int)
        first_dn = np.full(len(dataframe), n + 1, dtype=int)

        for k in range(1, n + 1):
            hi = dataframe["high"].shift(-k).to_numpy()
            lo = dataframe["low"].shift(-k).to_numpy()
            dn_hit = (lo <= dn_price) & (first_dn == n + 1)
            first_dn[dn_hit] = k
            up_hit = (hi >= up_price) & (first_up == n + 1)
            first_up[up_hit] = k

        dataframe["&-hit"] = np.where(first_up < first_dn, "up", "down")
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
            dataframe["up"] > self.entry_prob.value,
            dataframe["btc_usdt_close_1d"] > dataframe["btc_usdt_ema200_1d"],
            dataframe["volume"] > 0,
        ]
        if enter_long_conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, enter_long_conditions), ["enter_long", "enter_tag"]
            ] = (1, "clf_hit_long")
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        exit_long_conditions = [
            dataframe["do_predict"] == 1,
            dataframe["up"] < 0.35,
        ]
        if exit_long_conditions:
            dataframe.loc[reduce(lambda x, y: x & y, exit_long_conditions), "exit_long"] = 1
        return dataframe
