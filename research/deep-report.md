# Deep research report

- Runs analysed: **26**
- Candidates per run: ~124
- Cumulative candidates evaluated: **3,152**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-25 11:37:57+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2276** (min 0.1793, max 0.4476, over 26 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.4% | 18.8% | -16.5% | 0.140 | 0.202 | 286 | 0 |
| `sma_trend_vol_filter` | 14.6% | 14.4% | -10.4% | 0.110 | 0.503 | 858 | 0 |
| `sma_trend_efficiency` | 13.8% | 12.3% | -13.7% | 0.220 | 0.411 | 345 | 0 |
| `ema_trend` | 10.3% | 11.6% | -15.2% | 0.106 | 0.155 | 156 | 0 |
| `sma_trend_fast_slow` | 6.1% | 8.8% | -16.5% | 0.114 | 0.187 | 262 | 0 |
| `ema_trend_regime` | 8.0% | 8.4% | -11.2% | 0.050 | 0.128 | 196 | 0 |
| `sma_trend_slope` | 6.5% | 7.5% | -14.2% | 0.094 | 0.151 | 232 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.305 | 0.429 | 52 | 0 |
| `sma_trend_confirm` | 5.3% | 1.6% | -16.6% | 0.086 | 0.143 | 133 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 52 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 26 | 26 | 29.4% | 28.1% | 0.131 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 26 | 26 | 28.7% | 27.4% | 0.348 | 8.0 |
| `sma_trend_period50` | 26 | 26 | 28.3% | 25.9% | 0.185 | 8.0 |
| `sma_trend_period175` | 26 | 26 | 26.9% | 25.7% | 0.103 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 23 | 23 | 26.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 26 | 26 | 26.6% | 25.5% | 0.383 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 26 | 26 | 26.2% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 26 | 26 | 25.6% | 24.5% | 0.400 | 10.0 |
| `sma_trend_period225` | 26 | 26 | 24.3% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 26 | 26 | 23.9% | 22.7% | 0.363 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 26 | 7.0% | -6.1% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 23 | 6.7% | -2.1% |
| `sma_trend_slope_period150_slope_bars40` | 23 | 13.2% | -3.2% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 26/26 runs (mean holdout 29.4%, worst 28.1%, mean DSR 0.131)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 26/26 runs (mean holdout 28.7%, worst 27.4%, mean DSR 0.348)
- KEEP: `sma_trend_period50` was positive in 26/26 runs (mean holdout 28.3%, worst 25.9%, mean DSR 0.185)
- KEEP: `sma_trend_period175` was positive in 26/26 runs (mean holdout 26.9%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 23/23 runs (mean holdout 26.7%, worst 26.2%, mean DSR 0.137)
- FAMILY `sma_trend` has the best median holdout CAGR (18.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.4%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.3%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.6%) - add more parameters to it

