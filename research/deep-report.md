# Deep research report

- Runs analysed: **137**
- Candidates per run: ~124
- Cumulative candidates evaluated: **16,916**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-25 23:41:47+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2289** (min 0.1681, max 0.4476, over 137 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 26.1% | 26.6% | -15.7% | 0.138 | 0.202 | 1498 | 0 |
| `sma_trend_vol_filter` | 20.1% | 19.2% | -9.7% | 0.108 | 0.503 | 4355 | 0 |
| `sma_trend_efficiency` | 18.4% | 19.2% | -13.2% | 0.219 | 0.411 | 2055 | 0 |
| `ema_trend` | 14.4% | 14.6% | -14.7% | 0.105 | 0.155 | 813 | 0 |
| `ema_trend_regime` | 11.7% | 11.3% | -10.5% | 0.050 | 0.130 | 966 | 0 |
| `sma_trend_fast_slow` | 10.9% | 10.8% | -16.0% | 0.112 | 0.187 | 1516 | 0 |
| `sma_trend_slope` | 10.5% | 10.4% | -13.4% | 0.094 | 0.151 | 1520 | 0 |
| `sma_trend_confirm` | 10.3% | 8.6% | -15.6% | 0.086 | 0.143 | 1000 | 0 |
| `donchian_trend_vol_filter` | 3.1% | 2.8% | -2.7% | 0.097 | 0.315 | 279 | 0 |
| `donchian_trend` | 4.2% | 2.7% | -4.0% | 0.302 | 0.429 | 344 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 137 | 137 | 36.7% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 137 | 137 | 36.5% | 23.2% | 0.181 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 137 | 137 | 35.9% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 137 | 137 | 34.5% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 137 | 137 | 34.3% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 137 | 137 | 33.2% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 137 | 137 | 32.3% | 24.5% | 0.391 | 9.5 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 134 | 134 | 32.2% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 137 | 137 | 30.6% | 23.1% | 0.126 | 9.0 |
| `sma_trend_period100` | 137 | 137 | 30.1% | 17.9% | 0.060 | 8.7 |

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

- KEEP: `sma_trend_period200` was positive in 137/137 runs (mean holdout 36.7%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 137/137 runs (mean holdout 36.5%, worst 23.2%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 137/137 runs (mean holdout 35.9%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 137/137 runs (mean holdout 34.5%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 137/137 runs (mean holdout 34.3%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (26.6%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.2%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.6%) - add more parameters to it

