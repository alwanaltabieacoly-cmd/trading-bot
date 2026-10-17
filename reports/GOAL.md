# Main goal (from user, recorded 2026-10-17 02:19 Africa/Tripoli)

Multi-agent decision system on top of Freqtrade. DRY-RUN ONLY. The LLM never places orders.

Agents:
1. Market analyst: multi-timeframe candles 1m/5m/15m/1h/4h/1d, highs/lows, trend, volume, order-book liquidity, bullish/bearish regime.
2. News & social: GDELT, Reddit, Fear & Greed (CryptoPanic later).
3. Session/time: weekday and Asia/London/NY session statistics.
4. Risk: sizing, drawdown, regime.
5. Decision maker: queries all four, may ask follow-ups, outputs a daily/periodic decision {pair, action allow/block/size, confidence, rationale}, logged to reports/decisions/.

The strategy only lets entries through when the decision allows it (veto layer).
LLM backend: OpenCode free models via `opencode run`.

Plan: Stage 7 after Stages 4-6: design in reports/ARCHITECTURE.md, OpenCode implements in agents/, test on recent data, wire into paper bot B as a veto. Add a 1m-timeframe test where feasible. Log everything in reports/PROGRESS.md.