# Deep research report

- Runs analysed: **10**
- Candidates per run: ~124
- Cumulative candidates evaluated: **1,168**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-21 17:18:09+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2653** (min 0.1793, max 0.4476, over 10 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.3% | 17.4% | -16.5% | 0.143 | 0.202 | 110 | 0 |
| `sma_trend_vol_filter` | 13.8% | 13.1% | -10.5% | 0.112 | 0.503 | 330 | 0 |
| `sma_trend_efficiency` | 13.3% | 11.8% | -13.7% | 0.220 | 0.411 | 105 | 0 |
| `ema_trend` | 9.6% | 11.5% | -15.2% | 0.109 | 0.155 | 60 | 0 |
| `sma_trend_fast_slow` | 5.1% | 8.1% | -16.5% | 0.117 | 0.187 | 100 | 0 |
| `ema_trend_regime` | 7.3% | 7.7% | -11.2% | 0.052 | 0.128 | 73 | 0 |
| `sma_trend_slope` | 5.8% | 6.6% | -14.2% | 0.094 | 0.151 | 70 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.310 | 0.429 | 20 | 0 |
| `sma_trend_confirm` | 4.6% | 1.2% | -16.6% | 0.086 | 0.143 | 38 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.102 | 0.311 | 20 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 10 | 10 | 28.4% | 28.1% | 0.134 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 10 | 10 | 27.6% | 27.4% | 0.353 | 8.0 |
| `sma_trend_period50` | 10 | 10 | 26.4% | 25.9% | 0.189 | 8.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 7 | 7 | 26.3% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period175` | 10 | 10 | 26.0% | 25.7% | 0.105 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 10 | 10 | 25.7% | 25.5% | 0.388 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 10 | 10 | 25.3% | 25.0% | 0.090 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 10 | 10 | 24.7% | 24.5% | 0.406 | 10.0 |
| `sma_trend_period225` | 10 | 10 | 23.4% | 23.1% | 0.131 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 10 | 10 | 23.0% | 22.7% | 0.368 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 10 | 7.1% | -7.0% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 10 | 4.9% | -2.7% |
| `sma_trend_confirm_slow_period100_fast_period20` | 7 | 10.1% | -1.0% |
| `sma_trend_confirm_slow_period150_fast_period50` | 7 | 12.7% | -1.0% |
| `sma_trend_slope_period100_slope_bars10` | 7 | 13.6% | -2.0% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 7 | 6.8% | -2.3% |
| `sma_trend_slope_period150_slope_bars40` | 7 | 13.2% | -3.7% |
| `sma_trend_confirm_slow_period100_fast_period50` | 4 | 10.9% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 10/10 runs (mean holdout 28.4%, worst 28.1%, mean DSR 0.134)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 10/10 runs (mean holdout 27.6%, worst 27.4%, mean DSR 0.353)
- KEEP: `sma_trend_period50` was positive in 10/10 runs (mean holdout 26.4%, worst 25.9%, mean DSR 0.189)
- KEEP: `sma_trend_efficiency_period200_er_n30_er_min0.2` was positive in 7/7 runs (mean holdout 26.3%, worst 26.2%, mean DSR 0.137)
- KEEP: `sma_trend_period175` was positive in 10/10 runs (mean holdout 26.0%, worst 25.7%, mean DSR 0.105)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.1%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (11.8%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.5%) - add more parameters to it

