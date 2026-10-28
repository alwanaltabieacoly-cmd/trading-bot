# Deep research report

- Runs analysed: **37**
- Candidates per run: ~124
- Cumulative candidates evaluated: **4,516**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-28 09:46:05+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2237** (min 0.1793, max 0.4476, over 37 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 21.0% | 20.9% | -16.4% | 0.140 | 0.202 | 407 | 0 |
| `sma_trend_vol_filter` | 15.9% | 16.0% | -10.4% | 0.110 | 0.503 | 1214 | 0 |
| `sma_trend_efficiency` | 14.4% | 13.2% | -13.7% | 0.220 | 0.411 | 510 | 0 |
| `ema_trend` | 11.4% | 11.9% | -15.2% | 0.106 | 0.155 | 222 | 0 |
| `ema_trend_regime` | 9.1% | 9.1% | -11.2% | 0.050 | 0.128 | 275 | 0 |
| `sma_trend_fast_slow` | 7.4% | 9.1% | -16.4% | 0.114 | 0.187 | 383 | 0 |
| `sma_trend_slope` | 7.5% | 8.2% | -14.1% | 0.094 | 0.151 | 359 | 0 |
| `sma_trend_confirm` | 6.5% | 3.0% | -16.5% | 0.086 | 0.143 | 221 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.304 | 0.429 | 74 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 74 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 37 | 37 | 31.1% | 28.1% | 0.130 | 9.0 |
| `sma_trend_period50` | 37 | 37 | 30.7% | 25.9% | 0.183 | 8.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 37 | 37 | 30.4% | 27.4% | 0.347 | 8.0 |
| `sma_trend_period175` | 37 | 37 | 28.5% | 25.7% | 0.102 | 8.2 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 37 | 37 | 28.2% | 25.5% | 0.382 | 7.3 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 37 | 37 | 27.9% | 25.0% | 0.088 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 34 | 34 | 27.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 37 | 37 | 26.8% | 24.5% | 0.396 | 10.0 |
| `sma_trend_period225` | 37 | 37 | 26.0% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 37 | 37 | 25.5% | 22.7% | 0.362 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 37 | 6.9% | -5.0% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 34 | 6.7% | -1.7% |
| `sma_trend_slope_period150_slope_bars40` | 28 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 37/37 runs (mean holdout 31.1%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_period50` was positive in 37/37 runs (mean holdout 30.7%, worst 25.9%, mean DSR 0.183)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 37/37 runs (mean holdout 30.4%, worst 27.4%, mean DSR 0.347)
- KEEP: `sma_trend_period175` was positive in 37/37 runs (mean holdout 28.5%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 37/37 runs (mean holdout 28.2%, worst 25.5%, mean DSR 0.382)
- FAMILY `sma_trend` has the best median holdout CAGR (20.9%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (16.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (13.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.9%) - add more parameters to it

