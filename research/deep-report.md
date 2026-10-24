# Deep research report

- Runs analysed: **21**
- Candidates per run: ~124
- Cumulative candidates evaluated: **2,532**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-24 07:22:35+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2327** (min 0.1793, max 0.4476, over 21 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 19.1% | 18.1% | -16.5% | 0.141 | 0.202 | 231 | 0 |
| `sma_trend_vol_filter` | 14.4% | 14.3% | -10.5% | 0.110 | 0.503 | 693 | 0 |
| `sma_trend_efficiency` | 13.6% | 12.2% | -13.7% | 0.220 | 0.411 | 270 | 0 |
| `ema_trend` | 10.2% | 11.6% | -15.2% | 0.107 | 0.155 | 126 | 0 |
| `sma_trend_fast_slow` | 5.8% | 8.5% | -16.5% | 0.115 | 0.187 | 210 | 0 |
| `ema_trend_regime` | 7.9% | 8.2% | -11.2% | 0.050 | 0.128 | 159 | 0 |
| `sma_trend_slope` | 6.4% | 7.5% | -14.2% | 0.094 | 0.151 | 180 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.306 | 0.429 | 42 | 0 |
| `sma_trend_confirm` | 5.2% | 1.6% | -16.6% | 0.086 | 0.143 | 102 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.100 | 0.311 | 42 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 21 | 21 | 29.2% | 28.1% | 0.131 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 21 | 21 | 28.4% | 27.4% | 0.348 | 8.0 |
| `sma_trend_period50` | 21 | 21 | 27.9% | 25.9% | 0.186 | 8.0 |
| `sma_trend_period175` | 21 | 21 | 26.7% | 25.7% | 0.103 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 18 | 18 | 26.6% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 21 | 21 | 26.4% | 25.5% | 0.384 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 21 | 21 | 26.0% | 25.0% | 0.088 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 21 | 21 | 25.3% | 24.5% | 0.401 | 10.0 |
| `sma_trend_period225` | 21 | 21 | 24.1% | 23.1% | 0.128 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 21 | 21 | 23.7% | 22.7% | 0.363 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 21 | 7.1% | -6.4% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 21 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 18 | 10.1% | -0.7% |
| `sma_trend_confirm_slow_period150_fast_period50` | 18 | 12.7% | -0.6% |
| `sma_trend_slope_period100_slope_bars10` | 18 | 13.6% | -1.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 18 | 6.7% | -2.2% |
| `sma_trend_slope_period150_slope_bars40` | 18 | 13.2% | -3.3% |
| `sma_trend_confirm_slow_period100_fast_period50` | 6 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 21/21 runs (mean holdout 29.2%, worst 28.1%, mean DSR 0.131)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 21/21 runs (mean holdout 28.4%, worst 27.4%, mean DSR 0.348)
- KEEP: `sma_trend_period50` was positive in 21/21 runs (mean holdout 27.9%, worst 25.9%, mean DSR 0.186)
- KEEP: `sma_trend_period175` was positive in 21/21 runs (mean holdout 26.7%, worst 25.7%, mean DSR 0.103)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 18/18 runs (mean holdout 26.6%, worst 26.2%, mean DSR 0.137)
- FAMILY `sma_trend` has the best median holdout CAGR (18.1%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (14.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (12.2%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.6%) - add more parameters to it

