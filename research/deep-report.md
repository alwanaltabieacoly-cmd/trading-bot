# Deep research report

- Runs analysed: **144**
- Candidates per run: ~124
- Cumulative candidates evaluated: **17,784**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-28 11:54:09+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2312** (min 0.1681, max 0.4476, over 144 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 26.6% | 27.0% | -15.6% | 0.138 | 0.202 | 1575 | 0 |
| `sma_trend_vol_filter` | 20.5% | 19.6% | -9.6% | 0.108 | 0.503 | 4565 | 0 |
| `sma_trend_efficiency` | 18.8% | 19.4% | -13.2% | 0.219 | 0.411 | 2167 | 0 |
| `ema_trend` | 14.7% | 15.0% | -14.6% | 0.105 | 0.155 | 855 | 0 |
| `ema_trend_regime` | 12.0% | 11.6% | -10.4% | 0.049 | 0.130 | 1010 | 0 |
| `sma_trend_fast_slow` | 11.1% | 11.0% | -15.9% | 0.112 | 0.187 | 1595 | 0 |
| `sma_trend_slope` | 10.8% | 10.9% | -13.3% | 0.094 | 0.151 | 1604 | 0 |
| `sma_trend_confirm` | 10.7% | 9.7% | -15.5% | 0.086 | 0.143 | 1056 | 0 |
| `donchian_trend_vol_filter` | 3.2% | 3.0% | -2.7% | 0.096 | 0.315 | 293 | 0 |
| `donchian_trend` | 4.4% | 2.8% | -4.0% | 0.302 | 0.429 | 365 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 144 | 144 | 37.2% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 144 | 144 | 37.2% | 23.2% | 0.181 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 144 | 144 | 36.4% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 144 | 144 | 35.0% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 144 | 144 | 34.8% | 25.5% | 0.378 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 144 | 144 | 33.7% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 144 | 144 | 32.8% | 24.5% | 0.388 | 9.4 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 141 | 141 | 32.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 144 | 144 | 31.1% | 23.1% | 0.126 | 9.0 |
| `sma_trend_period100` | 144 | 144 | 30.9% | 17.9% | 0.059 | 8.8 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 100 | 6.7% | -3.4% |
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

- KEEP: `sma_trend_period200` was positive in 144/144 runs (mean holdout 37.2%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 144/144 runs (mean holdout 37.2%, worst 23.2%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 144/144 runs (mean holdout 36.4%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 144/144 runs (mean holdout 35.0%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 144/144 runs (mean holdout 34.8%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (27.0%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.6%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (19.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (15.0%) - add more parameters to it

