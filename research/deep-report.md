# Deep research report

- Runs analysed: **42**
- Candidates per run: ~124
- Cumulative candidates evaluated: **5,136**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-29 16:12:23+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.222** (min 0.1793, max 0.4476, over 42 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 21.5% | 21.8% | -16.4% | 0.139 | 0.202 | 462 | 0 |
| `sma_trend_vol_filter` | 16.4% | 16.5% | -10.4% | 0.110 | 0.503 | 1369 | 0 |
| `sma_trend_efficiency` | 14.6% | 14.2% | -13.7% | 0.220 | 0.411 | 585 | 0 |
| `ema_trend` | 11.7% | 12.2% | -15.2% | 0.106 | 0.155 | 252 | 0 |
| `ema_trend_regime` | 9.5% | 9.4% | -11.1% | 0.050 | 0.128 | 310 | 0 |
| `sma_trend_fast_slow` | 7.8% | 9.3% | -16.4% | 0.113 | 0.187 | 438 | 0 |
| `sma_trend_slope` | 7.8% | 8.3% | -14.1% | 0.094 | 0.151 | 419 | 0 |
| `sma_trend_confirm` | 6.9% | 3.3% | -16.5% | 0.086 | 0.143 | 261 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.304 | 0.429 | 84 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.099 | 0.311 | 84 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 42 | 42 | 31.7% | 28.1% | 0.130 | 9.0 |
| `sma_trend_period50` | 42 | 42 | 31.4% | 25.9% | 0.182 | 8.5 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 42 | 42 | 31.0% | 27.4% | 0.346 | 8.0 |
| `sma_trend_period175` | 42 | 42 | 29.1% | 25.7% | 0.102 | 8.3 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 42 | 42 | 28.8% | 25.5% | 0.382 | 7.5 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 42 | 42 | 28.6% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 39 | 39 | 27.6% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 42 | 42 | 27.3% | 24.5% | 0.395 | 10.0 |
| `sma_trend_period225` | 42 | 42 | 26.6% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 42 | 42 | 26.1% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 42 | 6.9% | -4.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 39 | 6.6% | -1.6% |
| `sma_trend_slope_period150_slope_bars40` | 28 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 42/42 runs (mean holdout 31.7%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_period50` was positive in 42/42 runs (mean holdout 31.4%, worst 25.9%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 42/42 runs (mean holdout 31.0%, worst 27.4%, mean DSR 0.346)
- KEEP: `sma_trend_period175` was positive in 42/42 runs (mean holdout 29.1%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 42/42 runs (mean holdout 28.8%, worst 25.5%, mean DSR 0.382)
- FAMILY `sma_trend` has the best median holdout CAGR (21.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (16.5%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (14.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.2%) - add more parameters to it

