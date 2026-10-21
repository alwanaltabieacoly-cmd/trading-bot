# Deep research report

- Runs analysed: **8**
- Candidates per run: ~124
- Cumulative candidates evaluated: **920**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-21 06:06:08+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2822** (min 0.1793, max 0.4476, over 8 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.1% | 17.4% | -16.5% | 0.145 | 0.202 | 88 | 0 |
| `sma_trend_vol_filter` | 13.7% | 13.1% | -10.5% | 0.112 | 0.503 | 264 | 0 |
| `sma_trend_efficiency` | 13.2% | 11.8% | -13.7% | 0.220 | 0.411 | 75 | 0 |
| `ema_trend` | 9.5% | 11.5% | -15.2% | 0.110 | 0.155 | 48 | 0 |
| `sma_trend_fast_slow` | 4.9% | 8.1% | -16.5% | 0.118 | 0.187 | 80 | 0 |
| `ema_trend_regime` | 7.2% | 7.7% | -11.2% | 0.052 | 0.128 | 57 | 0 |
| `sma_trend_slope` | 5.7% | 6.6% | -14.2% | 0.094 | 0.151 | 50 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.312 | 0.429 | 16 | 0 |
| `sma_trend_confirm` | 4.4% | 1.2% | -16.6% | 0.086 | 0.143 | 26 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.103 | 0.311 | 16 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 8 | 8 | 28.2% | 28.1% | 0.135 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 8 | 8 | 27.5% | 27.4% | 0.355 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 5 | 5 | 26.3% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period50` | 8 | 8 | 26.1% | 25.9% | 0.190 | 8.0 |
| `sma_trend_period175` | 8 | 8 | 25.8% | 25.7% | 0.106 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 8 | 8 | 25.6% | 25.5% | 0.390 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 8 | 8 | 25.1% | 25.0% | 0.091 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 8 | 8 | 24.6% | 24.5% | 0.408 | 10.0 |
| `sma_trend_period225` | 8 | 8 | 23.2% | 23.1% | 0.132 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 8 | 8 | 22.8% | 22.7% | 0.370 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 8 | 7.1% | -7.1% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 8 | 4.9% | -2.9% |
| `sma_trend_confirm_slow_period100_fast_period20` | 5 | 10.1% | -1.1% |
| `sma_trend_confirm_slow_period150_fast_period50` | 5 | 12.7% | -1.1% |
| `sma_trend_slope_period100_slope_bars10` | 5 | 13.6% | -2.1% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 5 | 6.8% | -2.5% |
| `sma_trend_slope_period150_slope_bars40` | 5 | 13.2% | -3.8% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 8/8 runs (mean holdout 28.2%, worst 28.1%, mean DSR 0.135)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 8/8 runs (mean holdout 27.5%, worst 27.4%, mean DSR 0.355)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 5/5 runs (mean holdout 26.3%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period50` was positive in 8/8 runs (mean holdout 26.1%, worst 25.9%, mean DSR 0.190)
- KEEP: `sma_trend_period175` was positive in 8/8 runs (mean holdout 25.8%, worst 25.7%, mean DSR 0.106)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.1%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (11.8%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

