"""Strategy registry.

Every strategy is a named, parameterised rule that maps OHLCV to a
long/cash position. The point of keeping the search space small and
explicit is that a small, readable space cannot hide a curve-fit.

Each entry is:  name -> (build_params, signal_function)
where signal_function(df, **params) returns a boolean Series (True = hold).
"""
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False).mean()


def _rsi(s, n=14):
    delta = s.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def _atr(df, n=14):
    high, low, prev_close = df["high"], df["low"], df["close"].shift(1)
    tr = pd.concat(
        [high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1
    ).max(axis=1)
    return tr.rolling(n).mean()


# --------------------------------------------------------------------------
# strategies
# --------------------------------------------------------------------------


def sma_trend(df, period=200):
    """Hold while close is above its n-period SMA. The proven baseline."""
    ma = _sma(df["close"], period)
    return (df["close"] > ma).fillna(False)


def ema_trend(df, fast=50, slow=200):
    """Hold while the fast EMA is above the slow EMA."""
    return (_ema(df["close"], fast) > _ema(df["close"], slow)).fillna(False)


def donchian_trend(df, period=100):
    """Hold while close is at the n-bar high (breakout trend following)."""
    prior_high = df["high"].rolling(period).max().shift(1)
    return (df["close"] >= prior_high).fillna(False)


def sma_trend_vol_filter(df, period=200, vol_lookback=30, vol_max_pct=3.0):
    """Trend filter, but stand aside when recent volatility is extreme.

    Crypto's biggest crashes come with a volatility spike. Sitting out of
    those is where a large part of the trend rule's edge comes from.
    """
    trend = sma_trend(df, period)
    atr_pct = (_atr(df, 30) / df["close"] * 100.0)
    vol_ok = atr_pct < vol_max_pct
    return (trend & vol_ok).fillna(False)


def sma_trend_rsi_filter(df, period=200, rsi_period=14, rsi_max=70):
    """Trend filter plus an overbought guard."""
    trend = sma_trend(df, period)
    not_overbought = _rsi(df["close"], rsi_period) < rsi_max
    return (trend & not_overbought).fillna(False)


def sma_trend_fast_slow(df, slow_period=200, fast_period=20):
    """Trend filter confirmed by a short-term pullback recovery.

    Enter on a pullback that turns back up, but only inside a long-term
    uptrend. The intent is to enter with less slippage risk than buying
    the exact top.
    """
    slow = _sma(df["close"], slow_period)
    fast = _sma(df["close"], fast_period)
    trend = df["close"] > slow
    recovering = fast > fast.shift(1)
    return (trend & recovering).fillna(False)


def ema_trend_regime(df, fast=50, slow=200, atr_period=14, atr_max_pct=4.0):
    """EMA cross, but only when volatility is not extreme."""
    trend = _ema(df["close"], fast) > _ema(df["close"], slow)
    atr_pct = (_atr(df, atr_period) / df["close"] * 100.0)
    return (trend & (atr_pct < atr_max_pct)).fillna(False)


def donchian_trend_vol_filter(df, period=100, atr_period=14, atr_max_pct=4.0):
    """Breakout trend with a volatility guard."""
    prior_high = df["high"].rolling(period).max().shift(1)
    trend = df["close"] >= prior_high
    atr_pct = (_atr(df, atr_period) / df["close"] * 100.0)
    return (trend & (atr_pct < atr_max_pct)).fillna(False)


# --------------------------------------------------------------------------
# registry
# --------------------------------------------------------------------------
# Each tuple: (id, description, {param: [values]}, signal_fn)
# The runner expands every id x every parameter combination into a candidate.

REGISTRY = [
    (
        "sma_trend",
        "close > SMA(n), else cash",
        {"period": [50, 100, 125, 150, 175, 200, 225, 250, 275, 300, 400]},
        sma_trend,
    ),
    (
        "ema_trend",
        "EMA(fast) > EMA(slow)",
        {"fast": [20, 50], "slow": [100, 200, 300]},
        ema_trend,
    ),
    (
        "donchian_trend",
        "close at n-bar high",
        {"period": [50, 100, 200]},
        donchian_trend,
    ),
    (
        "sma_trend_vol_filter",
        "close > SMA(n) and ATR% below limit",
        {
            "period": [100, 150, 175, 200, 225, 250, 300],
            "vol_lookback": [30],
            "vol_max_pct": [1.5, 2.0, 2.5, 3.0, 4.0],
        },
        sma_trend_vol_filter,
    ),
    (
        "sma_trend_rsi_filter",
        "close > SMA(n) and RSI below limit",
        {
            "period": [100, 150, 200, 250],
            "rsi_period": [14],
            "rsi_max": [60, 70, 80],
        },
        sma_trend_rsi_filter,
    ),
    (
        "sma_trend_fast_slow",
        "close > SMA(slow) and fast SMA rising",
        {"slow_period": [100, 150, 200, 250], "fast_period": [10, 20, 50]},
        sma_trend_fast_slow,
    ),
    (
        "ema_trend_regime",
        "EMA cross with volatility guard",
        {
            "fast": [20, 50],
            "slow": [100, 200],
            "atr_period": [14],
            "atr_max_pct": [2.0, 3.0, 4.0],
        },
        ema_trend_regime,
    ),
    (
        "donchian_trend_vol_filter",
        "breakout trend with volatility guard",
        {
            "period": [50, 100, 200],
            "atr_period": [14],
            "atr_max_pct": [2.0, 3.0, 4.0],
        },
        donchian_trend_vol_filter,
    ),
]


def expand():
    """Yield (candidate_id, params, fn, family, desc) for every combination."""
    import itertools

    out = []
    for sid, desc, grid, fn in REGISTRY:
        keys = list(grid.keys())
        for combo in itertools.product(*[grid[k] for k in keys]):
            params = dict(zip(keys, combo))
            cid = sid + "_" + "_".join(f"{k}{v}" for k, v in params.items())
            out.append((cid, params, fn, sid, desc))
    return out


def describe(cid, params):
    return cid + " " + ",".join(f"{k}={v}" for k, v in sorted(params.items()))
