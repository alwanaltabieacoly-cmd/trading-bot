from datetime import datetime
from typing import Optional

import talib.abstract as ta
from freqtrade.strategy import IStrategy, informative
from pandas import DataFrame


class TrendEmaRsi(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "15m"

    can_short = False

    minimal_roi = {
        "0": 0.06,
        "60": 0.03,
        "240": 0.01,
    }

    stoploss = -0.05

    trailing_stop = True
    trailing_stop_positive = 0.02
    trailing_stop_positive_offset = 0.03
    trailing_only_offset_is_reached = True

    startup_candle_count = 810

    process_only_new_candles = True

    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = False

    def informative_pairs(self):
        pairs = self.dp.current_whitelist()
        return [(pair, "1h") for pair in pairs]

    @informative("1h")
    def populate_indicators_1h(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema20"] = ta.EMA(dataframe, timeperiod=20)
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["ema20"] > dataframe["ema50"])
                & (dataframe["ema20"].shift(1) <= dataframe["ema50"].shift(1))
                & (dataframe["rsi"] >= 45)
                & (dataframe["rsi"] <= 70)
                & (dataframe["close"] > dataframe["ema200_1h"])
                & (dataframe["volume"] > 0)
            ),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (
                    (dataframe["ema20"] < dataframe["ema50"])
                    & (dataframe["ema20"].shift(1) >= dataframe["ema50"].shift(1))
                )
                | (dataframe["rsi"] > 78)
            ),
            "exit_long",
        ] = 1
        return dataframe

    def leverage(self, pair: str, current_time: datetime, current_rate: float,
                 proposed_leverage: float, max_leverage: float, entry_tag: Optional[str],
                 side: str, **kwargs) -> float:
        return 1.0
