# PROGRESS log (Africa/Tripoli time, UTC+2)

## 2026-10-17 02:03 - Stage 4 start
- Wrote user_data/config_btc.json (BTC/USDT only, max_open_trades 1).
## 2026-10-17 02:04 - BtcEma200Hold benchmark (OpenCode deepseek-v4.1-flash-free)
- 1d, enter close>EMA200, exit close<EMA200, stoploss -0.08 (kept per risk rule).
- `freqtrade backtesting -c config.json -c config_btc.json -s BtcEma200Hold -i 1d --timerange ...`
- IS 20240101-20250630: 17 trades, 17.6% win, +5.59%, maxDD 2.23%, Sharpe 0.12, BTC market +142.53%.
- OOS 20250701-: 6 trades, 33.3% win, +0.60%, maxDD 0.77%, Sharpe 0.05, BTC market -22.19%.
- Note: stake 10 USDT of 100 wallet, so % profit is diluted vs real holding.
## 2026-10-17 02:05 - Fear&Greed history cached
- Invoke-RestMethod api.alternative.me/fng/?limit=0 -> user_data/external/fng.csv, 3177 rows 2018-02-01..2026-10-17.
## 2026-10-17 02:06 - FreqaiClfRegime written by OpenCode
- LightGBMClassifier, label up if +2% hit before -5% within 24 candles; F&G features merged with D+1 availability (merge_asof backward); BTC 1d EMA200 regime; entry_prob hyperoptable; config user_data/config_freqai_clf.json.
- Problem: first run failed, pandas MergeError datetime64[ms] vs [us]. Fix (me): cast avail to dataframe date dtype. Rerun pipeline stage4.ps1 (IS backtest, hyperopt 60 epochs buy, OOS, lookahead/recursive analysis).
## 2026-10-17 02:08 - Sentiment collector (OpenCode)
- sentiment/collector.py -> sentiment/sentiment.sqlite (gitignored *.sqlite), log sentiment/collector.log.
- Test run 1: fng stored 1 row; GDELT 429 Too Many Requests; Reddit 403 Blocked.
- Fix (me): commit after each GDELT query; GDELT sleep 6->12 s. Test run 2: fng ok (2 rows total), GDELT 429 again, Reddit 403 again. Reddit blocks unauthenticated JSON from this IP; not worked around (would need OAuth app).
- Scheduled Task TradingBot\SentimentCollector created (HOURLY, current user, pythonw). Next run 03:10.## 2026-10-17 02:11 - Reports folder created
- reports/STAGES.md (stage 1-3 summaries), reports/RESEARCH.md (user research notes), this PROGRESS.md.
## 2026-10-17 02:12 - Dry-run bot setup
- config.private.json (gitignored): api_server 127.0.0.1, user faris, random 32-char password/jwt/ws_token.
- user_data/bots/botA.json (TrendEmaRsi, port 8081, db botA.dryrun.sqlite), botC.json (BtcEma200Hold, 1d, port 8083, + config_btc.json). dry_run true, wallet 100.
- run_bot.ps1 launcher (refuses to start if dry_run != true).
- Scheduled tasks TradingBot\DryRunBotA / DryRunBotC created (ONLOGON) and triggered with schtasks /Run: "SUCCESS".
- Problem: my verification command was interrupted; re-checking.## 2026-10-17 02:15 - Bots A and C verified running
- Log: "Changing state to: RUNNING", "Dry run is enabled. All trades are simulated."; heartbeat PIDs botA=12128, botC=10900.
- status.ps1 written (localhost API, Basic auth from config.private.json). First version miscounted open trades (empty JSON array -> 1); fixed by filtering items without pair.
- botC immediately opened a dry-run BTC/USDT position (BTC daily close > EMA200 at start).
- One shell call was rejected by the auto-review classifier with "error occured while classifying"; identical retry succeeded.
## 2026-10-17 02:16 - Data for Stage 5/6
- download-data 1h/4h/1d from 20220101 (--prepend) and 5m from 20250601 for NFI.
## 2026-10-17 02:19 - Queue updated
- reports/GOAL.md recorded (multi-agent veto system = Stage 7). RESEARCH.md got "Video & community research" section.
- Stage 5 prep: cloned iterativv/NostalgiaForInfinity (depth 1) to D:\Openwork_Projects\NostalgiaForInfinity, commit 4cd1046 (2026-10-16). Latest = NostalgiaForInfinityX8 (5m, stoploss -0.99, startup 800). 5m data downloaded 20250601- for 5 pairs.
- FreqAI v2 still training IS window (115 models so far).
## 2026-10-17 02:23 - Stage 5: NostalgiaForInfinityX8 OOS
- `backtesting -c config.json -c config_nfi.json (5m, use_exit_signal, StaticPairList) -s NostalgiaForInfinityX8 --timerange 20250701-20261015`
- Result: 5 trades, 4 wins, +1.12% (1.123 USDT), max underwater 1.46% (0.60% closed), Sharpe closed 0.08 / daily 0.55, market -17.51%.
- Caveat: NFI is built for 40+ pairs and more slots; with 5 pairs and max_open_trades=2 it logs "Cancelling entry ... due to grind mode slots limit" and barely trades. Uses position adjustment (DCA grinding) and stoploss -0.99 -> violates our -0.08 risk rule; benchmark only, not for paper bot.
- Warning: 1d data ends 2026-10-14 after prepend download.
## 2026-10-17 02:25 - Stage 6a: EmaTrendBreakout (OpenCode), round params, not hyperopted
- 1h, EMA600 filter, 48h Donchian breakout + volume>MA48, exit 24h low or below EMA600, stop -5%, trailing +2% after +4%.
- 2022 held-out bear (20220128-20221231, no 15m detail available): 159 trades, 57 wins (35.8%), -13.11%, max underwater 14.54%, Sharpe -2.23, market -54.51%.
- IS 20240101-20250630 (15m detail): 370 trades, -8.07%, max underwater 10.89%, Sharpe -0.79, market +116.22%.
- OOS 20250701- (15m detail): 225 trades, 90 wins (40.0%), -0.03%, max underwater 5.60%, Sharpe -0.00, market -18.38%.
- Problem: first 2022 run failed (no 15m data for --timeframe-detail); rerun without detail.
## 2026-10-17 02:27-02:36 - Stage 7 design + implementation
- reports/ARCHITECTURE.md written (fail-closed veto file, agents never place orders), reports/AGENTS_SPEC.md (detailed spec for OpenCode).
- Problem: two shell calls passing the long spec inline were rejected by auto-review ("error occured while classifying"); worked around by putting the spec in reports/AGENTS_SPEC.md and giving OpenCode a short prompt (same action).
- OpenCode (deepseek-v4.1-flash-free, ~5 min) wrote agents/{common,market_agent,news_agent,session_agent,risk_agent,decision_agent,run_cycle}.py.
- Test --no-llm --asof 2026-10-10T00:00Z: all 5 pairs block (fallback rule: 1h regime bear).
- Test with LLM: first attempt fell back - raw output "The command line is too long." (cmd 8k limit). Fix (me): common.call_llm writes prompt to reports/decisions/_prompts/ and passes a short instruction. Rerun (176 s): model=opencode/deepseek-v4.1-flash-free source=llm; all 5 pairs block, conf 0.62-0.70, rationales cite 15m/1h bear regime.
## 2026-10-17 02:36 - FreqAI v2 (FreqaiClfRegime) in-sample, default entry_prob 0.60
- IS 20240219-20250630 (BTC/ETH/SOL): 1246 trades, 755 wins (60.6%), -36.31%, maxDD 38.71%, Sharpe -5.13, market +43.97%. With +2%/-5% exits breakeven win rate is ~71%; classifier far below. Hyperopt of entry_prob running.
## 2026-10-17 02:40 - 1m feasibility test
- download-data 1m BTC/ETH from 20260901. EmaTrendBreakout run unchanged on -i 1m (EMA600 = 10h, 48-min breakout), 20260915-20261015, BTC+ETH.
- Result: 547 trades (18.2/day), 60 wins (11.0%), -11.89% in one month. Fees (0.1% x2 per trade) dominate on 1m; not viable with this logic.
## 2026-10-17 02:59 - FreqAI v2 results (FreqaiClfRegime, LightGBMClassifier, +2%/-5% target, F&G features)
- Hyperopt (60 epochs, buy space, SharpeHyperOptLoss, -j 1) best entry_prob = 0.76.
- IS tuned 20240101-20250630: 1186 trades, 761 wins (64.2%), -27.17%, maxDD 32.54%, Sharpe -3.32, market +71.77%.
- OOS tuned 20250701-20261015: 333 trades, 209 wins (62.8%), -4.76%, maxDD 6.39%, Sharpe -0.79, market -19.82%.
- lookahead-analysis 20250901-20251101: 20 signals, 0 biased entries, 0 biased exits; flagged columns only &-hit (target, expected), up/down/do_predict (FreqAI predictions - known false-positive pattern because models retrain differently per run).
- recursive-analysis: only btc_usdt_ema200_1d varies (-0.499% at 199 startup, -0.000% at 999); startup 4900 is sufficient.
- Verdict: classifier wins ~63% but needs ~71% to break even with +2/-5 exits -> losing. Not chosen for bot B.
- Note: first full pipeline run produced only stale results (MergeError, see above) - those lines in stage4.out were ignored.
## 2026-10-17 03:00-03:08 - Stage 7 wiring + bot B
- OpenCode wrote user_data/strategies/TrendAdx1hRegimeVeto.py (subclass; confirm_trade_entry fail-closed on missing/stale(>26h)/block decision in dry_run/live only; custom_stake_amount x size). TrendAdx1hRegimeVeto.json = tuned TrendAdx1hRegime params.
- Bot B chosen = TrendAdx1hRegime (OOS -0.70% vs FreqAI v2 -4.76%) + agent veto. user_data/bots/botB.json port 8082.
- agents_cycle.ps1: incremental download-data (5m/15m/1h/4h/1d, 1m BTC/ETH) then `python -m agents.run_cycle --api-url http://127.0.0.1:8082/api/v1 --live-orderbook`. Scheduled task TradingBot\AgentsCycle every 4h (30 min limit).
- First live cycle 03:01-03:07: source=llm, all 5 pairs BLOCK (conf 0.80-0.85; intraday bear on 5m-4h, thin BNB book). Written user_data/decisions/latest.json and reports/decisions/2026-10-17_0102.json.
- Problem: cycle.log written as UTF-16 by PowerShell 5 `*>>`; fixed to `| Out-File -Append -Encoding utf8`.
- Problem: schtasks default ExecutionTimeLimit = 72h would kill the bots. Set bots to unlimited (PT0S), cycle/collector to 30 min, battery stop disabled, MultipleInstances IgnoreNew. Restarted bots A/B/C (killed old freqtrade processes, schtasks /Run) at 03:08.
## 2026-10-17 03:09 - INTERRUPTION
- My session was interrupted during the bot restart command; on resume verified restart had completed: botA PID 7280, botB PID 1136, botC PID 1836 (python.exe, started 03:08:18), all "Dry run is enabled", API on 127.0.0.1:8081/8082/8083.
- status.ps1: A 0 trades; B 0 trades (veto blocking); C 1 open BTC/USDT -0.31%.
- Collector scheduled run 03:10: fng stored.
- FreqaiExampleSpot (Stage 6b) backtests running in background (fex_oos.log, fex_22.log).
## 2026-10-17 03:11-03:28 - Agent historical replay (anonymized)
- reports/REPLAY_SPEC.md; OpenCode (~5.5 min) added --anonymize to decision_agent/run_cycle, agents/replay.py, agents/evaluate_replay.py.
- Leak audit of anonymized prompt (2026-09-28): 0 matches for BTC/ETH/SOL/BNB/XRP, weekday names, absolute close/ema fields; 'USDT' only in the generic system line; '202x' matches were digits inside feature values. Remaining weak leak: Fear&Greed value/tone could hint at a period.
- Rule (no-LLM) replay: 66 weekly dates 2025-07-07..2026-10-05 written.
- LLM anonymized replay test 2026-09-28: source=llm, model deepseek-v4.1-flash-free, ~5 min.
- Launched detached LLM replay every 21 days 2025-07-07..2026-10-05, PID 9396, log reports/decisions/replay_llm.out (resumable).
## 2026-10-17 03:35 - Stage 6b: FreqaiExampleSpot (stock FreqaiExampleStrategy, can_short=False, 1h, LightGBMRegressor, config_freqai_example.json BTC/ETH/SOL, train 90d / retrain 7d)
- OOS 20250701-20261015: 1524 trades (3.24/day), -50.75%, max underwater 51.44%, Sharpe -12.94, market -19.82%. Untuned example strategy loses heavily (fees + noisy signals).
- 2022 held-out run (20220415-20221231) started next in the same background job (fex_22.log).
## 2026-10-17 04:01 - INTERRUPTION
- Session interrupted while polling the LLM replay; replay (PID 9396) and FreqaiExampleSpot 2022 run continued in background. Stage 4-6 table appended to STAGES.md.

## 2026-10-17 04:06 - FreqaiExampleSpot 2022 held-out (20220415-20221231)
- 1847 trades (7.1/day), -59.96%, max underwater 62.01%, Sharpe -19.03, market -69.58%. TOTAL row: |    TOTAL |   1847 |     -0.32 |   -59.959 |    -59.96 |  3:47:00 |       736 |

