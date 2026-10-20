import unittest
import numpy as np
import pandas as pd
from research import engine, validate, config

class TestEngineMetrics(unittest.TestCase):
    def test_years_zero_guard(self):
        r = np.array([0.01]*2)
        m = engine.metrics(r, 365)
        self.assertEqual(m, {})

    def test_buy_and_hold_turnover(self):
        df = pd.DataFrame({"close":[100.0,110.0,105.0]})
        net, trades = engine.buy_and_hold(df)
        self.assertEqual(trades, 1)
        self.assertAlmostEqual(net[1], 0.10 - config.COST_PER_SIDE, places=9)

    def test_date_mask(self):
        dates = pd.Series(["2020-01-01","2020-01-02","2020-01-03"], dtype="datetime64[ns, UTC]" if False else None)
        # simpler
        d = pd.to_datetime(["2020-01-01","2020-01-02","2020-01-03"], utc=True)
        m = engine.date_mask(d, start="2020-01-02", end="2020-01-03")
        self.assertTrue(m.tolist()==[False,True,False])

class TestValidateGate(unittest.TestCase):
    def test_passes_gate_returns_bool_and_reasons(self):
        cand = {"train_cagr":10.0,"holdout_cagr":5.0,"assets_positive":3,"assets_tested":5,"train_dd":-10.0,"dsr":0.99}
        ok, reasons = validate.passes_gate(cand)
        self.assertTrue(ok)
        self.assertEqual(reasons, [])
    def test_passes_basic_holdout_cagr(self):
        cand = {"train_cagr":10.0,"holdout_cagr":-1.0,"assets_positive":3,"assets_tested":5,"train_dd":-10.0}
        ok, reasons = validate.passes_basic(cand)
        self.assertFalse(ok)
        self.assertTrue(any("holdout CAGR" in r for r in reasons))

if __name__=="__main__":
    unittest.main()
