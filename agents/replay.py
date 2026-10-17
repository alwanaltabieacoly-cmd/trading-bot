import argparse
import json
from datetime import timedelta

from . import common, decision_agent
from .run_cycle import build_record, parse_pairs


def _dates(start, end, every_days):
    step = max(1, int(every_days))
    current = start
    while current <= end:
        yield current
        current = current + timedelta(days=step)


def _midnight(value):
    dt = common.parse_utc(value)
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m agents.replay")
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--every-days", type=int, default=1)
    parser.add_argument("--pairs", default=None)
    parser.add_argument("--anonymize", action="store_true")
    parser.add_argument("--no-llm", action="store_true")
    args = parser.parse_args(argv)

    start = _midnight(args.start)
    end = _midnight(args.end)
    pairs = parse_pairs(args.pairs)
    use_llm = not args.no_llm
    suffix = "llm" if use_llm else "rule"

    out_dir = common.DECISIONS_DIR / "replay"
    out_dir.mkdir(parents=True, exist_ok=True)

    for day in _dates(start, end, args.every_days):
        asof = day.strftime("%Y-%m-%d")
        out_path = out_dir / f"{asof}_{suffix}.json"
        if out_path.exists():
            print(f"skip {out_path}")
            continue
        decision = decision_agent.decide(
            pairs,
            day,
            use_llm=use_llm,
            anonymize=args.anonymize,
        )
        generated_at = common.iso_utc(common.utc_now())
        record = build_record(
            decision, pairs, use_llm, False, generated_at, anonymize=args.anonymize
        )
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(record, fh, indent=2, default=str)
        print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
