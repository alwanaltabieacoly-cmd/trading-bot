# Deep research report

- Runs analysed: **83**
- Candidates per run: ~124
- Cumulative candidates evaluated: **10,220**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-08 23:47:51+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2142** (min 0.1681, max 0.4476, over 83 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.2% | 22.6% | -16.3% | 0.139 | 0.202 | 904 | 0 |
| `sma_trend_vol_filter` | 17.2% | 17.2% | -10.2% | 0.110 | 0.503 | 2683 | 0 |
| `sma_trend_efficiency` | 15.7% | 15.4% | -13.5% | 0.220 | 0.411 | 1207 | 0 |
| `ema_trend` | 11.6% | 12.5% | -15.1% | 0.105 | 0.155 | 489 | 0 |
| `ema_trend_regime` | 9.4% | 9.5% | -11.1% | 0.050 | 0.130 | 589 | 0 |
| `sma_trend_fast_slow` | 8.5% | 9.3% | -16.3% | 0.113 | 0.187 | 880 | 0 |
| `sma_trend_slope` | 8.0% | 8.3% | -14.0% | 0.094 | 0.151 | 884 | 0 |
| `sma_trend_confirm` | 7.2% | 4.6% | -16.4% | 0.086 | 0.143 | 568 | 0 |
| `donchian_trend` | 2.9% | 1.8% | -4.2% | 0.304 | 0.429 | 182 | 0 |
| `donchian_trend_vol_filter` | 1.9% | 1.3% | -2.9% | 0.100 | 0.315 | 171 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 83 | 83 | 33.0% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 83 | 83 | 32.2% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 83 | 83 | 31.7% | 23.2% | 0.183 | 8.7 |
| `sma_trend_period175` | 83 | 83 | 30.6% | 25.7% | 0.102 | 8.7 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 83 | 83 | 30.4% | 25.5% | 0.381 | 8.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 83 | 83 | 29.7% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 80 | 80 | 28.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 83 | 83 | 28.4% | 24.5% | 0.395 | 9.7 |
| `sma_trend_period225` | 83 | 83 | 27.3% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 83 | 83 | 26.8% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 83 | 6.7% | -3.7% |
| `sma_trend_slope_period150_slope_bars40` | 50 | 13.0% | -2.7% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 33 | 10.1% | -1.2% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 33 | 4.8% | -1.8% |
| `sma_trend_slope_period100_slope_bars10` | 26 | 13.5% | -1.4% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 18 | 10.9% | -1.3% |
| `ema_trend_fast50_slow300` | 9 | 8.5% | -2.0% |
| `sma_trend_period400` | 9 | 15.0% | -0.5% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 83/83 runs (mean holdout 33.0%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 83/83 runs (mean holdout 32.2%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 83/83 runs (mean holdout 31.7%, worst 23.2%, mean DSR 0.183)
- KEEP: `sma_trend_period175` was positive in 83/83 runs (mean holdout 30.6%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 83/83 runs (mean holdout 30.4%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.6%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.2%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.5%) - add more parameters to it

