# Deep research report

- Runs analysed: **107**
- Candidates per run: ~124
- Cumulative candidates evaluated: **13,196**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-15 22:54:11+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2191** (min 0.1681, max 0.4476, over 107 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 23.5% | 23.7% | -16.0% | 0.139 | 0.202 | 1168 | 0 |
| `sma_trend_vol_filter` | 18.1% | 17.8% | -10.0% | 0.109 | 0.503 | 3455 | 0 |
| `sma_trend_efficiency` | 16.8% | 17.1% | -13.3% | 0.220 | 0.411 | 1575 | 0 |
| `ema_trend` | 12.5% | 13.7% | -14.9% | 0.105 | 0.155 | 633 | 0 |
| `ema_trend_regime` | 10.1% | 10.0% | -10.8% | 0.050 | 0.130 | 768 | 0 |
| `sma_trend_fast_slow` | 9.3% | 9.8% | -16.1% | 0.113 | 0.187 | 1156 | 0 |
| `sma_trend_slope` | 8.8% | 9.0% | -13.7% | 0.094 | 0.151 | 1160 | 0 |
| `sma_trend_confirm` | 8.3% | 5.7% | -16.0% | 0.086 | 0.143 | 760 | 0 |
| `donchian_trend` | 3.6% | 2.1% | -4.1% | 0.303 | 0.429 | 254 | 0 |
| `donchian_trend_vol_filter` | 2.5% | 2.1% | -2.8% | 0.098 | 0.315 | 219 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 107 | 107 | 34.2% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 107 | 107 | 33.4% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 107 | 107 | 33.1% | 23.2% | 0.184 | 8.9 |
| `sma_trend_period175` | 107 | 107 | 32.1% | 25.7% | 0.101 | 8.9 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 107 | 107 | 31.8% | 25.5% | 0.380 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 107 | 107 | 30.9% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 104 | 104 | 30.2% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 107 | 107 | 29.8% | 24.5% | 0.398 | 9.6 |
| `sma_trend_period225` | 107 | 107 | 28.4% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 107 | 107 | 27.9% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 107/107 runs (mean holdout 34.2%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 107/107 runs (mean holdout 33.4%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 107/107 runs (mean holdout 33.1%, worst 23.2%, mean DSR 0.184)
- KEEP: `sma_trend_period175` was positive in 107/107 runs (mean holdout 32.1%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 107/107 runs (mean holdout 31.8%, worst 25.5%, mean DSR 0.380)
- FAMILY `sma_trend` has the best median holdout CAGR (23.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.8%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (17.1%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.7%) - add more parameters to it

