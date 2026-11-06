# Deep research report

- Runs analysed: **73**
- Candidates per run: ~124
- Cumulative candidates evaluated: **8,980**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-11-06 18:02:33+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.2196** (min 0.1793, max 0.4476, over 73 runs)
- Verdict: **search is weakly informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 22.7% | 22.8% | -16.3% | 0.139 | 0.202 | 803 | 0 |
| `sma_trend_vol_filter` | 17.5% | 17.6% | -10.3% | 0.109 | 0.503 | 2353 | 0 |
| `sma_trend_efficiency` | 15.5% | 15.4% | -13.5% | 0.220 | 0.411 | 1057 | 0 |
| `ema_trend` | 12.1% | 13.4% | -15.2% | 0.105 | 0.155 | 438 | 0 |
| `ema_trend_regime` | 9.9% | 10.0% | -11.1% | 0.050 | 0.128 | 518 | 0 |
| `sma_trend_fast_slow` | 8.8% | 9.8% | -16.4% | 0.113 | 0.187 | 779 | 0 |
| `sma_trend_slope` | 8.3% | 8.5% | -14.1% | 0.094 | 0.151 | 779 | 0 |
| `sma_trend_confirm` | 7.6% | 4.7% | -16.4% | 0.086 | 0.143 | 506 | 0 |
| `donchian_trend` | 2.8% | 1.8% | -4.2% | 0.304 | 0.429 | 152 | 0 |
| `donchian_trend_vol_filter` | 1.8% | 1.2% | -2.9% | 0.100 | 0.315 | 146 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 73 | 73 | 33.2% | 28.1% | 0.129 | 9.0 |
| `sma_trend_period50` | 73 | 73 | 32.7% | 25.9% | 0.182 | 8.7 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 73 | 73 | 32.5% | 27.4% | 0.345 | 8.0 |
| `sma_trend_period175` | 73 | 73 | 30.9% | 25.7% | 0.102 | 8.8 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 73 | 73 | 30.6% | 25.5% | 0.381 | 8.2 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 73 | 73 | 30.0% | 25.0% | 0.087 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 73 | 73 | 28.7% | 24.5% | 0.393 | 10.0 |
| `sma_trend_efficiency_period200_er_n30_er_min0.2` | 70 | 70 | 28.7% | 26.2% | 0.137 | 9.0 |
| `sma_trend_period225` | 73 | 73 | 27.7% | 23.1% | 0.127 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 73 | 73 | 27.3% | 22.7% | 0.361 | 8.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period250_fast_period10` | 73 | 6.7% | -3.5% |
| `sma_trend_efficiency_period250_er_n20_er_min0.3` | 49 | 6.6% | -1.4% |
| `sma_trend_slope_period150_slope_bars40` | 40 | 13.0% | -2.4% |
| `sma_trend_confirm_slow_period100_fast_period20` | 24 | 10.1% | -0.8% |
| `sma_trend_fast_slow_slow_period150_fast_period10` | 24 | 4.9% | -2.1% |
| `sma_trend_confirm_slow_period150_fast_period50` | 21 | 12.7% | -0.7% |
| `sma_trend_slope_period100_slope_bars10` | 21 | 13.6% | -1.6% |
| `sma_trend_confirm_slow_period100_fast_period50` | 9 | 10.8% | -0.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 73/73 runs (mean holdout 33.2%, worst 28.1%, mean DSR 0.129)
- KEEP: `sma_trend_period50` was positive in 73/73 runs (mean holdout 32.7%, worst 25.9%, mean DSR 0.182)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 73/73 runs (mean holdout 32.5%, worst 27.4%, mean DSR 0.345)
- KEEP: `sma_trend_period175` was positive in 73/73 runs (mean holdout 30.9%, worst 25.7%, mean DSR 0.102)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 73/73 runs (mean holdout 30.6%, worst 25.5%, mean DSR 0.381)
- FAMILY `sma_trend` has the best median holdout CAGR (22.8%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (17.6%) - add more parameters to it
- FAMILY `sma_trend_efficiency` has the best median holdout CAGR (15.4%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (13.4%) - add more parameters to it

