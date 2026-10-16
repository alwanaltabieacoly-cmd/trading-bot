import sys
import os

sys.path.append(os.path.dirname(__file__))

import talib.abstract as ta
from pandas import DataFrame

from freqtrade.strategy import BooleanParameter, IntParameter, informative

from TrendAdx1h import TrendAdx1h


class TrendAdx1hRegime(TrendAdx1h):
    startup_candle_count = 4900

    btc_adx_bear = IntParameter(20, 40, default=30, space="buy")
    use_btc_adx = BooleanParameter(default=True, space="buy")

    @informative("1d", "BTC/USDT")
    def populate_indicators_btc_1d(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        return dataframe

    @informative("4h", "BTC/USDT")
    def populate_indicators_btc_4h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["adx"] = ta.ADX(dataframe, timeperiod=14)
        dataframe["plus_di"] = ta.PLUS_DI(dataframe, timeperiod=14)
        dataframe["minus_di"] = ta.MINUS_DI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe = super().populate_entry_trend(dataframe, metadata)

        regime_ok = dataframe["btc_usdt_close_1d"] > dataframe["btc_usdt_ema200_1d"]
        if self.use_btc_adx.value:
            bearish_adx = (
                (dataframe["btc_usdt_adx_4h"] > self.btc_adx_bear.value)
                & (dataframe["btc_usdt_minus_di_4h"] > dataframe["btc_usdt_plus_di_4h"])
            )
            regime_ok = regime_ok & ~bearish_adx

        regime_ok = regime_ok.fillna(False)
        dataframe.loc[~regime_ok, "enter_long"] = 0
        return dataframe
