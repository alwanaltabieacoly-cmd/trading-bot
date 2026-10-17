import sys, os

sys.path.append(os.path.dirname(__file__))
from FreqaiExampleStrategy import FreqaiExampleStrategy


class FreqaiExampleSpot(FreqaiExampleStrategy):
    can_short = False
    timeframe = "1h"
    startup_candle_count = 40
