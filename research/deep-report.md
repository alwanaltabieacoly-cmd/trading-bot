# Deep research report

- Runs analysed: **46**
- Candidates per run: ~124
- Cumulative candidates evaluated: **5,632**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-30 14:15:24+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2213** (min 0.1793, max 0.4476, over 46 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 21.8% | 22.3% | -16.4% | 0.139 | 0.202 | 506 | 0 |
| `sma_trend_vol_filter` | 16.7% | 16.7% | -10.4% | 0.109 | 0.503 | 1493 | 0 |
| `sma_trend_efficiency` | 14.7% | 14.5% | -13.7% | 0.220 | 0.411 | 645 | 0 |
| `ema_trend` | 11.8% | 12.3% | -15.2% | 0.106 | 0.155 | 276 | 0 |
| `ema_trend_regime` | 9.6% | 9.6% | -11.1% | 0.050 | 0.128 | 338 | 0 |
| `sma_trend_fast_slow` | 8.1% | 9.4% | -16.4% | 0.113 | 0.187 | 482 | 0 |
| `sma_trend_slope` | 8.0% | 8.5% | -14.1% | 0.094 | 0.151 | 467 | 0 |
| `sma_trend_confirm` | 7.1% | 3.5% | -16.5% | 0.086 | 0.143 | 293 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.304 | 0.429 | 92 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.099 | 0.311 | 92 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 46 | 46 | 32.0% | 28.1% | 0.130 | 9.0 |
| `sma_trend_period50` | 46 | 46 | 31.8% | 25.9% | 0.182 | 8.6 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 46 | 46 | 31.3% | 27.4% | 0.346 | 8.0 |
| `sma_trend_period175` | 46 | 46 | 29.5% | 25.7% | 0.102 | 8.3 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 46 | 46 | 29.2% | 25.5% | 0.382 | 7.7 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 46 | 46 | 28.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 43 | 43 | 27.8% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 46 | 46 | 27.6% | 24.5% | 0.394 | 10.0 |
| `sma_trend_period225` | 46 | 46 | 26.9% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 46 | 46 | 26.4% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 46 | 6.9% | -4.3% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 43 | 6.6% | -1.5% |
| `sma_trend_slope_period150_slope_bars40` | 28 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 46/46 runs (mean holdout 32.0%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_period50` was positive in 46/46 runs (mean holdout 31.8%, worst 25.9%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 46/46 runs (mean holdout 31.3%, worst 27.4%, mean DSR 0.346)
- KEEP: `sma_trend_period175` was positive in 46/46 runs (mean holdout 29.5%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 46/46 runs (mean holdout 29.2%, worst 25.5%, mean DSR 0.382)
- FAMILY `sma_trend` has the best median holdout CAGR (22.3%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (16.7%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (14.5%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.3%) - add more parameters to it

