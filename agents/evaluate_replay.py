import argparse
import json

import pandas as pd

from . import common

FAR_FUTURE = "2100-01-01T00:00:00+00:00"
REPLAY_DIR = common.DECISIONS_DIR / "replay"
RESULTS_PATH = common.PROJECT_ROOT / "reports" / "REPLAY_RESULTS.md"
SOURCES = ("llm", "rule")


def _price_at(df, ts):
    sub = df[df["date"] <= ts]
    if sub.empty:
        return None, None
    row = sub.iloc[-1]
    try:
        price = float(row["close"])
    except (TypeError, ValueError):
        return None, None
    if not price:
        return None, None
    return price, row["date"]


def _forward_returns(pair, asof_dt):
    df = common.load_candles(pair, "1h", FAR_FUTURE)
    if df is None or df.empty:
        return None
    asof_ts = pd.Timestamp(asof_dt)
    entry, entry_date = _price_at(df, asof_ts)
    if entry is None:
        return None
    price_24h, date_24h = _price_at(df, asof_ts + pd.Timedelta(hours=24))
    price_7d, date_7d = _price_at(df, asof_ts + pd.Timedelta(days=7))
    ret_24h = None
    if price_24h is not None and date_24h is not None and date_24h > entry_date:
        ret_24h = price_24h / entry - 1.0
    ret_7d = None
    if price_7d is not None and date_7d is not None and date_7d > entry_date:
        ret_7d = price_7d / entry - 1.0
    return ret_24h, ret_7d


def _load_records():
    records = []
    if not REPLAY_DIR.exists():
        return records
    for path in sorted(REPLAY_DIR.glob("*.json")):
        try:
            with open(path, encoding="utf-8") as fh:
                record = json.load(fh)
        except (OSError, ValueError):
            continue
        if not isinstance(record, dict):
            continue
        record["_suffix"] = path.stem.rsplit("_", 1)[-1] if "_" in path.stem else ""
        records.append(record)
    return records


def _source(record):
    if isinstance(record.get("use_llm"), bool):
        return "llm" if record["use_llm"] else "rule"
    return "llm" if record.get("_suffix") == "llm" else "rule"


def _collect_rows(records):
    rows = []
    for record in records:
        asof = record.get("asof")
        if asof is None:
            continue
        try:
            asof_dt = common.parse_utc(asof)
        except (TypeError, ValueError):
            continue
        decision = record.get("decision")
        decisions = decision.get("pairs") if isinstance(decision, dict) else None
        if not isinstance(decisions, dict):
            continue
        pairs = record.get("pairs")
        if not isinstance(pairs, list) or not pairs:
            pairs = list(decisions.keys())
        source = _source(record)
        for pair in pairs:
            item = decisions.get(pair)
            if not isinstance(item, dict):
                continue
            returns = _forward_returns(pair, asof_dt)
            if returns is None:
                continue
            ret_24h, ret_7d = returns
            if ret_24h is None and ret_7d is None:
                continue
            rows.append(
                {
                    "source": source,
                    "pair": pair,
                    "asof": asof,
                    "action": item.get("action"),
                    "ret_24h": ret_24h,
                    "ret_7d": ret_7d,
                }
            )
    return rows


def _stats(series):
    values = pd.Series(series, dtype="float64").dropna()
    if values.empty:
        return None, None
    return float(values.mean()), float(values.median())


def _hit_rate(series):
    values = pd.Series(series, dtype="float64").dropna()
    if values.empty:
        return None
    return float((values > 0).mean())


def _summarize(df):
    summary = {}
    for source in SOURCES:
        sub = df[df["source"] == source]
        allowed = sub[sub["action"] == "allow"]
        blocked = sub[sub["action"] == "block"]
        summary[source] = {
            "decisions": int(len(sub)),
            "allow": int(len(allowed)),
            "block": int(len(blocked)),
            "allow_24h": _stats(allowed["ret_24h"]),
            "allow_7d": _stats(allowed["ret_7d"]),
            "block_24h": _stats(blocked["ret_24h"]),
            "block_7d": _stats(blocked["ret_7d"]),
            "allow_hit": _hit_rate(allowed["ret_7d"]),
            "block_hit": _hit_rate(blocked["ret_7d"]),
            "baseline_24h": _stats(sub["ret_24h"]),
            "baseline_7d": _stats(sub["ret_7d"]),
            "baseline_hit": _hit_rate(sub["ret_7d"]),
        }
    return summary


def _pct(value):
    if value is None:
        return "n/a"
    return f"{float(value) * 100.0:.2f}%"


def _num(value):
    if value is None:
        return "n/a"
    return f"{float(value):.3f}"


def _render(summary, n_records, n_rows):
    lines = [
        "# Replay evaluation results",
        "",
        f"- replay records read: {n_records}",
        f"- pair decisions with forward returns: {n_rows}",
        f"- generated: {common.iso_utc(common.utc_now())}",
        "- forward returns: 1h candles, 24h and 7d after asof",
        "",
    ]
    for source in SOURCES:
        data = summary[source]
        lines.append(f"## source: {source}")
        lines.append("")
        lines.append(
            f"- decisions: {data['decisions']} "
            f"(allow {data['allow']}, block {data['block']})"
        )
        lines.append("")
        lines.append("| metric | allowed | blocked | always allow |")
        lines.append("| --- | --- | --- | --- |")
        lines.append(
            f"| mean 24h return | {_pct(data['allow_24h'][0])} | "
            f"{_pct(data['block_24h'][0])} | {_pct(data['baseline_24h'][0])} |"
        )
        lines.append(
            f"| median 24h return | {_pct(data['allow_24h'][1])} | "
            f"{_pct(data['block_24h'][1])} | {_pct(data['baseline_24h'][1])} |"
        )
        lines.append(
            f"| mean 7d return | {_pct(data['allow_7d'][0])} | "
            f"{_pct(data['block_7d'][0])} | {_pct(data['baseline_7d'][0])} |"
        )
        lines.append(
            f"| median 7d return | {_pct(data['allow_7d'][1])} | "
            f"{_pct(data['block_7d'][1])} | {_pct(data['baseline_7d'][1])} |"
        )
        lines.append(
            f"| hit rate 7d > 0 | {_num(data['allow_hit'])} | "
            f"{_num(data['block_hit'])} | {_num(data['baseline_hit'])} |"
        )
        lines.append("")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m agents.evaluate_replay")
    parser.parse_args(argv)
    records = _load_records()
    rows = _collect_rows(records)
    df = pd.DataFrame(
        rows, columns=["source", "pair", "asof", "action", "ret_24h", "ret_7d"]
    )
    summary = _summarize(df)
    text = _render(summary, len(records), int(len(df)))
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_PATH, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
