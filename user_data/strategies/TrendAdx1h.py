from datetime import datetime

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from pandas import DataFrame

from freqtrade.strategy import (
    IStrategy,
    IntParameter,
    DecimalParameter,
    informative,
    stoploss_from_absolute,
)


class TrendAdx1h(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "1h"
    can_short = False
    startup_candle_count = 250
    process_only_new_candles = True

    stoploss = -0.08
    use_custom_stoploss = True
    trailing_stop = False
    minimal_roi = {"0": 0.15, "720": 0.06, "1440": 0.02}

    adx_min = IntParameter(15, 35, default=22, space="buy")
    rsi_low = IntParameter(35, 55, default=45, space="buy")
    rsi_high = IntParameter(60, 80, default=70, space="buy")
    atr_pct_max = DecimalParameter(0.01, 0.06, decimals=3, default=0.03, space="buy")

    rsi_exit = IntParameter(65, 85, default=75, space="sell")
    atr_mult = DecimalParameter(1.5, 4.0, decimals=1, default=2.5, space="sell")

    @informative("4h")
    def populate_indicators_4h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema20"] = ta.EMA(dataframe, timeperiod=20)
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        dataframe["adx"] = ta.ADX(dataframe, timeperiod=14)
        dataframe["atr"] = ta.ATR(dataframe, timeperiod=14)
        dataframe["atr_pct"] = dataframe["atr"] / dataframe["close"]

        cross_up = qtpylib.crossed_above(dataframe["ema20"], dataframe["ema50"])
        dataframe["ema_cross_up"] = cross_up.rolling(3).max().fillna(0)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["close"] > dataframe["ema200_4h"])
                & (dataframe["ema50_4h"] > dataframe["ema200_4h"])
                & (dataframe["ema20"] > dataframe["ema50"])
                & (dataframe["ema_cross_up"] > 0)
                & (dataframe["adx"] > self.adx_min.value)
                & (dataframe["rsi"] > self.rsi_low.value)
                & (dataframe["rsi"] < self.rsi_high.value)
                & (dataframe["atr_pct"] < self.atr_pct_max.value)
                & (dataframe["volume"] > 0)
            ),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                qtpylib.crossed_below(dataframe["ema20"], dataframe["ema50"])
                | (dataframe["rsi"] > self.rsi_exit.value)
            ),
            "exit_long",
        ] = 1
        return dataframe

    def custom_stoploss(
        self,
        pair: str,
        trade,
        current_time: datetime,
        current_rate: float,
        current_profit: float,
        after_fill: bool,
        **kwargs,
    ):
        dataframe, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        if dataframe is None or dataframe.empty:
            return None

        atr = dataframe["atr"].iloc[-1]
        if atr != atr or atr <= 0:
            return None

        stop_price = current_rate - self.atr_mult.value * atr
        value = stoploss_from_absolute(stop_price, current_rate, is_short=False)

        if value is None:
            return None

        # stoploss_from_absolute returns a positive distance; clamp to max 8%
        return min(abs(value), abs(self.stoploss))
