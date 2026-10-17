import numpy as np
import pandas as pd

from . import common


def _ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


def _atr_pct(df, period=14):
    high = df["high"]
    low = df["low"]
    close = df["close"]
    prev = close.shift(1)
    tr = pd.concat(
        [(high - low), (high - prev).abs(), (low - prev).abs()], axis=1
    ).max(axis=1)
    atr = tr.rolling(period).mean().iloc[-1]
    last_close = close.iloc[-1]
    if not np.isfinite(atr) or not last_close:
        return None
    return float(atr / last_close * 100.0)


def _orderbook(pair):
    try:
        import ccxt

        exchange = ccxt.bybit()
        ob = exchange.fetch_order_book(pair, limit=50)
        bids = ob.get("bids") or []
        asks = ob.get("asks") or []
        if not bids or not asks:
            return None
        best_bid = float(bids[0][0])
        best_ask = float(asks[0][0])
        mid = (best_bid + best_ask) / 2.0
        if not mid:
            return None
        spread_pct = (best_ask - best_bid) / mid * 100.0
        bid_depth = sum(float(p) * float(q) for p, q in bids if float(p) >= mid * 0.99)
        ask_depth = sum(float(p) * float(q) for p, q in asks if float(p) <= mid * 1.01)
        return {
            "spread_pct": common.rnd(spread_pct),
            "bid_depth_1pct_usdt": common.rnd(bid_depth, 2),
            "ask_depth_1pct_usdt": common.rnd(ask_depth, 2),
        }
    except Exception:
        return None


def _timeframe(pair, tf, asof):
    df = common.load_candles(pair, tf, asof)
    if df is None or len(df) < 2:
        return {"available": False}
    close = df["close"]
    ema50 = _ema(close, 50)
    ema200 = _ema(close, 200)
    last_close = float(close.iloc[-1])
    last_ema50 = float(ema50.iloc[-1])
    last_ema200 = float(ema200.iloc[-1])
    slope = None
    if len(ema50) > 5 and float(ema50.iloc[-6]):
        slope = float((ema50.iloc[-1] - ema50.iloc[-6]) / ema50.iloc[-6] * 100.0)
    dist_high = None
    dist_low = None
    if len(df) >= 20:
        high20 = float(df["high"].rolling(20).max().iloc[-1])
        low20 = float(df["low"].rolling(20).min().iloc[-1])
        if high20:
            dist_high = (last_close - high20) / high20 * 100.0
        if low20:
            dist_low = (last_close - low20) / low20 * 100.0
    vol_z = None
    vol = df["volume"]
    if len(vol) >= 48:
        window = vol.iloc[-48:]
        std = float(window.std(ddof=0))
        if np.isfinite(std) and std:
            vol_z = float((float(vol.iloc[-1]) - float(window.mean())) / std)
    if last_close > last_ema200 and last_ema50 > last_ema200:
        regime = "bull"
    elif last_close < last_ema200 and last_ema50 < last_ema200:
        regime = "bear"
    else:
        regime = "range"
    return {
        "available": True,
        "close": common.rnd(last_close),
        "ema50": common.rnd(last_ema50),
        "ema200": common.rnd(last_ema200),
        "ema50_slope": common.rnd(slope),
        "dist_to_high20_pct": common.rnd(dist_high),
        "dist_to_low20_pct": common.rnd(dist_low),
        "atr_pct_14": common.rnd(_atr_pct(df)),
        "volume_z_48": common.rnd(vol_z),
        "regime": regime,
    }


def analyze(pairs, asof, live_orderbook=False):
    asof_dt = common.parse_utc(asof)
    report = {
        "asof": common.iso_utc(asof_dt),
        "live_orderbook": bool(live_orderbook),
        "pairs": {},
    }
    for pair in pairs:
        entry = {"timeframes": {}}
        for tf in common.TIMEFRAMES:
            entry["timeframes"][tf] = _timeframe(pair, tf, asof_dt)
        if live_orderbook:
            entry["orderbook"] = _orderbook(pair)
        report["pairs"][pair] = entry
    return report
