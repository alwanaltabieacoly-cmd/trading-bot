# Deep research report

- Runs analysed: **12**
- Candidates per run: ~124
- Cumulative candidates evaluated: **1,416**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-22 04:55:12+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2551** (min 0.1793, max 0.4476, over 12 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.6% | 17.4% | -16.5% | 0.143 | 0.202 | 132 | 0 |
| `sma_trend_vol_filter` | 14.0% | 13.5% | -10.5% | 0.111 | 0.503 | 396 | 0 |
| `sma_trend_efficiency` | 13.4% | 12.0% | -13.7% | 0.220 | 0.411 | 135 | 0 |
| `ema_trend` | 9.8% | 11.5% | -15.2% | 0.108 | 0.155 | 72 | 0 |
| `ema_trend_regime` | 7.5% | 8.1% | -11.2% | 0.051 | 0.128 | 89 | 0 |
| `sma_trend_fast_slow` | 5.3% | 8.1% | -16.5% | 0.116 | 0.187 | 120 | 0 |
| `sma_trend_slope` | 6.0% | 6.9% | -14.2% | 0.094 | 0.151 | 90 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.309 | 0.429 | 24 | 0 |
| `sma_trend_confirm` | 4.9% | 1.5% | -16.6% | 0.086 | 0.143 | 50 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.102 | 0.311 | 24 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 12 | 12 | 28.6% | 28.1% | 0.133 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 12 | 12 | 27.9% | 27.4% | 0.351 | 8.0 |
| `sma_trend_period50` | 12 | 12 | 26.8% | 25.9% | 0.188 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 9 | 9 | 26.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period175` | 12 | 12 | 26.2% | 25.7% | 0.105 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 12 | 12 | 26.0% | 25.5% | 0.387 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 12 | 12 | 25.5% | 25.0% | 0.090 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 12 | 12 | 24.9% | 24.5% | 0.404 | 10.0 |
| `sma_trend_period225` | 12 | 12 | 23.6% | 23.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 12 | 12 | 23.2% | 22.7% | 0.366 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 12 | 7.1% | -6.8% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 12 | 4.9% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 9 | 10.1% | -0.8% |
| `sma_trend_confirm_slow_period150_fast_period50` | 9 | 12.7% | -0.8% |
| `sma_trend_slope_period100_slope_bars10` | 9 | 13.6% | -1.8% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 9 | 6.8% | -2.3% |
| `sma_trend_slope_period150_slope_bars40` | 9 | 13.2% | -3.5% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 12/12 runs (mean holdout 28.6%, worst 28.1%, mean DSR 0.133)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 12/12 runs (mean holdout 27.9%, worst 27.4%, mean DSR 0.351)
- KEEP: `sma_trend_period50` was positive in 12/12 runs (mean holdout 26.8%, worst 25.9%, mean DSR 0.188)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 9/9 runs (mean holdout 26.4%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period175` was positive in 12/12 runs (mean holdout 26.2%, worst 25.7%, mean DSR 0.105)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.5%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

