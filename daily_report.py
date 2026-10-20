"""Generate a daily digest from decisions + paper broker state."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DECISIONS = ROOT / "reports" / "decisions"
STATE = ROOT / "user_data" / "paper_broker" / "state.json"
LOG = ROOT / "user_data" / "paper_broker" / "trades.jsonl"
OUT = ROOT / "reports" / "daily_digest.md"

def main():
    now = datetime.now(timezone.utc)
    # latest decision
    latest = None
    if (ROOT / "user_data" / "decisions" / "latest.json").exists():
        latest = json.loads((ROOT / "user_data" / "decisions" / "latest.json").read_text())
    else:
        files = sorted(DECISIONS.glob("*.json"))
        if files:
            latest = json.loads(files[-1].read_text())

    state = json.loads(STATE.read_text()) if STATE.exists() else {"cash":0,"equity":0,"positions":{},"trades":[]}
    trades = []
    if LOG.exists():
        trades = [json.loads(l) for l in LOG.read_text().strip().splitlines() if l.strip()]

    lines = [f"# Daily Digest — {now.strftime('%Y-%m-%d %H:%M UTC')}", ""]

    # Portfolio
    lines.append("## Paper Portfolio")
    lines.append(f"- Cash: ${state.get('cash',0):.2f}")
    lines.append(f"- Equity: ${state.get('equity',0):.2f}")
    lines.append(f"- Open positions: {len([p for p in state.get('positions',{}).values() if p.get('qty',0)>0])}")
    lines.append(f"- Total trades logged: {len(trades)}")
    lines.append("")

    # Deliberation
    lines.append("## Latest Deliberation")
    if latest:
        pairs = latest.get("pairs") or latest.get("decision",{}).get("pairs",{})
        for sym, d in (pairs or {}).items():
            action = d.get("action","?")
            size = d.get("size",0)
            conf = d.get("confidence",0)
            lines.append(f"- **{sym}**: {action} (size={size}, conf={conf}) — {d.get('rationale','')[:80]}")
        lines.append(f"- Source: {latest.get('source','?')} | Model: {latest.get('model','?')}")
    else:
        lines.append("- No decision yet.")
    lines.append("")

    # Recent trades
    lines.append("## Recent Trades (last 10)")
    for t in trades[-10:]:
        pnl = t.get("pnl")
        pnl_str = f" pnl={pnl:.2f}" if pnl is not None else ""
        lines.append(f"- {t.get('ts','?')[:16]} {t.get('side','?')} {t.get('symbol','?')} qty={t.get('qty',0):.4f} @ {t.get('price',0)}{pnl_str}")
    if not trades:
        lines.append("- No trades yet.")
    lines.append("")

    # Agent accuracy (if outcome data exists)
    outcome_file = ROOT / "user_data" / "paper_broker" / "outcomes.jsonl"
    if outcome_file.exists():
        outcomes = [json.loads(l) for l in outcome_file.read_text().strip().splitlines() if l.strip()]
        if outcomes:
            wins = sum(1 for o in outcomes if o.get("profitable"))
            lines.append("## Agent Learning")
            lines.append(f"- Evaluated trades: {len(outcomes)}")
            lines.append(f"- Win rate: {wins/len(outcomes)*100:.1f}%")
            lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}")

if __name__ == "__main__":
    main()
