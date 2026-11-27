# Deep research report

- Runs analysed: **142**
- Candidates per run: ~124
- Cumulative candidates evaluated: **17,536**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-27 20:01:47+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2304** (min 0.1681, max 0.4476, over 142 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 26.5% | 26.9% | -15.7% | 0.138 | 0.202 | 1553 | 0 |
| `sma_trend_vol_filter` | 20.4% | 19.5% | -9.6% | 0.108 | 0.503 | 4505 | 0 |
| `sma_trend_efficiency` | 18.7% | 19.4% | -13.2% | 0.219 | 0.411 | 2135 | 0 |
| `ema_trend` | 14.6% | 14.9% | -14.6% | 0.105 | 0.155 | 843 | 0 |
| `ema_trend_regime` | 11.9% | 11.5% | -10.5% | 0.050 | 0.130 | 996 | 0 |
| `sma_trend_fast_slow` | 11.1% | 10.9% | -16.0% | 0.112 | 0.187 | 1573 | 0 |
| `sma_trend_slope` | 10.7% | 10.9% | -13.4% | 0.094 | 0.151 | 1580 | 0 |
| `sma_trend_confirm` | 10.6% | 9.1% | -15.5% | 0.086 | 0.143 | 1040 | 0 |
| `donchian_trend_vol_filter` | 3.2% | 3.0% | -2.7% | 0.096 | 0.315 | 289 | 0 |
| `donchian_trend` | 4.3% | 2.8% | -4.0% | 0.302 | 0.429 | 359 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 142 | 142 | 37.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 142 | 142 | 37.0% | 23.2% | 0.181 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 142 | 142 | 36.2% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 142 | 142 | 34.9% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 142 | 142 | 34.7% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 142 | 142 | 33.6% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 142 | 142 | 32.7% | 24.5% | 0.388 | 9.4 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 139 | 139 | 32.6% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 142 | 142 | 31.0% | 23.1% | 0.126 | 9.0 |
| `sma_trend_period100` | 142 | 142 | 30.7% | 17.9% | 0.059 | 8.8 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 98 | 6.7% | -3.5% |
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

- KEEP: `sma_trend_period200` was positive in 142/142 runs (mean holdout 37.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 142/142 runs (mean holdout 37.0%, worst 23.2%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 142/142 runs (mean holdout 36.2%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 142/142 runs (mean holdout 34.9%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 142/142 runs (mean holdout 34.7%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (26.9%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.5%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.9%) - add more parameters to it

