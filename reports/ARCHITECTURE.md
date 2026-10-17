# Stage 7 architecture: multi-agent veto layer (dry-run only)

Principle: agents produce a *permission* file; the Freqtrade strategy reads it and can only BLOCK or SHRINK entries. No agent can place, modify or close orders. If the file is missing, stale (> 26h) or invalid, the strategy blocks new entries (fail-closed).

## Layout
```
agents/
  common.py          # paths, sqlite/feather loaders, opencode CLI wrapper (timeout, JSON extraction, retries)
  market_agent.py    # deterministic features -> JSON report per pair
  news_agent.py      # reads sentiment/sentiment.sqlite (F&G, GDELT tone, Reddit) -> JSON report
  session_agent.py   # weekday + Asia(00-08 UTC)/London(07-16)/NY(13-21) return/volatility stats per pair
  risk_agent.py      # reads paper-bot API/db: open trades, drawdown, exposure -> size cap
  decision_agent.py  # orchestrator: runs 1-4, builds prompt, calls LLM, validates, writes decision
  run_cycle.py       # entry point (scheduled every 4h); --asof for historical replay tests
reports/decisions/YYYY-MM-DD_HHMM.json   # full record: inputs, prompt, raw LLM text, parsed decision
user_data/decisions/latest.json           # what the strategy reads
```

## Agent outputs (all JSON, numbers computed in Python, LLM only interprets)
- market: per pair, per timeframe 1m/5m/15m/1h/4h/1d: close, EMA50/200 slope, position vs 20/50-period high/low, ATR%, volume z-score; order-book top-20 bid/ask depth and spread via ccxt public `fetch_order_book` (no keys); regime label from rules (bull/bear/range).
- news: latest F&G value + 7d change; GDELT tone mean last 24h vs 7d; Reddit title count/score (if available; currently 403-blocked).
- session: last 90d stats of mean return and ATR by weekday and by session; flags current session.
- risk: account equity, open trades, current and max drawdown of bot B, BTC regime (daily close vs EMA200); hard rules: drawdown > 10% -> block all; BTC below EMA200 -> max size 0.5.
- decision: `{"asof": ts, "pairs": {"BTC/USDT": {"action": "allow|block", "size": 0.0-1.0, "confidence": 0-1, "rationale": "..."}}, "followups": [...]}`. The decision agent may issue up to 2 follow-up questions answered by re-querying agent functions (deterministic), then a final call.

## Safety / validation
- LLM via `opencode run -m opencode/deepseek-v4.1-flash-free` with a 300s timeout, fallback opencode/glm-5.3-flash-free; if both fail -> deterministic rule decision (risk agent rules only), marked `"source":"fallback"`.
- Parsed output is schema-checked; size is clipped to the risk agent cap; any pair not mentioned = block.
- Strategy hook: `confirm_trade_entry` returns False when action != allow; `custom_stake_amount` multiplies by size. Backtests ignore the veto unless a replayed decision file exists (to avoid lookahead, replay uses only data < asof).
- LLM backtests are prone to memorization/look-ahead (see RESEARCH.md); evaluation is forward-only on the paper bot plus a short --asof replay sanity test.