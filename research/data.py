"""Market data fetching and caching.

Uses the public Bybit API through ccxt - no API key needed for candles.
Data is cached as parquet under research/data/ and committed to the repo so
every daily run is auditable and reproducible.
"""
import os
import time

import pandas as pd

from . import config

PARQUET_ENGINE = "pyarrow"


def _cache_path(asset, timeframe):
    return os.path.join(config.DATA_DIR, f"{asset}_{timeframe}.parquet")


def fetch_candles(asset, timeframe, days_back=1600, retries=3):
    """Fetch OHLCV from Bybit public API."""
    import ccxt

    ex = ccxt.bybit({"enableRateLimit": True})
    since = ex.parse8601(
        f"{(pd.Timestamp.utcnow() - pd.Timedelta(days=days_back)).strftime('%Y-%m-%dT%H:%M:%SZ')}"
    )
    all_rows = []
    while since < ex.milliseconds():
        try:
            rows = ex.fetch_ohlcv(
                f"{asset}/USDT", timeframe=timeframe, since=since, limit=1000
            )
        except Exception as e:
            if retries <= 0:
                raise
            retries -= 1
            time.sleep(5)
            continue
        if not rows:
            break
        all_rows.extend(rows)
        last = rows[-1][0]
        if last <= since:
            break
        since = last + 1
        time.sleep(ex.rateLimit / 1000)

    df = pd.DataFrame(
        all_rows, columns=["ts", "open", "high", "low", "close", "volume"]
    )
    df["date"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df.drop(columns=["ts"]).drop_duplicates(subset=["date"]).sort_values("date")
    return df.reset_index(drop=True)


def update_asset(asset, timeframe, days_back=1600):
    """Fetch and merge into the local cache. Returns the cached frame."""
    path = _cache_path(asset, timeframe)
    new = fetch_candles(asset, timeframe, days_back=days_back)

    if os.path.exists(path):
        try:
            old = pd.read_parquet(path)
        except Exception:
            old = None
        if old is not None and len(old):
            new = (
                pd.concat([old, new], ignore_index=True)
                .drop_duplicates(subset=["date"], keep="last")
                .sort_values("date")
                .reset_index(drop=True)
            )

    new.to_parquet(path, index=False, engine=PARQUET_ENGINE)
    return new


def load(asset, timeframe):
    """Load cached data. Returns None if not cached yet."""
    path = _cache_path(asset, timeframe)
    if not os.path.exists(path):
        return None
    try:
        return pd.read_parquet(path)
    except Exception:
        return None


def update_all(assets=None, timeframes=None):
    assets = assets or config.ASSETS
    timeframes = timeframes or config.TIMEFRAMES
    result = {}
    for a in assets:
        for tf in timeframes:
            try:
                df = update_asset(a, tf)
                result[(a, tf)] = df
                print(f"  {a} {tf}: {len(df)} bars "
                      f"({df['date'].iloc[0]} -> {df['date'].iloc[-1]})", flush=True)
            except Exception as e:
                print(f"  {a} {tf}: FAILED {type(e).__name__}: {e}", flush=True)
    return result
