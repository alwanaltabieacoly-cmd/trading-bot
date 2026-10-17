import talib.abstract as ta

from freqtrade.strategy import IStrategy


class EmaTrendBreakout(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "1h"
    can_short = False

    startup_candle_count = 650
    process_only_new_candles = True

    stoploss = -0.05
    trailing_stop = True
    trailing_stop_positive = 0.02
    trailing_stop_positive_offset = 0.04
    trailing_only_offset_is_reached = True
    minimal_roi = {"0": 100}

    def populate_indicators(self, dataframe, metadata):
        dataframe["ema600"] = ta.EMA(dataframe, timeperiod=600)
        dataframe["dc_high"] = dataframe["high"].rolling(48).max().shift(1)
        dataframe["dc_low"] = dataframe["low"].rolling(24).min().shift(1)
        dataframe["vol_ma"] = dataframe["volume"].rolling(48).mean()
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[
            (dataframe["close"] > dataframe["ema600"])
            & (dataframe["close"] > dataframe["dc_high"])
            & (dataframe["volume"] > dataframe["vol_ma"])
            & (dataframe["volume"] > 0),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[
            (dataframe["close"] < dataframe["dc_low"])
            | (dataframe["close"] < dataframe["ema600"]),
            "exit_long",
        ] = 1
        return dataframe
