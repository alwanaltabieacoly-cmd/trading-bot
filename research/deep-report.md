# Deep research report

- Runs analysed: **4**
- Candidates per run: ~100
- Cumulative candidates evaluated: **424**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-20 01:35:44+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.3805** (min 0.1793, max 0.4476, over 4 runs)
- Verdict: **search is informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.0% | 17.4% | -16.5% | 0.151 | 0.202 | 44 | 0 |
| `sma_trend_vol_filter` | 13.6% | 13.0% | -10.5% | 0.116 | 0.503 | 132 | 0 |
| `sma_trend_efficiency` | 13.1% | 11.5% | -13.7% | 0.220 | 0.411 | 15 | 0 |
| `ema_trend` | 9.4% | 11.1% | -15.2% | 0.115 | 0.155 | 24 | 0 |
| `sma_trend_fast_slow` | 4.8% | 7.9% | -16.5% | 0.123 | 0.187 | 40 | 0 |
| `ema_trend_regime` | 7.1% | 7.4% | -11.2% | 0.055 | 0.128 | 28 | 0 |
| `sma_trend_slope` | 5.5% | 6.3% | -14.2% | 0.094 | 0.151 | 10 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.321 | 0.429 | 8 | 0 |
| `sma_trend_confirm` | 4.3% | 0.9% | -16.6% | 0.086 | 0.143 | 5 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.108 | 0.311 | 8 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 4 | 4 | 28.1% | 28.1% | 0.141 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 4 | 4 | 27.4% | 27.4% | 0.366 | 8.0 |
| `sma_trend_period50` | 4 | 4 | 25.9% | 25.9% | 0.197 | 8.0 |
| `sma_trend_period175` | 4 | 4 | 25.7% | 25.7% | 0.111 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 4 | 4 | 25.5% | 25.5% | 0.401 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 4 | 4 | 25.0% | 25.0% | 0.096 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 4 | 4 | 24.5% | 24.5% | 0.419 | 10.0 |
| `sma_trend_period225` | 4 | 4 | 23.1% | 23.1% | 0.138 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 4 | 4 | 22.7% | 22.7% | 0.380 | 8.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct4.0` | 4 | 4 | 20.8% | 20.8% | 0.437 | 9.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 4 | 7.1% | -7.2% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 4 | 4.9% | -3.0% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max70` | 3 | 0.5% | -5.6% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max80` | 3 | 12.2% | -5.4% |
| `sma_trend_confirm_slow_period100_fast_period50` | 1 | 10.9% | -0.2% |
| `sma_trend_confirm_slow_period100_fast_period20` | 1 | 10.1% | -1.2% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 1 | 6.8% | -2.6% |
| `sma_trend_confirm_slow_period150_fast_period50` | 1 | 12.6% | -1.2% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 4/4 runs (mean holdout 28.1%, worst 28.1%, mean DSR 0.141)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 4/4 runs (mean holdout 27.4%, worst 27.4%, mean DSR 0.366)
- KEEP: `sma_trend_period50` was positive in 4/4 runs (mean holdout 25.9%, worst 25.9%, mean DSR 0.197)
- KEEP: `sma_trend_period175` was positive in 4/4 runs (mean holdout 25.7%, worst 25.7%, mean DSR 0.111)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 4/4 runs (mean holdout 25.5%, worst 25.5%, mean DSR 0.401)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (11.5%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.1%) - add more parameters to it

