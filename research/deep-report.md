# Deep research report

- Runs analysed: **126**
- Candidates per run: ~124
- Cumulative candidates evaluated: **15,552**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-21 23:23:38+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2254** (min 0.1681, max 0.4476, over 126 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 25.1% | 25.1% | -15.8% | 0.138 | 0.202 | 1377 | 0 |
| `sma_trend_vol_filter` | 19.4% | 18.9% | -9.7% | 0.109 | 0.503 | 4025 | 0 |
| `sma_trend_efficiency` | 17.9% | 18.5% | -13.3% | 0.219 | 0.411 | 1879 | 0 |
| `ema_trend` | 13.7% | 14.3% | -14.7% | 0.105 | 0.155 | 747 | 0 |
| `ema_trend_regime` | 11.2% | 10.7% | -10.6% | 0.050 | 0.130 | 892 | 0 |
| `sma_trend_fast_slow` | 10.3% | 10.3% | -16.0% | 0.113 | 0.187 | 1384 | 0 |
| `sma_trend_slope` | 9.9% | 10.0% | -13.5% | 0.094 | 0.151 | 1388 | 0 |
| `sma_trend_confirm` | 9.6% | 7.9% | -15.7% | 0.086 | 0.143 | 912 | 0 |
| `donchian_trend_vol_filter` | 2.9% | 2.6% | -2.7% | 0.097 | 0.315 | 257 | 0 |
| `donchian_trend` | 4.0% | 2.5% | -4.1% | 0.302 | 0.429 | 311 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 126 | 126 | 35.8% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 126 | 126 | 35.1% | 23.2% | 0.182 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 126 | 126 | 35.0% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 126 | 126 | 33.6% | 25.7% | 0.101 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 126 | 126 | 33.4% | 25.5% | 0.378 | 8.2 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 126 | 126 | 32.4% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 123 | 123 | 31.5% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 126 | 126 | 31.4% | 24.5% | 0.393 | 9.5 |
| `sma_trend_period225` | 126 | 126 | 29.8% | 23.1% | 0.126 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 126 | 126 | 29.3% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 126/126 runs (mean holdout 35.8%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 126/126 runs (mean holdout 35.1%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 126/126 runs (mean holdout 35.0%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 126/126 runs (mean holdout 33.6%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 126/126 runs (mean holdout 33.4%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (25.1%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (18.9%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (18.5%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.3%) - add more parameters to it

