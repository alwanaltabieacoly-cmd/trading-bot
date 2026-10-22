# Deep research report

- Runs analysed: **11**
- Candidates per run: ~124
- Cumulative candidates evaluated: **1,292**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-22 00:04:26+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2597** (min 0.1793, max 0.4476, over 11 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.4% | 17.4% | -16.5% | 0.143 | 0.202 | 121 | 0 |
| `sma_trend_vol_filter` | 13.9% | 13.4% | -10.5% | 0.112 | 0.503 | 363 | 0 |
| `sma_trend_efficiency` | 13.3% | 12.0% | -13.7% | 0.220 | 0.411 | 120 | 0 |
| `ema_trend` | 9.7% | 11.5% | -15.2% | 0.108 | 0.155 | 66 | 0 |
| `ema_trend_regime` | 7.4% | 8.1% | -11.2% | 0.051 | 0.128 | 81 | 0 |
| `sma_trend_fast_slow` | 5.2% | 8.1% | -16.5% | 0.116 | 0.187 | 110 | 0 |
| `sma_trend_slope` | 5.9% | 6.8% | -14.2% | 0.094 | 0.151 | 80 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.309 | 0.429 | 22 | 0 |
| `sma_trend_confirm` | 4.7% | 1.5% | -16.6% | 0.086 | 0.143 | 44 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.102 | 0.311 | 22 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 11 | 11 | 28.5% | 28.1% | 0.133 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 11 | 11 | 27.8% | 27.4% | 0.352 | 8.0 |
| `sma_trend_period50` | 11 | 11 | 26.6% | 25.9% | 0.188 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 8 | 8 | 26.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period175` | 11 | 11 | 26.1% | 25.7% | 0.105 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 11 | 11 | 25.8% | 25.5% | 0.387 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 11 | 11 | 25.4% | 25.0% | 0.090 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 11 | 11 | 24.8% | 24.5% | 0.405 | 10.0 |
| `sma_trend_period225` | 11 | 11 | 23.5% | 23.1% | 0.131 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 11 | 11 | 23.1% | 22.7% | 0.367 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 11 | 7.1% | -6.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 11 | 4.9% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 8 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 8 | 12.7% | -0.9% |
| `sma_trend_slope_period100_slope_bars10` | 8 | 13.6% | -1.8% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 8 | 6.8% | -2.3% |
| `sma_trend_slope_period150_slope_bars40` | 8 | 13.2% | -3.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 11/11 runs (mean holdout 28.5%, worst 28.1%, mean DSR 0.133)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 11/11 runs (mean holdout 27.8%, worst 27.4%, mean DSR 0.352)
- KEEP: `sma_trend_period50` was positive in 11/11 runs (mean holdout 26.6%, worst 25.9%, mean DSR 0.188)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 8/8 runs (mean holdout 26.4%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period175` was positive in 11/11 runs (mean holdout 26.1%, worst 25.7%, mean DSR 0.105)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.4%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

