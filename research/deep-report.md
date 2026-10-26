# Deep research report

- Runs analysed: **29**
- Candidates per run: ~124
- Cumulative candidates evaluated: **3,524**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-26 06:21:49+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2269** (min 0.1793, max 0.4476, over 29 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.7% | 19.7% | -16.4% | 0.140 | 0.202 | 319 | 0 |
| `sma_trend_vol_filter` | 14.9% | 14.7% | -10.4% | 0.110 | 0.503 | 957 | 0 |
| `sma_trend_efficiency` | 13.9% | 12.4% | -13.7% | 0.220 | 0.411 | 390 | 0 |
| `ema_trend` | 10.5% | 11.7% | -15.2% | 0.106 | 0.155 | 174 | 0 |
| `sma_trend_fast_slow` | 6.4% | 8.9% | -16.5% | 0.114 | 0.187 | 295 | 0 |
| `ema_trend_regime` | 8.2% | 8.6% | -11.2% | 0.050 | 0.128 | 219 | 0 |
| `sma_trend_slope` | 6.7% | 7.6% | -14.2% | 0.094 | 0.151 | 265 | 0 |
| `sma_trend_confirm` | 5.6% | 2.2% | -16.6% | 0.086 | 0.143 | 157 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.305 | 0.429 | 58 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 58 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 29 | 29 | 29.7% | 28.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 29 | 29 | 29.0% | 27.4% | 0.347 | 8.0 |
| `sma_trend_period50` | 29 | 29 | 28.9% | 25.9% | 0.185 | 8.0 |
| `sma_trend_period175` | 29 | 29 | 27.2% | 25.7% | 0.103 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 29 | 29 | 26.9% | 25.5% | 0.383 | 7.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 26 | 26 | 26.9% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 29 | 29 | 26.6% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 29 | 29 | 25.9% | 24.5% | 0.400 | 10.0 |
| `sma_trend_period225` | 29 | 29 | 24.7% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 29 | 29 | 24.2% | 22.7% | 0.362 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 29 | 7.0% | -5.8% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 26 | 6.7% | -2.0% |
| `sma_trend_slope_period150_slope_bars40` | 26 | 13.2% | -3.0% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 29/29 runs (mean holdout 29.7%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 29/29 runs (mean holdout 29.0%, worst 27.4%, mean DSR 0.347)
- KEEP: `sma_trend_period50` was positive in 29/29 runs (mean holdout 28.9%, worst 25.9%, mean DSR 0.185)
- KEEP: `sma_trend_period175` was positive in 29/29 runs (mean holdout 27.2%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 29/29 runs (mean holdout 26.9%, worst 25.5%, mean DSR 0.383)
- FAMILY `sma_trend` has the best median holdout CAGR (19.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.7%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.7%) - add more parameters to it

