# Deep research report

- Runs analysed: **109**
- Candidates per run: ~124
- Cumulative candidates evaluated: **13,444**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-16 11:28:01+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2198** (min 0.1681, max 0.4476, over 109 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 23.7% | 23.7% | -16.0% | 0.139 | 0.202 | 1190 | 0 |
| `sma_trend_vol_filter` | 18.3% | 17.9% | -9.9% | 0.109 | 0.503 | 3515 | 0 |
| `sma_trend_efficiency` | 17.0% | 17.4% | -13.3% | 0.219 | 0.411 | 1607 | 0 |
| `ema_trend` | 12.6% | 13.7% | -14.9% | 0.105 | 0.155 | 645 | 0 |
| `ema_trend_regime` | 10.3% | 10.1% | -10.8% | 0.050 | 0.130 | 780 | 0 |
| `sma_trend_fast_slow` | 9.4% | 9.9% | -16.1% | 0.113 | 0.187 | 1180 | 0 |
| `sma_trend_slope` | 8.9% | 9.1% | -13.7% | 0.094 | 0.151 | 1184 | 0 |
| `sma_trend_confirm` | 8.4% | 5.9% | -16.0% | 0.086 | 0.143 | 776 | 0 |
| `donchian_trend_vol_filter` | 2.6% | 2.2% | -2.8% | 0.098 | 0.315 | 223 | 0 |
| `donchian_trend` | 3.7% | 2.1% | -4.1% | 0.303 | 0.429 | 260 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 109 | 109 | 34.4% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 109 | 109 | 33.6% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 109 | 109 | 33.3% | 23.2% | 0.184 | 8.9 |
| `sma_trend_period175` | 109 | 109 | 32.2% | 25.7% | 0.101 | 8.9 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 109 | 109 | 32.0% | 25.5% | 0.379 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 109 | 109 | 31.1% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 106 | 106 | 30.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 109 | 109 | 29.9% | 24.5% | 0.397 | 9.6 |
| `sma_trend_period225` | 109 | 109 | 28.6% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 109 | 109 | 28.1% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 109/109 runs (mean holdout 34.4%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 109/109 runs (mean holdout 33.6%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 109/109 runs (mean holdout 33.3%, worst 23.2%, mean DSR 0.184)
- KEEP: `sma_trend_period175` was positive in 109/109 runs (mean holdout 32.2%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 109/109 runs (mean holdout 32.0%, worst 25.5%, mean DSR 0.379)
- FAMILY `sma_trend` has the best median holdout CAGR (23.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.9%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.7%) - add more parameters to it

