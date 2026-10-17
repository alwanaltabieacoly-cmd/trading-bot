import talib.abstract as ta

from freqtrade.strategy import IStrategy


class BtcEma200Hold(IStrategy):
    INTERFACE_VERSION = 3

    timeframe = "1d"
    can_short = False

    startup_candle_count = 250
    process_only_new_candles = True

    stoploss = -0.08
    trailing_stop = False
    minimal_roi = {"0": 100}

    def populate_indicators(self, dataframe, metadata):
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[
            (dataframe["close"] > dataframe["ema200"]) & (dataframe["volume"] > 0),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[
            dataframe["close"] < dataframe["ema200"],
            "exit_long",
        ] = 1
        return dataframe
