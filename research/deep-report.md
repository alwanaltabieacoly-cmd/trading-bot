# Deep research report

- Runs analysed: **30**
- Candidates per run: ~124
- Cumulative candidates evaluated: **3,648**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-26 14:21:26+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2266** (min 0.1793, max 0.4476, over 30 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.9% | 19.7% | -16.4% | 0.140 | 0.202 | 330 | 0 |
| `sma_trend_vol_filter` | 15.0% | 14.7% | -10.4% | 0.110 | 0.503 | 990 | 0 |
| `sma_trend_efficiency` | 14.0% | 12.5% | -13.7% | 0.220 | 0.411 | 405 | 0 |
| `ema_trend` | 10.6% | 11.8% | -15.2% | 0.106 | 0.155 | 180 | 0 |
| `sma_trend_fast_slow` | 6.5% | 8.9% | -16.5% | 0.114 | 0.187 | 306 | 0 |
| `ema_trend_regime` | 8.3% | 8.6% | -11.2% | 0.050 | 0.128 | 226 | 0 |
| `sma_trend_slope` | 6.8% | 7.6% | -14.2% | 0.094 | 0.151 | 276 | 0 |
| `sma_trend_confirm` | 5.7% | 2.2% | -16.5% | 0.086 | 0.143 | 165 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.305 | 0.429 | 60 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 60 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 30 | 30 | 29.9% | 28.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 30 | 30 | 29.2% | 27.4% | 0.347 | 8.0 |
| `sma_trend_period50` | 30 | 30 | 29.1% | 25.9% | 0.185 | 8.0 |
| `sma_trend_period175` | 30 | 30 | 27.3% | 25.7% | 0.103 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 30 | 30 | 27.1% | 25.5% | 0.383 | 7.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 27 | 27 | 26.9% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 30 | 30 | 26.7% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 30 | 30 | 26.0% | 24.5% | 0.399 | 10.0 |
| `sma_trend_period225` | 30 | 30 | 24.8% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 30 | 30 | 24.4% | 22.7% | 0.362 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 30 | 7.0% | -5.7% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 27 | 6.7% | -1.9% |
| `sma_trend_slope_period150_slope_bars40` | 27 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 30/30 runs (mean holdout 29.9%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 30/30 runs (mean holdout 29.2%, worst 27.4%, mean DSR 0.347)
- KEEP: `sma_trend_period50` was positive in 30/30 runs (mean holdout 29.1%, worst 25.9%, mean DSR 0.185)
- KEEP: `sma_trend_period175` was positive in 30/30 runs (mean holdout 27.3%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 30/30 runs (mean holdout 27.1%, worst 25.5%, mean DSR 0.383)
- FAMILY `sma_trend` has the best median holdout CAGR (19.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.7%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.5%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.8%) - add more parameters to it

