# Deep research report

- Runs analysed: **27**
- Candidates per run: ~124
- Cumulative candidates evaluated: **3,276**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-25 16:28:10+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2275** (min 0.1793, max 0.4476, over 27 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.5% | 18.8% | -16.4% | 0.140 | 0.202 | 297 | 0 |
| `sma_trend_vol_filter` | 14.7% | 14.5% | -10.4% | 0.110 | 0.503 | 891 | 0 |
| `sma_trend_efficiency` | 13.8% | 12.3% | -13.7% | 0.220 | 0.411 | 360 | 0 |
| `ema_trend` | 10.3% | 11.6% | -15.2% | 0.106 | 0.155 | 162 | 0 |
| `sma_trend_fast_slow` | 6.2% | 8.8% | -16.5% | 0.114 | 0.187 | 273 | 0 |
| `ema_trend_regime` | 8.0% | 8.4% | -11.2% | 0.050 | 0.128 | 204 | 0 |
| `sma_trend_slope` | 6.5% | 7.5% | -14.2% | 0.094 | 0.151 | 243 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.305 | 0.429 | 54 | 0 |
| `sma_trend_confirm` | 5.4% | 1.6% | -16.6% | 0.086 | 0.143 | 141 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 54 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 27 | 27 | 29.5% | 28.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 27 | 27 | 28.8% | 27.4% | 0.347 | 8.0 |
| `sma_trend_period50` | 27 | 27 | 28.5% | 25.9% | 0.185 | 8.0 |
| `sma_trend_period175` | 27 | 27 | 27.0% | 25.7% | 0.103 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 24 | 24 | 26.8% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 27 | 27 | 26.7% | 25.5% | 0.383 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 27 | 27 | 26.3% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 27 | 27 | 25.7% | 24.5% | 0.400 | 10.0 |
| `sma_trend_period225` | 27 | 27 | 24.4% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 27 | 27 | 24.0% | 22.7% | 0.363 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 27 | 7.0% | -6.0% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 24 | 6.7% | -2.1% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_slope_period150_slope_bars40` | 24 | 13.2% | -3.2% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 27/27 runs (mean holdout 29.5%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 27/27 runs (mean holdout 28.8%, worst 27.4%, mean DSR 0.347)
- KEEP: `sma_trend_period50` was positive in 27/27 runs (mean holdout 28.5%, worst 25.9%, mean DSR 0.185)
- KEEP: `sma_trend_period175` was positive in 27/27 runs (mean holdout 27.0%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 24/24 runs (mean holdout 26.8%, worst 26.2%, mean DSR 0.137)
- FAMILY `sma_trend` has the best median holdout CAGR (18.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.5%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.3%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.6%) - add more parameters to it

