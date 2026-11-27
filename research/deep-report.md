# Deep research report

- Runs analysed: **140**
- Candidates per run: ~124
- Cumulative candidates evaluated: **17,288**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-27 02:15:47+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2297** (min 0.1681, max 0.4476, over 140 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 26.4% | 26.8% | -15.7% | 0.138 | 0.202 | 1531 | 0 |
| `sma_trend_efficiency` | 18.6% | 19.3% | -13.2% | 0.219 | 0.411 | 2103 | 0 |
| `sma_trend_vol_filter` | 20.3% | 19.3% | -9.6% | 0.108 | 0.503 | 4445 | 0 |
| `ema_trend` | 14.5% | 14.8% | -14.6% | 0.105 | 0.155 | 831 | 0 |
| `ema_trend_regime` | 11.9% | 11.4% | -10.5% | 0.050 | 0.130 | 984 | 0 |
| `sma_trend_fast_slow` | 11.0% | 10.9% | -16.0% | 0.112 | 0.187 | 1551 | 0 |
| `sma_trend_slope` | 10.6% | 10.8% | -13.4% | 0.094 | 0.151 | 1556 | 0 |
| `sma_trend_confirm` | 10.5% | 8.7% | -15.5% | 0.086 | 0.143 | 1024 | 0 |
| `donchian_trend_vol_filter` | 3.1% | 2.9% | -2.7% | 0.097 | 0.315 | 285 | 0 |
| `donchian_trend` | 4.3% | 2.8% | -4.0% | 0.302 | 0.429 | 353 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 140 | 140 | 36.9% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 140 | 140 | 36.8% | 23.2% | 0.181 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 140 | 140 | 36.1% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 140 | 140 | 34.8% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 140 | 140 | 34.5% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 140 | 140 | 33.5% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 140 | 140 | 32.6% | 24.5% | 0.389 | 9.4 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 137 | 137 | 32.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 140 | 140 | 30.8% | 23.1% | 0.126 | 9.0 |
| `sma_trend_period100` | 140 | 140 | 30.5% | 17.9% | 0.059 | 8.8 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 96 | 6.7% | -3.5% |
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

- KEEP: `sma_trend_period200` was positive in 140/140 runs (mean holdout 36.9%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 140/140 runs (mean holdout 36.8%, worst 23.2%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 140/140 runs (mean holdout 36.1%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 140/140 runs (mean holdout 34.8%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 140/140 runs (mean holdout 34.5%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (26.8%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.3%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.3%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.8%) - add more parameters to it

