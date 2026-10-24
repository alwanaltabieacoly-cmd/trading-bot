# Deep research report

- Runs analysed: **22**
- Candidates per run: ~124
- Cumulative candidates evaluated: **2,656**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-24 12:45:06+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.231** (min 0.1793, max 0.4476, over 22 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.1% | 18.1% | -16.5% | 0.141 | 0.202 | 242 | 0 |
| `sma_trend_vol_filter` | 14.4% | 14.2% | -10.5% | 0.110 | 0.503 | 726 | 0 |
| `sma_trend_efficiency` | 13.6% | 12.2% | -13.7% | 0.220 | 0.411 | 285 | 0 |
| `ema_trend` | 10.1% | 11.6% | -15.2% | 0.107 | 0.155 | 132 | 0 |
| `sma_trend_fast_slow` | 5.8% | 8.7% | -16.5% | 0.114 | 0.187 | 220 | 0 |
| `ema_trend_regime` | 7.8% | 8.2% | -11.2% | 0.050 | 0.128 | 166 | 0 |
| `sma_trend_slope` | 6.4% | 7.5% | -14.2% | 0.094 | 0.151 | 190 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.306 | 0.429 | 44 | 0 |
| `sma_trend_confirm` | 5.2% | 1.6% | -16.6% | 0.086 | 0.143 | 107 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 44 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 22 | 22 | 29.2% | 28.1% | 0.131 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 22 | 22 | 28.4% | 27.4% | 0.348 | 8.0 |
| `sma_trend_period50` | 22 | 22 | 27.9% | 25.9% | 0.186 | 8.0 |
| `sma_trend_period175` | 22 | 22 | 26.7% | 25.7% | 0.103 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 19 | 19 | 26.6% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 22 | 22 | 26.4% | 25.5% | 0.384 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 22 | 22 | 26.0% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 22 | 22 | 25.3% | 24.5% | 0.401 | 10.0 |
| `sma_trend_period225` | 22 | 22 | 24.1% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 22 | 22 | 23.7% | 22.7% | 0.363 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 22 | 7.1% | -6.4% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 22 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 19 | 10.1% | -0.8% |
| `sma_trend_confirm_slow_period150_fast_period50` | 19 | 12.7% | -0.6% |
| `sma_trend_slope_period100_slope_bars10` | 19 | 13.6% | -1.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 19 | 6.7% | -2.2% |
| `sma_trend_slope_period150_slope_bars40` | 19 | 13.2% | -3.3% |
| `sma_trend_confirm_slow_period100_fast_period50` | 7 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 22/22 runs (mean holdout 29.2%, worst 28.1%, mean DSR 0.131)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 22/22 runs (mean holdout 28.4%, worst 27.4%, mean DSR 0.348)
- KEEP: `sma_trend_period50` was positive in 22/22 runs (mean holdout 27.9%, worst 25.9%, mean DSR 0.186)
- KEEP: `sma_trend_period175` was positive in 22/22 runs (mean holdout 26.7%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 19/19 runs (mean holdout 26.6%, worst 26.2%, mean DSR 0.137)
- FAMILY `sma_trend` has the best median holdout CAGR (18.1%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.2%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.6%) - add more parameters to it

