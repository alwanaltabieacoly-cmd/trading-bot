# Deep research report

- Runs analysed: **17**
- Candidates per run: ~124
- Cumulative candidates evaluated: **2,036**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-23 10:09:43+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2402** (min 0.1793, max 0.4476, over 17 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.0% | 18.1% | -16.5% | 0.141 | 0.202 | 187 | 0 |
| `sma_trend_vol_filter` | 14.4% | 14.1% | -10.5% | 0.111 | 0.503 | 561 | 0 |
| `sma_trend_efficiency` | 13.5% | 12.2% | -13.7% | 0.220 | 0.411 | 210 | 0 |
| `ema_trend` | 10.1% | 11.6% | -15.2% | 0.107 | 0.155 | 102 | 0 |
| `sma_trend_fast_slow` | 5.6% | 8.4% | -16.5% | 0.115 | 0.187 | 170 | 0 |
| `ema_trend_regime` | 7.8% | 8.2% | -11.2% | 0.051 | 0.128 | 129 | 0 |
| `sma_trend_slope` | 6.4% | 7.5% | -14.2% | 0.094 | 0.151 | 140 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.307 | 0.429 | 34 | 0 |
| `sma_trend_confirm` | 5.2% | 1.5% | -16.6% | 0.086 | 0.143 | 80 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.101 | 0.311 | 34 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 17 | 17 | 29.1% | 28.1% | 0.132 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 17 | 17 | 28.3% | 27.4% | 0.349 | 8.0 |
| `sma_trend_period50` | 17 | 17 | 27.6% | 25.9% | 0.187 | 8.0 |
| `sma_trend_period175` | 17 | 17 | 26.6% | 25.7% | 0.104 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 14 | 14 | 26.5% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 17 | 17 | 26.4% | 25.5% | 0.385 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 17 | 17 | 25.9% | 25.0% | 0.089 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 17 | 17 | 25.2% | 24.5% | 0.402 | 10.0 |
| `sma_trend_period225` | 17 | 17 | 24.0% | 23.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 17 | 17 | 23.6% | 22.7% | 0.364 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 17 | 7.1% | -6.5% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 17 | 4.9% | -2.3% |
| `sma_trend_confirm_slow_period100_fast_period20` | 14 | 10.1% | -0.6% |
| `sma_trend_confirm_slow_period150_fast_period50` | 14 | 12.7% | -0.6% |
| `sma_trend_slope_period100_slope_bars10` | 14 | 13.6% | -1.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 14 | 6.7% | -2.2% |
| `sma_trend_slope_period150_slope_bars40` | 14 | 13.2% | -3.3% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 17/17 runs (mean holdout 29.1%, worst 28.1%, mean DSR 0.132)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 17/17 runs (mean holdout 28.3%, worst 27.4%, mean DSR 0.349)
- KEEP: `sma_trend_period50` was positive in 17/17 runs (mean holdout 27.6%, worst 25.9%, mean DSR 0.187)
- KEEP: `sma_trend_period175` was positive in 17/17 runs (mean holdout 26.6%, worst 25.7%, mean DSR 0.104)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 14/14 runs (mean holdout 26.5%, worst 26.2%, mean DSR 0.137)
- FAMILY `sma_trend` has the best median holdout CAGR (18.1%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.1%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.6%) - add more parameters to it

