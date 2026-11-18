# Deep research report

- Runs analysed: **114**
- Candidates per run: ~124
- Cumulative candidates evaluated: **14,064**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-18 04:28:25+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2214** (min 0.1681, max 0.4476, over 114 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 24.1% | 23.9% | -15.9% | 0.139 | 0.202 | 1245 | 0 |
| `sma_trend_vol_filter` | 18.6% | 18.0% | -9.9% | 0.109 | 0.503 | 3665 | 0 |
| `sma_trend_efficiency` | 17.2% | 17.7% | -13.3% | 0.219 | 0.411 | 1687 | 0 |
| `ema_trend` | 13.0% | 13.8% | -14.9% | 0.105 | 0.155 | 675 | 0 |
| `ema_trend_regime` | 10.5% | 10.3% | -10.7% | 0.050 | 0.130 | 810 | 0 |
| `sma_trend_fast_slow` | 9.7% | 10.0% | -16.1% | 0.113 | 0.187 | 1240 | 0 |
| `sma_trend_slope` | 9.2% | 9.4% | -13.6% | 0.094 | 0.151 | 1244 | 0 |
| `sma_trend_confirm` | 8.8% | 6.7% | -15.9% | 0.086 | 0.143 | 816 | 0 |
| `donchian_trend_vol_filter` | 2.7% | 2.3% | -2.8% | 0.098 | 0.315 | 233 | 0 |
| `donchian_trend` | 3.8% | 2.2% | -4.1% | 0.303 | 0.429 | 275 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 114 | 114 | 34.8% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 114 | 114 | 34.0% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 114 | 114 | 33.8% | 23.2% | 0.183 | 8.9 |
| `sma_trend_period175` | 114 | 114 | 32.6% | 25.7% | 0.101 | 8.9 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 114 | 114 | 32.4% | 25.5% | 0.379 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 114 | 114 | 31.4% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 111 | 111 | 30.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 114 | 114 | 30.4% | 24.5% | 0.396 | 9.5 |
| `sma_trend_period225` | 114 | 114 | 28.9% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 114 | 114 | 28.4% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 114/114 runs (mean holdout 34.8%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 114/114 runs (mean holdout 34.0%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 114/114 runs (mean holdout 33.8%, worst 23.2%, mean DSR 0.183)
- KEEP: `sma_trend_period175` was positive in 114/114 runs (mean holdout 32.6%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 114/114 runs (mean holdout 32.4%, worst 25.5%, mean DSR 0.379)
- FAMILY `sma_trend` has the best median holdout CAGR (23.9%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (18.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (17.7%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.8%) - add more parameters to it

