# Deep research report

- Runs analysed: **14**
- Candidates per run: ~124
- Cumulative candidates evaluated: **1,664**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-22 15:23:26+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2478** (min 0.1793, max 0.4476, over 14 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.8% | 17.8% | -16.5% | 0.142 | 0.202 | 154 | 0 |
| `sma_trend_vol_filter` | 14.1% | 14.0% | -10.5% | 0.111 | 0.503 | 462 | 0 |
| `sma_trend_efficiency` | 13.4% | 12.0% | -13.7% | 0.220 | 0.411 | 165 | 0 |
| `ema_trend` | 9.9% | 11.5% | -15.2% | 0.108 | 0.155 | 84 | 0 |
| `sma_trend_fast_slow` | 5.4% | 8.2% | -16.5% | 0.116 | 0.187 | 140 | 0 |
| `ema_trend_regime` | 7.6% | 8.1% | -11.2% | 0.051 | 0.128 | 105 | 0 |
| `sma_trend_slope` | 6.2% | 7.2% | -14.2% | 0.094 | 0.151 | 110 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.308 | 0.429 | 28 | 0 |
| `sma_trend_confirm` | 5.0% | 1.5% | -16.6% | 0.086 | 0.143 | 62 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.101 | 0.311 | 28 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 14 | 14 | 28.8% | 28.1% | 0.132 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 14 | 14 | 28.1% | 27.4% | 0.350 | 8.0 |
| `sma_trend_period50` | 14 | 14 | 27.2% | 25.9% | 0.188 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 11 | 11 | 26.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period175` | 14 | 14 | 26.4% | 25.7% | 0.104 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 14 | 14 | 26.1% | 25.5% | 0.386 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 14 | 14 | 25.7% | 25.0% | 0.089 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 14 | 14 | 25.0% | 24.5% | 0.403 | 10.0 |
| `sma_trend_period225` | 14 | 14 | 23.8% | 23.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 14 | 14 | 23.4% | 22.7% | 0.365 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 14 | 7.1% | -6.7% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 14 | 4.9% | -2.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 11 | 10.1% | -0.7% |
| `sma_trend_confirm_slow_period150_fast_period50` | 11 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 11 | 13.6% | -1.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 11 | 6.7% | -2.2% |
| `sma_trend_slope_period150_slope_bars40` | 11 | 13.2% | -3.4% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 14/14 runs (mean holdout 28.8%, worst 28.1%, mean DSR 0.132)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 14/14 runs (mean holdout 28.1%, worst 27.4%, mean DSR 0.350)
- KEEP: `sma_trend_period50` was positive in 14/14 runs (mean holdout 27.2%, worst 25.9%, mean DSR 0.188)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 11/11 runs (mean holdout 26.4%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period175` was positive in 14/14 runs (mean holdout 26.4%, worst 25.7%, mean DSR 0.104)
- FAMILY `sma_trend` has the best median holdout CAGR (17.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

