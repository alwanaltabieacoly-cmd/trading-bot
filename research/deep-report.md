# Deep research report

- Runs analysed: **134**
- Candidates per run: ~124
- Cumulative candidates evaluated: **16,544**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-24 21:17:11+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.228** (min 0.1681, max 0.4476, over 134 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 25.8% | 26.2% | -15.7% | 0.138 | 0.202 | 1465 | 0 |
| `sma_trend_vol_filter` | 19.9% | 19.2% | -9.7% | 0.108 | 0.503 | 4265 | 0 |
| `sma_trend_efficiency` | 18.3% | 19.0% | -13.2% | 0.219 | 0.411 | 2007 | 0 |
| `ema_trend` | 14.2% | 14.5% | -14.7% | 0.105 | 0.155 | 795 | 0 |
| `ema_trend_regime` | 11.6% | 11.1% | -10.5% | 0.050 | 0.130 | 948 | 0 |
| `sma_trend_fast_slow` | 10.7% | 10.7% | -16.0% | 0.112 | 0.187 | 1480 | 0 |
| `sma_trend_slope` | 10.3% | 10.4% | -13.4% | 0.094 | 0.151 | 1484 | 0 |
| `sma_trend_confirm` | 10.1% | 8.4% | -15.6% | 0.086 | 0.143 | 976 | 0 |
| `donchian_trend_vol_filter` | 3.0% | 2.7% | -2.7% | 0.097 | 0.315 | 273 | 0 |
| `donchian_trend` | 4.2% | 2.6% | -4.1% | 0.302 | 0.429 | 335 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 134 | 134 | 36.4% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 134 | 134 | 36.1% | 23.2% | 0.182 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 134 | 134 | 35.6% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 134 | 134 | 34.3% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 134 | 134 | 34.0% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 134 | 134 | 33.0% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 131 | 131 | 32.0% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 134 | 134 | 32.0% | 24.5% | 0.392 | 9.5 |
| `sma_trend_period225` | 134 | 134 | 30.4% | 23.1% | 0.126 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 134 | 134 | 29.9% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 134/134 runs (mean holdout 36.4%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 134/134 runs (mean holdout 36.1%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 134/134 runs (mean holdout 35.6%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 134/134 runs (mean holdout 34.3%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 134/134 runs (mean holdout 34.0%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (26.2%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.2%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.5%) - add more parameters to it

