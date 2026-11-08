# Deep research report

- Runs analysed: **79**
- Candidates per run: ~124
- Cumulative candidates evaluated: **9,724**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-08 00:42:31+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2165** (min 0.1681, max 0.4476, over 79 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.4% | 22.7% | -16.3% | 0.139 | 0.202 | 864 | 0 |
| `sma_trend_vol_filter` | 17.3% | 17.3% | -10.3% | 0.109 | 0.503 | 2551 | 0 |
| `sma_trend_efficiency` | 15.6% | 15.4% | -13.5% | 0.220 | 0.411 | 1147 | 0 |
| `ema_trend` | 11.8% | 13.1% | -15.1% | 0.105 | 0.155 | 469 | 0 |
| `ema_trend_regime` | 9.6% | 9.7% | -11.1% | 0.050 | 0.130 | 557 | 0 |
| `sma_trend_fast_slow` | 8.6% | 9.5% | -16.3% | 0.113 | 0.187 | 840 | 0 |
| `sma_trend_slope` | 8.1% | 8.4% | -14.0% | 0.094 | 0.151 | 844 | 0 |
| `sma_trend_confirm` | 7.3% | 4.7% | -16.4% | 0.086 | 0.143 | 544 | 0 |
| `donchian_trend` | 2.9% | 1.8% | -4.2% | 0.304 | 0.429 | 170 | 0 |
| `donchian_trend_vol_filter` | 1.9% | 1.3% | -2.9% | 0.100 | 0.315 | 159 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 79 | 79 | 33.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 79 | 79 | 32.3% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 79 | 79 | 32.1% | 23.2% | 0.182 | 8.7 |
| `sma_trend_period175` | 79 | 79 | 30.7% | 25.7% | 0.102 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 79 | 79 | 30.5% | 25.5% | 0.381 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 79 | 79 | 29.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 76 | 76 | 28.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 79 | 79 | 28.6% | 24.5% | 0.394 | 9.8 |
| `sma_trend_period225` | 79 | 79 | 27.5% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 79 | 79 | 27.0% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 79 | 6.7% | -3.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 46 | 13.0% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 29 | 10.0% | -1.0% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 29 | 4.8% | -1.9% |
| `sma_trend_slope_period100_slope_bars10` | 22 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 14 | 10.8% | -1.1% |
| `ema_trend_fast50_slow300` | 5 | 8.4% | -2.0% |
| `sma_trend_period400` | 5 | 14.8% | -0.6% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 79/79 runs (mean holdout 33.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 79/79 runs (mean holdout 32.3%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 79/79 runs (mean holdout 32.1%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_period175` was positive in 79/79 runs (mean holdout 30.7%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 79/79 runs (mean holdout 30.5%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.1%) - add more parameters to it

