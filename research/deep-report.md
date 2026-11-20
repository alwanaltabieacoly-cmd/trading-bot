# Deep research report

- Runs analysed: **121**
- Candidates per run: ~124
- Cumulative candidates evaluated: **14,932**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-20 12:59:42+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2238** (min 0.1681, max 0.4476, over 121 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 24.7% | 24.7% | -15.8% | 0.139 | 0.202 | 1322 | 0 |
| `sma_trend_vol_filter` | 19.0% | 18.4% | -9.8% | 0.109 | 0.503 | 3875 | 0 |
| `sma_trend_efficiency` | 17.6% | 18.4% | -13.3% | 0.219 | 0.411 | 1799 | 0 |
| `ema_trend` | 13.4% | 14.1% | -14.8% | 0.105 | 0.155 | 717 | 0 |
| `ema_trend_regime` | 10.9% | 10.6% | -10.7% | 0.050 | 0.130 | 857 | 0 |
| `sma_trend_fast_slow` | 10.0% | 10.2% | -16.1% | 0.113 | 0.187 | 1324 | 0 |
| `sma_trend_slope` | 9.6% | 9.7% | -13.6% | 0.094 | 0.151 | 1328 | 0 |
| `sma_trend_confirm` | 9.2% | 7.3% | -15.8% | 0.086 | 0.143 | 872 | 0 |
| `donchian_trend_vol_filter` | 2.8% | 2.5% | -2.7% | 0.097 | 0.315 | 247 | 0 |
| `donchian_trend` | 3.9% | 2.5% | -4.1% | 0.302 | 0.429 | 296 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 121 | 121 | 35.4% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 121 | 121 | 34.6% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 121 | 121 | 34.5% | 23.2% | 0.183 | 9.0 |
| `sma_trend_period175` | 121 | 121 | 33.2% | 25.7% | 0.101 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 121 | 121 | 33.0% | 25.5% | 0.379 | 8.2 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 121 | 121 | 32.0% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 118 | 118 | 31.2% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 121 | 121 | 31.0% | 24.5% | 0.394 | 9.5 |
| `sma_trend_period225` | 121 | 121 | 29.4% | 23.1% | 0.126 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 121 | 121 | 28.9% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 121/121 runs (mean holdout 35.4%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 121/121 runs (mean holdout 34.6%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 121/121 runs (mean holdout 34.5%, worst 23.2%, mean DSR 0.183)
- KEEP: `sma_trend_period175` was positive in 121/121 runs (mean holdout 33.2%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 121/121 runs (mean holdout 33.0%, worst 25.5%, mean DSR 0.379)
- FAMILY `sma_trend` has the best median holdout CAGR (24.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (18.4%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (18.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.1%) - add more parameters to it

