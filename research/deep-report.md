# Deep research report

- Runs analysed: **81**
- Candidates per run: ~124
- Cumulative candidates evaluated: **9,972**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-08 15:17:58+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2153** (min 0.1681, max 0.4476, over 81 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.3% | 22.7% | -16.3% | 0.139 | 0.202 | 884 | 0 |
| `sma_trend_vol_filter` | 17.2% | 17.3% | -10.2% | 0.110 | 0.503 | 2617 | 0 |
| `sma_trend_efficiency` | 15.6% | 15.4% | -13.5% | 0.220 | 0.411 | 1177 | 0 |
| `ema_trend` | 11.7% | 12.8% | -15.1% | 0.105 | 0.155 | 479 | 0 |
| `ema_trend_regime` | 9.5% | 9.5% | -11.1% | 0.050 | 0.130 | 573 | 0 |
| `sma_trend_fast_slow` | 8.5% | 9.4% | -16.3% | 0.113 | 0.187 | 860 | 0 |
| `sma_trend_slope` | 8.1% | 8.3% | -14.0% | 0.094 | 0.151 | 864 | 0 |
| `sma_trend_confirm` | 7.3% | 4.7% | -16.4% | 0.086 | 0.143 | 556 | 0 |
| `donchian_trend` | 2.9% | 1.8% | -4.2% | 0.304 | 0.429 | 176 | 0 |
| `donchian_trend_vol_filter` | 1.9% | 1.3% | -2.9% | 0.100 | 0.315 | 165 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 81 | 81 | 33.0% | 28.1% | 0.129 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 81 | 81 | 32.3% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period50` | 81 | 81 | 31.9% | 23.2% | 0.183 | 8.7 |
| `sma_trend_period175` | 81 | 81 | 30.7% | 25.7% | 0.102 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 81 | 81 | 30.4% | 25.5% | 0.381 | 8.1 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 81 | 81 | 29.8% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 78 | 78 | 28.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 81 | 81 | 28.5% | 24.5% | 0.394 | 9.8 |
| `sma_trend_period225` | 81 | 81 | 27.4% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 81 | 81 | 26.9% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 81 | 6.7% | -3.7% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 48 | 13.0% | -2.7% |
| `sma_trend_confirm_slow_period100_fast_period20` | 31 | 10.1% | -1.1% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 31 | 4.8% | -1.9% |
| `sma_trend_slope_period100_slope_bars10` | 24 | 13.5% | -1.5% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 16 | 10.9% | -1.2% |
| `ema_trend_fast50_slow300` | 7 | 8.5% | -2.0% |
| `sma_trend_period400` | 7 | 14.9% | -0.6% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 81/81 runs (mean holdout 33.0%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 81/81 runs (mean holdout 32.3%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period50` was positive in 81/81 runs (mean holdout 31.9%, worst 23.2%, mean DSR 0.183)
- KEEP: `sma_trend_period175` was positive in 81/81 runs (mean holdout 30.7%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 81/81 runs (mean holdout 30.4%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.7%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.3%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (12.8%) - add more parameters to it

