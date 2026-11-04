# Deep research report

- Runs analysed: **66**
- Candidates per run: ~124
- Cumulative candidates evaluated: **8,112**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-04 18:02:23+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2197** (min 0.1793, max 0.4476, over 66 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.6% | 22.8% | -16.4% | 0.139 | 0.202 | 726 | 0 |
| `sma_trend_vol_filter` | 17.4% | 17.6% | -10.3% | 0.109 | 0.503 | 2125 | 0 |
| `sma_trend_efficiency` | 15.4% | 15.4% | -13.6% | 0.220 | 0.411 | 951 | 0 |
| `ema_trend` | 12.1% | 13.4% | -15.2% | 0.105 | 0.155 | 396 | 0 |
| `ema_trend_regime` | 9.9% | 10.0% | -11.1% | 0.050 | 0.128 | 472 | 0 |
| `sma_trend_fast_slow` | 8.8% | 9.7% | -16.4% | 0.113 | 0.187 | 702 | 0 |
| `sma_trend_slope` | 8.3% | 8.5% | -14.1% | 0.094 | 0.151 | 701 | 0 |
| `sma_trend_confirm` | 7.5% | 4.6% | -16.4% | 0.086 | 0.143 | 450 | 0 |
| `donchian_trend` | 2.7% | 1.8% | -4.3% | 0.303 | 0.429 | 132 | 0 |
| `donchian_trend_vol_filter` | 1.7% | 0.9% | -3.0% | 0.099 | 0.315 | 132 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 66 | 66 | 33.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 66 | 66 | 32.8% | 25.9% | 0.181 | 8.6 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 66 | 66 | 32.4% | 27.4% | 0.346 | 8.0 |
| `sma_trend_period175` | 66 | 66 | 30.7% | 25.7% | 0.102 | 8.7 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 66 | 66 | 30.4% | 25.5% | 0.381 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 66 | 66 | 29.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 63 | 63 | 28.6% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 66 | 66 | 28.5% | 24.5% | 0.394 | 10.0 |
| `sma_trend_period225` | 66 | 66 | 27.7% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 66 | 66 | 27.3% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 66 | 6.7% | -3.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 34 | 13.0% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 24 | 10.1% | -0.8% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 66/66 runs (mean holdout 33.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 66/66 runs (mean holdout 32.8%, worst 25.9%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 66/66 runs (mean holdout 32.4%, worst 27.4%, mean DSR 0.346)
- KEEP: `sma_trend_period175` was positive in 66/66 runs (mean holdout 30.7%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 66/66 runs (mean holdout 30.4%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.6%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.4%) - add more parameters to it

