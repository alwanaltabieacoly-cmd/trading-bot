# Deep research report

- Runs analysed: **138**
- Candidates per run: ~124
- Cumulative candidates evaluated: **17,040**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-26 08:26:49+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2291** (min 0.1681, max 0.4476, over 138 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 26.2% | 26.6% | -15.7% | 0.138 | 0.202 | 1509 | 0 |
| `sma_trend_vol_filter` | 20.2% | 19.3% | -9.6% | 0.108 | 0.503 | 4385 | 0 |
| `sma_trend_efficiency` | 18.5% | 19.2% | -13.2% | 0.219 | 0.411 | 2071 | 0 |
| `ema_trend` | 14.4% | 14.7% | -14.7% | 0.105 | 0.155 | 819 | 0 |
| `ema_trend_regime` | 11.8% | 11.3% | -10.5% | 0.050 | 0.130 | 972 | 0 |
| `sma_trend_fast_slow` | 10.9% | 10.9% | -16.0% | 0.112 | 0.187 | 1528 | 0 |
| `sma_trend_slope` | 10.5% | 10.5% | -13.4% | 0.094 | 0.151 | 1532 | 0 |
| `sma_trend_confirm` | 10.3% | 8.6% | -15.5% | 0.086 | 0.143 | 1008 | 0 |
| `donchian_trend_vol_filter` | 3.1% | 2.8% | -2.7% | 0.097 | 0.315 | 281 | 0 |
| `donchian_trend` | 4.3% | 2.7% | -4.0% | 0.302 | 0.429 | 347 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 138 | 138 | 36.8% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 138 | 138 | 36.6% | 23.2% | 0.181 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 138 | 138 | 36.0% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 138 | 138 | 34.6% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 138 | 138 | 34.4% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 138 | 138 | 33.3% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 138 | 138 | 32.4% | 24.5% | 0.390 | 9.4 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 135 | 135 | 32.3% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 138 | 138 | 30.7% | 23.1% | 0.126 | 9.0 |
| `sma_trend_period100` | 138 | 138 | 30.3% | 17.9% | 0.059 | 8.8 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 95 | 6.7% | -3.6% |
| `sma_trend_slope_period150_slope_bars40` | 62 | 12.9% | -2.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 33 | 10.1% | -1.2% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 33 | 4.8% | -1.8% |
| `sma_trend_slope_period100_slope_bars10` | 26 | 13.5% | -1.4% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 18 | 10.9% | -1.3% |
| `ema_trend_fast50_slow300` | 9 | 8.5% | -2.0% |
| `sma_trend_period400` | 9 | 15.0% | -0.5% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 138/138 runs (mean holdout 36.8%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 138/138 runs (mean holdout 36.6%, worst 23.2%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 138/138 runs (mean holdout 36.0%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 138/138 runs (mean holdout 34.6%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 138/138 runs (mean holdout 34.4%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (26.6%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.7%) - add more parameters to it

