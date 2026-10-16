from datetime import datetime

import talib.abstract as ta
from pandas import DataFrame
from freqtrade.strategy import IStrategy, informative, IntParameter, DecimalParameter
from freqtrade.strategy import stoploss_from_absolute

import freqtrade.vendor.qtpylib.indicators as qtpylib


class PullbackTrend1h(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "1h"
    can_short = False
    startup_candle_count = 250
    process_only_new_candles = True

    stoploss = -0.08
    trailing_stop = False
    use_custom_stoploss = True

    minimal_roi = {
        "0": 0.08,
        "480": 0.04,
        "1440": 0.015,
    }

    adx4h_min = IntParameter(15, 35, default=20, space="buy")
    rsi_buy = IntParameter(25, 45, default=35, space="buy")
    atr_pct_max = DecimalParameter(0.01, 0.06, decimals=3, default=0.035, space="buy")

    rsi_sell = IntParameter(55, 80, default=65, space="sell")
    atr_mult = DecimalParameter(1.5, 4.0, decimals=1, default=2.5, space="sell")

    @informative("4h")
    def populate_indicators_4h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        dataframe["adx"] = ta.ADX(dataframe, timeperiod=14)
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        dataframe["atr"] = ta.ATR(dataframe, timeperiod=14)
        dataframe["atr_pct"] = dataframe["atr"] / dataframe["close"]

        bollinger = qtpylib.bollinger_bands(
            qtpylib.typical_price(dataframe), window=20, stds=2
        )
        dataframe["bb_lower"] = bollinger["lower"]
        dataframe["bb_mid"] = bollinger["mid"]

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["ema50_4h"] > dataframe["ema200_4h"])
                & (dataframe["close"] > dataframe["ema200_4h"])
                & (dataframe["adx_4h"] > self.adx4h_min.value)
                & (dataframe["close"] > dataframe["ema200"])
                & (dataframe["rsi"] < self.rsi_buy.value)
                & (dataframe["close"] < dataframe["bb_lower"] * 1.01)
                & (dataframe["atr_pct"] < self.atr_pct_max.value)
                & (dataframe["volume"] > 0)
            ),
            ["enter_long", "enter_tag"],
        ] = (1, "pullback")

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["rsi"] > self.rsi_sell.value)
                | (
                    (dataframe["close"] > dataframe["bb_mid"])
                    & (dataframe["rsi"] > 50)
                )
            ),
            ["exit_long", "exit_tag"],
        ] = (1, "exit")

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
    ) -> float | None:
        df, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        if df is None or df.empty:
            return None

        atr = df["atr"].iloc[-1]
        stop_price = trade.open_rate - self.atr_mult.value * atr
        value = stoploss_from_absolute(stop_price, current_rate, is_short=False)
        return min(abs(value), 0.08)
