# Deep research report

- Runs analysed: **115**
- Candidates per run: ~124
- Cumulative candidates evaluated: **14,188**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-18 14:04:46+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2218** (min 0.1681, max 0.4476, over 115 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 24.2% | 24.0% | -15.9% | 0.139 | 0.202 | 1256 | 0 |
| `sma_trend_vol_filter` | 18.7% | 18.1% | -9.9% | 0.109 | 0.503 | 3695 | 0 |
| `sma_trend_efficiency` | 17.3% | 17.7% | -13.3% | 0.219 | 0.411 | 1703 | 0 |
| `ema_trend` | 13.0% | 13.9% | -14.8% | 0.105 | 0.155 | 681 | 0 |
| `ema_trend_regime` | 10.6% | 10.4% | -10.7% | 0.050 | 0.130 | 816 | 0 |
| `sma_trend_fast_slow` | 9.7% | 10.0% | -16.1% | 0.113 | 0.187 | 1252 | 0 |
| `sma_trend_slope` | 9.3% | 9.4% | -13.6% | 0.094 | 0.151 | 1256 | 0 |
| `sma_trend_confirm` | 8.8% | 6.8% | -15.9% | 0.086 | 0.143 | 824 | 0 |
| `donchian_trend_vol_filter` | 2.7% | 2.4% | -2.8% | 0.098 | 0.315 | 235 | 0 |
| `donchian_trend` | 3.8% | 2.2% | -4.1% | 0.303 | 0.429 | 278 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 115 | 115 | 34.9% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 115 | 115 | 34.1% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 115 | 115 | 33.9% | 23.2% | 0.183 | 9.0 |
| `sma_trend_period175` | 115 | 115 | 32.7% | 25.7% | 0.101 | 8.9 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 115 | 115 | 32.5% | 25.5% | 0.379 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 115 | 115 | 31.5% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 112 | 112 | 30.8% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 115 | 115 | 30.4% | 24.5% | 0.396 | 9.5 |
| `sma_trend_period225` | 115 | 115 | 29.0% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 115 | 115 | 28.5% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 115/115 runs (mean holdout 34.9%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 115/115 runs (mean holdout 34.1%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 115/115 runs (mean holdout 33.9%, worst 23.2%, mean DSR 0.183)
- KEEP: `sma_trend_period175` was positive in 115/115 runs (mean holdout 32.7%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 115/115 runs (mean holdout 32.5%, worst 25.5%, mean DSR 0.379)
- FAMILY `sma_trend` has the best median holdout CAGR (24.0%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (18.1%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (17.7%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.9%) - add more parameters to it

