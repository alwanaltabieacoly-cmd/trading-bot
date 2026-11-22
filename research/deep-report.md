# Deep research report

- Runs analysed: **129**
- Candidates per run: ~124
- Cumulative candidates evaluated: **15,924**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-22 21:51:39+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2263** (min 0.1681, max 0.4476, over 129 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 25.4% | 25.7% | -15.8% | 0.138 | 0.202 | 1410 | 0 |
| `sma_trend_vol_filter` | 19.5% | 19.0% | -9.7% | 0.109 | 0.503 | 4115 | 0 |
| `sma_trend_efficiency` | 18.0% | 18.7% | -13.2% | 0.219 | 0.411 | 1927 | 0 |
| `ema_trend` | 13.9% | 14.4% | -14.7% | 0.105 | 0.155 | 765 | 0 |
| `ema_trend_regime` | 11.3% | 10.8% | -10.6% | 0.050 | 0.130 | 913 | 0 |
| `sma_trend_fast_slow` | 10.4% | 10.4% | -16.0% | 0.112 | 0.187 | 1420 | 0 |
| `sma_trend_slope` | 10.0% | 10.0% | -13.5% | 0.094 | 0.151 | 1424 | 0 |
| `sma_trend_confirm` | 9.7% | 8.2% | -15.7% | 0.086 | 0.143 | 936 | 0 |
| `donchian_trend_vol_filter` | 3.0% | 2.6% | -2.7% | 0.097 | 0.315 | 263 | 0 |
| `donchian_trend` | 4.1% | 2.5% | -4.1% | 0.302 | 0.429 | 320 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 129 | 129 | 36.0% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 129 | 129 | 35.4% | 23.2% | 0.182 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 129 | 129 | 35.2% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 129 | 129 | 33.9% | 25.7% | 0.101 | 9.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 129 | 129 | 33.6% | 25.5% | 0.378 | 8.2 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 129 | 129 | 32.6% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 126 | 126 | 31.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 129 | 129 | 31.6% | 24.5% | 0.393 | 9.5 |
| `sma_trend_period225` | 129 | 129 | 30.0% | 23.1% | 0.126 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 129 | 129 | 29.5% | 22.7% | 0.360 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 95 | 6.7% | -3.6% |
| `sma_trend_slope_period150_slope_bars40` | 62 | 12.9% | -2.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 33 | 10.1% | -1.2% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 33 | 4.8% | -1.8% |
| `sma_trend_slope_period100_slope_bars10` | 26 | 13.5% | -1.4% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 18 | 10.9% | -1.3% |
| `ema_trend_fast50_slow300` | 9 | 8.5% | -2.0% |
| `sma_trend_period400` | 9 | 15.0% | -0.5% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 129/129 runs (mean holdout 36.0%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 129/129 runs (mean holdout 35.4%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 129/129 runs (mean holdout 35.2%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 129/129 runs (mean holdout 33.9%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 129/129 runs (mean holdout 33.6%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (25.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (18.7%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.4%) - add more parameters to it

