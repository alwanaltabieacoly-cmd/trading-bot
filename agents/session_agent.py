from datetime import timedelta

import pandas as pd

from . import common

SESSIONS = {
    "asia": (0, 8),
    "london": (7, 16),
    "ny": (13, 21),
}

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def _sessions_for_hour(hour):
    return [name for name, (start, end) in SESSIONS.items() if start <= hour < end]


def _stats(sub):
    if sub.empty:
        return None
    return {
        "mean_return": common.rnd(sub["ret"].mean() * 100.0),
        "mean_abs_return": common.rnd(sub["abs_ret"].mean() * 100.0),
        "n": int(len(sub)),
    }


def _pair_stats(pair, asof):
    df = common.load_candles(pair, "1h", asof)
    if df is None:
        return {"available": False}
    horizon = pd.Timestamp(asof - timedelta(days=90))
    df = df[df["date"] >= horizon].copy()
    if len(df) < 2:
        return {"available": False}
    df["ret"] = df["close"].pct_change()
    df = df.dropna(subset=["ret"])
    if df.empty:
        return {"available": False}
    df["abs_ret"] = df["ret"].abs()
    df["weekday"] = df["date"].dt.dayofweek
    df["hour"] = df["date"].dt.hour
    weekday = {WEEKDAYS[wd]: _stats(df[df["weekday"] == wd]) for wd in range(7)}
    session = {
        name: _stats(df[(df["hour"] >= start) & (df["hour"] < end)])
        for name, (start, end) in SESSIONS.items()
    }
    return {"available": True, "weekday": weekday, "session": session}


def analyze(pairs, asof):
    asof_dt = common.parse_utc(asof)
    return {
        "asof": common.iso_utc(asof_dt),
        "current_weekday": WEEKDAYS[asof_dt.weekday()],
        "current_session": _sessions_for_hour(asof_dt.hour),
        "pairs": {pair: _pair_stats(pair, asof_dt) for pair in pairs},
    }
