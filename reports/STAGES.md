# Stage summaries (all numbers from Freqtrade backtest output; dry-run research only)

## Stage 1-2 (commit 96fb200)
- Data: Bybit spot 15m/1h/4h from 2024-01-01 for BTC, ETH, SOL, BNB, XRP /USDT (later 1h/4h from 2023-05-01, 1d from 2023-01-01).
- Baseline TrendEmaRsi (15m): 20251001- on 2 pairs: 298 trades, 112 wins, -4.82%. OOS 20250701- on 5 pairs: 746 trades, 37.0% win, -14.14%, maxDD 14.67%, Sharpe -4.87, market -18.52%.
- In-sample = 20240101-20250630, OOS = 20250701-20261016. Hyperopt SharpeHyperOptLoss, buy+sell spaces, 300 epochs.

| Strategy | IS trades / win% / profit | OOS trades | OOS win% | OOS profit | OOS maxDD | OOS Sharpe | OOS market |
|---|---|---|---|---|---|---|---|
| TrendAdx1h | 33 / 48.5% / +0.85% | 24 | 45.8% | -0.38% | 1.21% | -0.09 | -18.69% |
| PullbackTrend1h | 127 / 63.8% / +5.97% | 113 | 57.5% | -4.31% | 5.04% | -0.95 | -18.69% |

Walk-forward (train->test profit): TrendAdx1h W1 +1.34->-1.16, W2 +1.43->-0.88, W3 -1.25->-0.23 (0/3 positive). PullbackTrend1h W1 +3.34->+0.82, W2 +4.39->-1.92, W3 +3.79->-1.02 (1/3). PullbackTrend1h overfit.

## Stage 3 (commit 763d104)
- Removed stoploss override from config.json (note: TrendAdx1h.json still carries -0.05 from its hyperopt export).
- TrendAdx1hRegime (BTC 1d close>EMA200 + BTC 4h ADX/DI bear filter): IS 34 trades, 61.8%, +2.10%; OOS 11 trades, 45.5%, -0.70%, maxDD 1.09%, Sharpe -0.13, market -18.76%. WF test: -4.68%, -1.56%, +0.08% (1/3).
- FreqaiLgbmRegime (LightGBMRegressor fwd return 12 candles, train 90d/retrain 7d, BTC/ETH/SOL): OOS 20250701-20261015 207 trades, 60.4%, -3.35%, maxDD 8.27%, Sharpe -0.44, market -19.82%. Untuned thresholds.
- Verdict: no validated edge; outperformance vs market comes from sitting in cash.
## Stage 4 (commit 67328f0)
| Strategy | Window | Trades | Win% | Profit | MaxDD | Sharpe | Market |
|---|---|---|---|---|---|---|---|
| BtcEma200Hold (BTC only, 1d) | IS 2024-01..2025-06 | 17 | 17.6% | +5.59% | 2.23% | 0.12 | +142.53% |
| BtcEma200Hold | OOS 2025-07.. | 6 | 33.3% | +0.60% | 0.77% | 0.05 | -22.19% |
| FreqaiClfRegime (entry_prob 0.76) | IS | 1186 | 64.2% | -27.17% | 32.54% | -3.32 | +71.77% |
| FreqaiClfRegime | OOS ..2026-10-15 | 333 | 62.8% | -4.76% | 6.39% | -0.79 | -19.82% |
- Lookahead-analysis on FreqaiClfRegime: 0 biased entries/exits of 20 signals.
- Paper bots (dry-run): A TrendEmaRsi :8081, B TrendAdx1hRegimeVeto :8082 (agent veto), C BtcEma200Hold :8083.
- Sentiment collector: F&G OK; GDELT 429 rate-limited; Reddit 403 blocked.

## Stage 5 - NostalgiaForInfinityX8 (commit 4cd1046 of NFI), OOS 2025-07-01..2026-10-15, 5 pairs, 2 slots
- 5 trades, 4 wins, +1.12%, maxDD 1.46%, market -17.51%. Crippled by our 5-pair/2-slot setup (grind slots limit); stoploss -0.99 + DCA breaks our risk rules. Benchmark only.

## Stage 6
| Strategy | Window | Trades | Win% | Profit | MaxDD | Sharpe | Market |
|---|---|---|---|---|---|---|---|
| EmaTrendBreakout (EMA600 + 48h breakout, round params) | 2022 held-out | 159 | 35.8% | -13.11% | 14.54% | -2.23 | -54.51% |
| EmaTrendBreakout | IS 2024-01..2025-06 | 370 | n/a | -8.07% | 10.89% | -0.79 | +116.22% |
| EmaTrendBreakout | OOS 2025-07.. | 225 | 40.0% | -0.03% | 5.60% | -0.00 | -18.38% |
| EmaTrendBreakout on 1m, BTC+ETH | 2026-09-15..10-15 | 547 | 11.0% | -11.89% | 11.92% | -207.44 | +0.37% |
| FreqaiExampleSpot (stock example, long only) | OOS ..2026-10-15 | 1524 | 42.0% | -50.75% | 51.44% | -12.94 | -19.82% || FreqaiExampleSpot | 2022 held-out (04-15..12-31) | 1847 | see PROGRESS | -59.96% | 62.01% | -19.03 | -69.58% |

## Stage 7 - Multi-agent veto (agents/, design in ARCHITECTURE.md)
- 4 deterministic agents (market multi-TF 1m..1d + order book, news F&G/GDELT/Reddit, session stats, risk) + LLM decision maker (OpenCode deepseek-v4.1-flash-free, fallback glm-5.3-flash-free, fallback deterministic rule). Up to 2 follow-up rounds.
- Wired into paper bot B (TrendAdx1hRegimeVeto) as a fail-closed veto via user_data/decisions/latest.json; cycle every 4h (Scheduled Task AgentsCycle). LLM never places orders.
- Historical replay, ANONYMIZED prompts (no pair names, dates, weekday, absolute prices; leak-audited), 23 dates every 21 days 2025-07-07..2026-10-05 (all source=llm, 0 fallbacks), vs deterministic rule on 66 weekly dates. Forward returns from 1h candles (agents/evaluate_replay.py, reports/REPLAY_RESULTS.md):

| source | decisions (allow/block) | mean 24h allowed / blocked / always | mean 7d allowed / blocked / always | 7d hit rate allowed / blocked / always |
|---|---|---|---|---|
| LLM (anonymized) | 115 (38/77) | -0.18% / +0.37% / +0.19% | +2.33% / +0.48% / +1.09% | 0.605 / 0.571 / 0.583 |
| Rule (1h+4h bull) | 330 (96/234) | -0.14% / +0.39% / +0.24% | -0.26% / +0.16% / +0.04% | 0.417 / 0.474 / 0.458 |

- Interpretation: LLM-allowed decisions had better 7d but worse 24h returns than blocked ones. Only 23 dates and 5 highly correlated pairs (effectively ~23 independent samples): NOT statistically meaningful. The simple rule filter showed no value.
- Caveats: (1) LLM memorization/look-ahead: anonymization removes names/dates/prices but Fear&Greed and GDELT values can still hint at a period; the model's knowledge cutoff is unknown, so 2025-2026 dates may be inside its training data. (2) Replay ignores risk-agent account data and live order book. (3) Decisions are not costed as trades. Forward paper trading on bot B is the only clean test.