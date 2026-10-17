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