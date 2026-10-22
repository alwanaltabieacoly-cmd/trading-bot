# Deep research report

- Runs analysed: **13**
- Candidates per run: ~124
- Cumulative candidates evaluated: **1,540**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-22 10:17:17+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2512** (min 0.1793, max 0.4476, over 13 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.7% | 17.4% | -16.5% | 0.142 | 0.202 | 143 | 0 |
| `sma_trend_vol_filter` | 14.1% | 13.9% | -10.5% | 0.111 | 0.503 | 429 | 0 |
| `sma_trend_efficiency` | 13.4% | 12.0% | -13.7% | 0.220 | 0.411 | 150 | 0 |
| `ema_trend` | 9.9% | 11.5% | -15.2% | 0.108 | 0.155 | 78 | 0 |
| `ema_trend_regime` | 7.6% | 8.1% | -11.2% | 0.051 | 0.128 | 97 | 0 |
| `sma_trend_fast_slow` | 5.4% | 8.1% | -16.5% | 0.116 | 0.187 | 130 | 0 |
| `sma_trend_slope` | 6.1% | 6.9% | -14.2% | 0.094 | 0.151 | 100 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.308 | 0.429 | 26 | 0 |
| `sma_trend_confirm` | 4.9% | 1.5% | -16.6% | 0.086 | 0.143 | 56 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.101 | 0.311 | 26 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 13 | 13 | 28.7% | 28.1% | 0.132 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 13 | 13 | 28.0% | 27.4% | 0.351 | 8.0 |
| `sma_trend_period50` | 13 | 13 | 27.0% | 25.9% | 0.188 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 10 | 10 | 26.4% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period175` | 13 | 13 | 26.3% | 25.7% | 0.104 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 13 | 13 | 26.0% | 25.5% | 0.386 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 13 | 13 | 25.6% | 25.0% | 0.089 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 13 | 13 | 25.0% | 24.5% | 0.404 | 10.0 |
| `sma_trend_period225` | 13 | 13 | 23.7% | 23.1% | 0.130 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 13 | 13 | 23.3% | 22.7% | 0.366 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 13 | 7.1% | -6.7% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 13 | 4.9% | -2.5% |
| `sma_trend_confirm_slow_period100_fast_period20` | 10 | 10.1% | -0.7% |
| `sma_trend_confirm_slow_period150_fast_period50` | 10 | 12.7% | -0.8% |
| `sma_trend_slope_period100_slope_bars10` | 10 | 13.6% | -1.7% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 10 | 6.7% | -2.2% |
| `sma_trend_slope_period150_slope_bars40` | 10 | 13.2% | -3.5% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 13/13 runs (mean holdout 28.7%, worst 28.1%, mean DSR 0.132)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 13/13 runs (mean holdout 28.0%, worst 27.4%, mean DSR 0.351)
- KEEP: `sma_trend_period50` was positive in 13/13 runs (mean holdout 27.0%, worst 25.9%, mean DSR 0.188)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 10/10 runs (mean holdout 26.4%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period175` was positive in 13/13 runs (mean holdout 26.3%, worst 25.7%, mean DSR 0.104)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.9%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

