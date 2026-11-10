# Deep research report

- Runs analysed: **89**
- Candidates per run: ~124
- Cumulative candidates evaluated: **10,964**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-10 23:27:58+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2141** (min 0.1681, max 0.4476, over 89 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.3% | 22.7% | -16.3% | 0.139 | 0.202 | 970 | 0 |
| `sma_trend_vol_filter` | 17.3% | 17.3% | -10.2% | 0.110 | 0.503 | 2881 | 0 |
| `sma_trend_efficiency` | 15.9% | 15.6% | -13.4% | 0.220 | 0.411 | 1297 | 0 |
| `ema_trend` | 11.7% | 12.8% | -15.1% | 0.105 | 0.155 | 525 | 0 |
| `ema_trend_regime` | 9.5% | 9.5% | -11.1% | 0.050 | 0.130 | 639 | 0 |
| `sma_trend_fast_slow` | 8.6% | 9.4% | -16.3% | 0.113 | 0.187 | 946 | 0 |
| `sma_trend_slope` | 8.1% | 8.3% | -14.0% | 0.094 | 0.151 | 950 | 0 |
| `sma_trend_confirm` | 7.3% | 4.7% | -16.3% | 0.086 | 0.143 | 616 | 0 |
| `donchian_trend` | 3.1% | 1.8% | -4.2% | 0.303 | 0.429 | 200 | 0 |
| `donchian_trend_vol_filter` | 2.1% | 1.4% | -2.9% | 0.100 | 0.315 | 183 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 89 | 89 | 33.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 89 | 89 | 32.4% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 89 | 89 | 31.7% | 23.2% | 0.184 | 8.7 |
| `sma_trend_period175` | 89 | 89 | 30.9% | 25.7% | 0.102 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 89 | 89 | 30.6% | 25.5% | 0.381 | 8.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 89 | 89 | 29.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 86 | 86 | 29.0% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 89 | 89 | 28.6% | 24.5% | 0.397 | 9.7 |
| `sma_trend_period225` | 89 | 89 | 27.4% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 89 | 89 | 26.9% | 22.7% | 0.360 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 89 | 6.7% | -3.7% |
| `sma_trend_slope_period150_slope_bars40` | 56 | 13.0% | -2.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 33 | 10.1% | -1.2% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 33 | 4.8% | -1.8% |
| `sma_trend_slope_period100_slope_bars10` | 26 | 13.5% | -1.4% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 18 | 10.9% | -1.3% |
| `ema_trend_fast50_slow300` | 9 | 8.5% | -2.0% |
| `sma_trend_period400` | 9 | 15.0% | -0.5% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 89/89 runs (mean holdout 33.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 89/89 runs (mean holdout 32.4%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 89/89 runs (mean holdout 31.7%, worst 23.2%, mean DSR 0.184)
- KEEP: `sma_trend_period175` was positive in 89/89 runs (mean holdout 30.9%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 89/89 runs (mean holdout 30.6%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.6%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.8%) - add more parameters to it

