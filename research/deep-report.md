# Deep research report

- Runs analysed: **78**
- Candidates per run: ~124
- Cumulative candidates evaluated: **9,600**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-07 20:58:20+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2171** (min 0.1752, max 0.4476, over 78 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.5% | 22.7% | -16.3% | 0.139 | 0.202 | 854 | 0 |
| `sma_trend_vol_filter` | 17.3% | 17.4% | -10.3% | 0.109 | 0.503 | 2518 | 0 |
| `sma_trend_efficiency` | 15.6% | 15.3% | -13.5% | 0.220 | 0.411 | 1132 | 0 |
| `ema_trend` | 11.9% | 13.1% | -15.2% | 0.105 | 0.155 | 464 | 0 |
| `ema_trend_regime` | 9.7% | 9.8% | -11.1% | 0.050 | 0.128 | 549 | 0 |
| `sma_trend_fast_slow` | 8.7% | 9.5% | -16.3% | 0.113 | 0.187 | 830 | 0 |
| `sma_trend_slope` | 8.2% | 8.4% | -14.0% | 0.094 | 0.151 | 834 | 0 |
| `sma_trend_confirm` | 7.4% | 4.7% | -16.4% | 0.086 | 0.143 | 538 | 0 |
| `donchian_trend` | 2.8% | 1.8% | -4.2% | 0.304 | 0.429 | 167 | 0 |
| `donchian_trend_vol_filter` | 1.8% | 1.3% | -2.9% | 0.100 | 0.315 | 156 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 78 | 78 | 33.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 78 | 78 | 32.4% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 78 | 78 | 32.2% | 23.2% | 0.182 | 8.7 |
| `sma_trend_period175` | 78 | 78 | 30.8% | 25.7% | 0.102 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 78 | 78 | 30.5% | 25.5% | 0.381 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 78 | 78 | 29.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 75 | 75 | 28.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 78 | 78 | 28.6% | 24.5% | 0.393 | 9.9 |
| `sma_trend_period225` | 78 | 78 | 27.5% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 78 | 78 | 27.0% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 78 | 6.7% | -3.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 45 | 13.0% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 28 | 10.0% | -1.0% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 28 | 4.8% | -2.0% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 13 | 10.8% | -1.0% |
| `ema_trend_fast50_slow300` | 4 | 8.4% | -2.0% |
| `sma_trend_period400` | 4 | 14.8% | -0.6% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 78/78 runs (mean holdout 33.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 78/78 runs (mean holdout 32.4%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 78/78 runs (mean holdout 32.2%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_period175` was positive in 78/78 runs (mean holdout 30.8%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 78/78 runs (mean holdout 30.5%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.3%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.1%) - add more parameters to it

