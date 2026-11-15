# Deep research report

- Runs analysed: **104**
- Candidates per run: ~124
- Cumulative candidates evaluated: **12,824**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-15 02:44:40+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.218** (min 0.1681, max 0.4476, over 104 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 23.2% | 23.2% | -16.0% | 0.139 | 0.202 | 1135 | 0 |
| `sma_trend_vol_filter` | 17.9% | 17.7% | -10.0% | 0.110 | 0.503 | 3365 | 0 |
| `sma_trend_efficiency` | 16.7% | 16.9% | -13.3% | 0.220 | 0.411 | 1527 | 0 |
| `ema_trend` | 12.3% | 13.4% | -15.0% | 0.105 | 0.155 | 615 | 0 |
| `ema_trend_regime` | 10.0% | 10.0% | -10.9% | 0.050 | 0.130 | 747 | 0 |
| `sma_trend_fast_slow` | 9.2% | 9.7% | -16.2% | 0.113 | 0.187 | 1120 | 0 |
| `sma_trend_slope` | 8.6% | 8.8% | -13.8% | 0.094 | 0.151 | 1124 | 0 |
| `sma_trend_confirm` | 8.0% | 5.5% | -16.0% | 0.086 | 0.143 | 736 | 0 |
| `donchian_trend` | 3.5% | 2.1% | -4.1% | 0.303 | 0.429 | 245 | 0 |
| `donchian_trend_vol_filter` | 2.5% | 1.9% | -2.8% | 0.098 | 0.315 | 213 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 104 | 104 | 34.0% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 104 | 104 | 33.2% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 104 | 104 | 32.8% | 23.2% | 0.184 | 8.8 |
| `sma_trend_period175` | 104 | 104 | 31.8% | 25.7% | 0.101 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 104 | 104 | 31.5% | 25.5% | 0.380 | 8.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 104 | 104 | 30.6% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 101 | 101 | 30.0% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 104 | 104 | 29.5% | 24.5% | 0.399 | 9.6 |
| `sma_trend_period225` | 104 | 104 | 28.2% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 104 | 104 | 27.7% | 22.7% | 0.360 | 8.0 |

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

- KEEP: `sma_trend_period200` was positive in 104/104 runs (mean holdout 34.0%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 104/104 runs (mean holdout 33.2%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 104/104 runs (mean holdout 32.8%, worst 23.2%, mean DSR 0.184)
- KEEP: `sma_trend_period175` was positive in 104/104 runs (mean holdout 31.8%, worst 25.7%, mean DSR 0.101)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 104/104 runs (mean holdout 31.5%, worst 25.5%, mean DSR 0.380)
- FAMILY `sma_trend` has the best median holdout CAGR (23.2%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.7%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (16.9%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.4%) - add more parameters to it

