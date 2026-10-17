import csv
import sqlite3
from datetime import datetime, timedelta, timezone

from . import common


def _parse_ts(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        pass
    for fmt in ("%Y%m%dT%H%M%SZ", "%Y%m%dT%H%M%S", "%Y%m%d%H%M%S", "%Y%m%d", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value).strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _fng_class(value):
    if value is None:
        return None
    if value <= 24:
        return "Extreme Fear"
    if value <= 49:
        return "Fear"
    if value <= 74:
        return "Greed"
    return "Extreme Greed"


def _query(sql, params=()):
    path = common.SENTIMENT_DB
    if not path.exists():
        return []
    conn = sqlite3.connect(str(path))
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(sql, params)
        return [dict(row) for row in cur.fetchall()]
    except sqlite3.Error:
        return []
    finally:
        conn.close()


def _fng_series():
    path = common.FNG_CSV
    if not path.exists():
        return []
    rows = []
    try:
        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                raw_date = row.get("date")
                raw_value = row.get("fng")
                if raw_date is None or raw_value is None:
                    continue
                try:
                    value = int(float(raw_value))
                except (TypeError, ValueError):
                    continue
                try:
                    day = datetime.strptime(raw_date.strip(), "%Y-%m-%d").replace(
                        tzinfo=timezone.utc
                    )
                except ValueError:
                    continue
                rows.append((day, value))
    except OSError:
        return []
    rows.sort(key=lambda item: item[0])
    return rows


def _fng_from_csv(series, asof):
    usable = [(d, v) for d, v in series if d + timedelta(days=1) <= asof]
    if not usable:
        return None, None
    day, value = usable[-1]
    target = day - timedelta(days=7)
    prior = [v for d, v in usable if d <= target]
    change = value - prior[-1] if prior else None
    entry = {
        "value": value,
        "classification": _fng_class(value),
        "date": day.date().isoformat(),
        "source": "csv",
    }
    return entry, change


def _fng_from_db(rows, asof):
    parsed = []
    for row in rows:
        collected = _parse_ts(row.get("ts_utc"))
        if collected is None or collected > asof:
            continue
        effective = _parse_ts(row.get("source_ts")) or collected
        parsed.append((effective, row))
    if not parsed:
        return None, None
    parsed.sort(key=lambda item: item[0])
    effective, latest = parsed[-1]
    value = latest.get("value")
    try:
        value = int(value)
    except (TypeError, ValueError):
        value = None
    target = effective - timedelta(days=7)
    prior = [r for eff, r in parsed if eff <= target]
    change = None
    if value is not None and prior:
        try:
            change = value - int(prior[-1].get("value"))
        except (TypeError, ValueError):
            change = None
    entry = {
        "value": value,
        "classification": latest.get("classification"),
        "date": effective.date().isoformat(),
        "source": "sqlite",
    }
    return entry, change


def _latest_fng(asof):
    csv_entry, csv_change = _fng_from_csv(_fng_series(), asof)
    db_entry, db_change = _fng_from_db(
        _query("SELECT ts_utc, value, classification, source_ts FROM fng"), asof
    )
    candidates = []
    if csv_entry:
        candidates.append((csv_entry["date"], csv_entry, csv_change))
    if db_entry:
        candidates.append((db_entry["date"], db_entry, db_change))
    if not candidates:
        return None, None
    candidates.sort(key=lambda item: item[0])
    _, entry, change = candidates[-1]
    return entry, change


def _gdelt(rows, asof):
    horizon_1d = asof - timedelta(hours=24)
    horizon_7d = asof - timedelta(days=7)
    buckets = {}
    for row in rows:
        collected = _parse_ts(row.get("ts_utc"))
        if collected is None or collected > asof:
            continue
        tone = row.get("tone")
        if tone is None:
            continue
        try:
            tone = float(tone)
        except (TypeError, ValueError):
            continue
        bucket = _parse_ts(row.get("bucket_date")) or collected
        query = row.get("query")
        slot = buckets.setdefault(query, {"24h": [], "7d": []})
        if horizon_7d < bucket <= asof:
            slot["7d"].append(tone)
            if bucket > horizon_1d:
                slot["24h"].append(tone)
    out = {}
    for query, slot in buckets.items():
        tones_1d = slot["24h"]
        tones_7d = slot["7d"]
        out[query] = {
            "tone_24h": common.rnd(sum(tones_1d) / len(tones_1d)) if tones_1d else None,
            "tone_7d": common.rnd(sum(tones_7d) / len(tones_7d)) if tones_7d else None,
            "n_24h": len(tones_1d),
            "n_7d": len(tones_7d),
        }
    return out


def _reddit(rows, asof):
    if not rows:
        return None
    horizon_1d = (asof - timedelta(hours=24)).timestamp()
    horizon_7d = (asof - timedelta(days=7)).timestamp()
    posts_24h = 0
    posts_7d = 0
    score_24h = 0
    total = 0
    for row in rows:
        collected = _parse_ts(row.get("ts_utc"))
        if collected is None or collected > asof:
            continue
        try:
            created = float(row.get("created_utc"))
        except (TypeError, ValueError):
            continue
        total += 1
        if created > horizon_7d:
            posts_7d += 1
            if created > horizon_1d:
                posts_24h += 1
                try:
                    score_24h += int(row.get("score"))
                except (TypeError, ValueError):
                    pass
    return {
        "posts_24h": posts_24h,
        "posts_7d": posts_7d,
        "score_24h": score_24h,
        "total_stored": total,
    }


def analyze(asof):
    asof_dt = common.parse_utc(asof)
    fng, fng_change = _latest_fng(asof_dt)
    gdelt = _gdelt(
        _query("SELECT ts_utc, query, bucket_date, tone FROM gdelt_tone"), asof_dt
    )
    reddit = _reddit(
        _query("SELECT ts_utc, subreddit, created_utc, score FROM reddit_posts"), asof_dt
    )
    return {
        "asof": common.iso_utc(asof_dt),
        "fng": fng,
        "fng_7d_change": fng_change,
        "gdelt": gdelt,
        "reddit": reddit,
    }
