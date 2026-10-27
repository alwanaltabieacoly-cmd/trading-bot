# Deep research report

- Runs analysed: **33**
- Candidates per run: ~124
- Cumulative candidates evaluated: **4,020**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-27 06:21:33+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2253** (min 0.1793, max 0.4476, over 33 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 20.4% | 20.5% | -16.4% | 0.140 | 0.202 | 363 | 0 |
| `sma_trend_vol_filter` | 15.4% | 15.2% | -10.4% | 0.110 | 0.503 | 1087 | 0 |
| `sma_trend_efficiency` | 14.2% | 12.6% | -13.7% | 0.220 | 0.411 | 450 | 0 |
| `ema_trend` | 11.0% | 11.8% | -15.2% | 0.106 | 0.155 | 198 | 0 |
| `sma_trend_fast_slow` | 6.9% | 8.9% | -16.4% | 0.114 | 0.187 | 339 | 0 |
| `ema_trend_regime` | 8.7% | 8.7% | -11.2% | 0.050 | 0.128 | 247 | 0 |
| `sma_trend_slope` | 7.1% | 7.7% | -14.1% | 0.094 | 0.151 | 311 | 0 |
| `sma_trend_confirm` | 6.1% | 2.7% | -16.5% | 0.086 | 0.143 | 189 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.304 | 0.429 | 66 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 66 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 33 | 33 | 30.4% | 28.1% | 0.130 | 9.0 |
| `sma_trend_period50` | 33 | 33 | 29.8% | 25.9% | 0.184 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 33 | 33 | 29.7% | 27.4% | 0.347 | 8.0 |
| `sma_trend_period175` | 33 | 33 | 27.8% | 25.7% | 0.102 | 8.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 33 | 33 | 27.6% | 25.5% | 0.382 | 7.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 33 | 33 | 27.3% | 25.0% | 0.088 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 30 | 30 | 27.1% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 33 | 33 | 26.4% | 24.5% | 0.398 | 10.0 |
| `sma_trend_period225` | 33 | 33 | 25.3% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 33 | 33 | 24.9% | 22.7% | 0.362 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 33 | 7.0% | -5.4% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 30 | 6.7% | -1.8% |
| `sma_trend_slope_period150_slope_bars40` | 28 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 33/33 runs (mean holdout 30.4%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_period50` was positive in 33/33 runs (mean holdout 29.8%, worst 25.9%, mean DSR 0.184)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 33/33 runs (mean holdout 29.7%, worst 27.4%, mean DSR 0.347)
- KEEP: `sma_trend_period175` was positive in 33/33 runs (mean holdout 27.8%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 33/33 runs (mean holdout 27.6%, worst 25.5%, mean DSR 0.382)
- FAMILY `sma_trend` has the best median holdout CAGR (20.5%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (15.2%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.6%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.8%) - add more parameters to it

