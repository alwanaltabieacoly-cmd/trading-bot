import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "sentiment.sqlite"
LOG_PATH = BASE_DIR / "collector.log"
TIMEOUT = 20
GDELT_SLEEP = 12


def utc_now_iso():
    return datetime.now(timezone.utc).isoformat()


def log(line):
    ts = utc_now_iso()
    entry = f"{ts} {line}"
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(entry + "\n")
    print(entry)


def init_db(conn):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS fng ("
        "ts_utc TEXT, value INTEGER, classification TEXT, source_ts TEXT)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS gdelt_tone ("
        "ts_utc TEXT, query TEXT, bucket_date TEXT, tone REAL)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS reddit_posts ("
        "ts_utc TEXT, subreddit TEXT, post_id TEXT, title TEXT, "
        "score INTEGER, num_comments INTEGER, created_utc REAL)"
    )
    conn.commit()


def collect_fng(conn):
    ts = utc_now_iso()
    resp = requests.get("https://api.alternative.me/fng/?limit=1", timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    item = data["data"][0]
    value = int(item["value"])
    classification = item.get("value_classification")
    source_ts = datetime.fromtimestamp(
        int(item["timestamp"]), tz=timezone.utc
    ).isoformat()
    conn.execute(
        "INSERT INTO fng (ts_utc, value, classification, source_ts) VALUES (?, ?, ?, ?)",
        (ts, value, classification, source_ts),
    )
    conn.commit()
    return 1


def collect_gdelt(conn):
    ts = utc_now_iso()
    count = 0
    for i, query in enumerate(["bitcoin", "ethereum"]):
        conn.commit()  # keep earlier queries if a later one is rate-limited
        if i > 0:
            time.sleep(GDELT_SLEEP)
        url = (
            "https://api.gdeltproject.org/api/v2/doc/doc"
            f"?query={query}&mode=timelinetone&format=json&timespan=1d"
        )
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        try:
            data = resp.json()
        except ValueError:
            raise ValueError(f"GDELT returned non-JSON response for '{query}'")
        timeline = data.get("timeline") or []
        if not timeline:
            continue
        for point in timeline[0].get("data", []):
            conn.execute(
                "INSERT INTO gdelt_tone (ts_utc, query, bucket_date, tone) "
                "VALUES (?, ?, ?, ?)",
                (ts, query, point.get("date"), float(point.get("value"))),
            )
            count += 1
    conn.commit()
    return count


def collect_reddit(conn):
    ts = utc_now_iso()
    headers = {"User-Agent": "windows:sentiment-collector:v0.1 (personal research)"}
    count = 0
    for sub in ["CryptoCurrency", "Bitcoin"]:
        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=25"
        resp = requests.get(url, headers=headers, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        for child in data.get("data", {}).get("children", []):
            post = child.get("data", {})
            conn.execute(
                "INSERT INTO reddit_posts "
                "(ts_utc, subreddit, post_id, title, score, num_comments, created_utc) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    ts,
                    sub,
                    post.get("id"),
                    post.get("title"),
                    post.get("score"),
                    post.get("num_comments"),
                    post.get("created_utc"),
                ),
            )
            count += 1
    conn.commit()
    return count


def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        init_db(conn)

        try:
            n = collect_fng(conn)
            log(f"fng: stored {n} row(s)")
        except Exception as exc:
            log(f"fng: ERROR {exc}")

        try:
            n = collect_gdelt(conn)
            log(f"gdelt_tone: stored {n} row(s)")
        except Exception as exc:
            log(f"gdelt_tone: ERROR {exc}")

        try:
            n = collect_reddit(conn)
            log(f"reddit_posts: stored {n} row(s)")
        except Exception as exc:
            log(f"reddit_posts: ERROR {exc}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
