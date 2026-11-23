# Deep research report

- Runs analysed: **130**
- Candidates per run: ~124
- Cumulative candidates evaluated: **16,048**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-23 02:51:21+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2266** (min 0.1681, max 0.4476, over 130 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 25.5% | 25.9% | -15.8% | 0.138 | 0.202 | 1421 | 0 |
| `sma_trend_vol_filter` | 19.6% | 19.0% | -9.7% | 0.109 | 0.503 | 4145 | 0 |
| `sma_trend_efficiency` | 18.1% | 18.7% | -13.2% | 0.219 | 0.411 | 1943 | 0 |
| `ema_trend` | 13.9% | 14.5% | -14.7% | 0.105 | 0.155 | 771 | 0 |
| `ema_trend_regime` | 11.3% | 10.9% | -10.6% | 0.050 | 0.130 | 920 | 0 |
| `sma_trend_fast_slow` | 10.5% | 10.4% | -16.0% | 0.112 | 0.187 | 1432 | 0 |
| `sma_trend_slope` | 10.1% | 10.0% | -13.5% | 0.094 | 0.151 | 1436 | 0 |
| `sma_trend_confirm` | 9.8% | 8.2% | -15.6% | 0.086 | 0.143 | 944 | 0 |
| `donchian_trend_vol_filter` | 3.0% | 2.6% | -2.7% | 0.097 | 0.315 | 265 | 0 |
| `donchian_trend` | 4.1% | 2.5% | -4.1% | 0.302 | 0.429 | 323 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 130 | 130 | 36.1% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 130 | 130 | 35.5% | 23.2% | 0.182 | 9.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 130 | 130 | 35.3% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 130 | 130 | 33.9% | 25.7% | 0.101 | 9.1 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 130 | 130 | 33.7% | 25.5% | 0.378 | 8.2 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 130 | 130 | 32.7% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 127 | 127 | 31.8% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 130 | 130 | 31.7% | 24.5% | 0.393 | 9.5 |
| `sma_trend_period225` | 130 | 130 | 30.1% | 23.1% | 0.126 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 130 | 130 | 29.6% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 130/130 runs (mean holdout 36.1%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 130/130 runs (mean holdout 35.5%, worst 23.2%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 130/130 runs (mean holdout 35.3%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 130/130 runs (mean holdout 33.9%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 130/130 runs (mean holdout 33.7%, worst 25.5%, mean DSR 0.378)
- FAMILY `sma_trend` has the best median holdout CAGR (25.9%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (19.0%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (18.7%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (14.5%) - add more parameters to it

