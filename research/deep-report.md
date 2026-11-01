# Deep research report

- Runs analysed: **54**
- Candidates per run: ~124
- Cumulative candidates evaluated: **6,624**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-01 07:39:15+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2199** (min 0.1793, max 0.4476, over 54 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.3% | 22.7% | -16.4% | 0.139 | 0.202 | 594 | 0 |
| `sma_trend_vol_filter` | 17.1% | 17.3% | -10.3% | 0.109 | 0.503 | 1741 | 0 |
| `sma_trend_efficiency` | 15.0% | 15.0% | -13.7% | 0.220 | 0.411 | 765 | 0 |
| `ema_trend` | 12.0% | 12.8% | -15.2% | 0.105 | 0.155 | 324 | 0 |
| `ema_trend_regime` | 9.8% | 9.9% | -11.1% | 0.050 | 0.128 | 394 | 0 |
| `sma_trend_fast_slow` | 8.5% | 9.5% | -16.4% | 0.113 | 0.187 | 570 | 0 |
| `sma_trend_slope` | 8.2% | 8.5% | -14.1% | 0.094 | 0.151 | 563 | 0 |
| `sma_trend_confirm` | 7.4% | 4.3% | -16.5% | 0.086 | 0.143 | 357 | 0 |
| `donchian_trend` | 2.5% | 1.7% | -4.3% | 0.304 | 0.429 | 108 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.099 | 0.311 | 108 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 54 | 54 | 32.6% | 28.1% | 0.130 | 9.0 |
| `sma_trend_period50` | 54 | 54 | 32.5% | 25.9% | 0.181 | 8.6 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 54 | 54 | 31.9% | 27.4% | 0.346 | 8.0 |
| `sma_trend_period175` | 54 | 54 | 30.1% | 25.7% | 0.102 | 8.5 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 54 | 54 | 29.9% | 25.5% | 0.381 | 7.9 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 54 | 54 | 29.5% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 51 | 51 | 28.2% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 54 | 54 | 28.1% | 24.5% | 0.393 | 10.0 |
| `sma_trend_period225` | 54 | 54 | 27.5% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 54 | 54 | 27.0% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 54 | 6.8% | -3.8% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 28 | 13.1% | -2.9% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period100_fast_period20` | 21 | 10.1% | -0.9% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 54/54 runs (mean holdout 32.6%, worst 28.1%, mean DSR 0.130)
- KEEP: `sma_trend_period50` was positive in 54/54 runs (mean holdout 32.5%, worst 25.9%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 54/54 runs (mean holdout 31.9%, worst 27.4%, mean DSR 0.346)
- KEEP: `sma_trend_period175` was positive in 54/54 runs (mean holdout 30.1%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 54/54 runs (mean holdout 29.9%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.8%) - add more parameters to it

