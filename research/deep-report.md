# Deep research report

- Runs analysed: **60**
- Candidates per run: ~124
- Cumulative candidates evaluated: **7,368**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-02 23:36:37+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2186** (min 0.1793, max 0.4476, over 60 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.5% | 22.8% | -16.4% | 0.139 | 0.202 | 660 | 0 |
| `sma_trend_vol_filter` | 17.3% | 17.5% | -10.3% | 0.109 | 0.503 | 1927 | 0 |
| `sma_trend_efficiency` | 15.2% | 15.3% | -13.6% | 0.220 | 0.411 | 858 | 0 |
| `ema_trend` | 12.0% | 13.1% | -15.2% | 0.105 | 0.155 | 360 | 0 |
| `ema_trend_regime` | 9.9% | 9.9% | -11.1% | 0.050 | 0.128 | 433 | 0 |
| `sma_trend_fast_slow` | 8.7% | 9.5% | -16.4% | 0.113 | 0.187 | 636 | 0 |
| `sma_trend_slope` | 8.3% | 8.5% | -14.1% | 0.094 | 0.151 | 632 | 0 |
| `sma_trend_confirm` | 7.5% | 4.6% | -16.5% | 0.086 | 0.143 | 402 | 0 |
| `donchian_trend` | 2.6% | 1.7% | -4.3% | 0.303 | 0.429 | 120 | 0 |
| `donchian_trend_vol_filter` | 1.6% | 0.9% | -3.0% | 0.099 | 0.311 | 120 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 60 | 60 | 32.9% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 60 | 60 | 32.8% | 25.9% | 0.181 | 8.6 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 60 | 60 | 32.2% | 27.4% | 0.346 | 8.0 |
| `sma_trend_period175` | 60 | 60 | 30.5% | 25.7% | 0.102 | 8.6 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 60 | 60 | 30.2% | 25.5% | 0.381 | 8.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 60 | 60 | 29.7% | 25.0% | 0.087 | 9.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 57 | 57 | 28.5% | 26.2% | 0.137 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 60 | 60 | 28.3% | 24.5% | 0.393 | 10.0 |
| `sma_trend_period225` | 60 | 60 | 27.7% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 60 | 60 | 27.2% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 60 | 6.8% | -3.6% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 31 | 13.1% | -2.6% |
| `sma_trend_confirm_slow_period100_fast_period20` | 24 | 10.1% | -0.8% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 60/60 runs (mean holdout 32.9%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 60/60 runs (mean holdout 32.8%, worst 25.9%, mean DSR 0.181)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 60/60 runs (mean holdout 32.2%, worst 27.4%, mean DSR 0.346)
- KEEP: `sma_trend_period175` was positive in 60/60 runs (mean holdout 30.5%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 60/60 runs (mean holdout 30.2%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.5%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.3%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.1%) - add more parameters to it

