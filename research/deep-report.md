# Deep research report

- Runs analysed: **3**
- Candidates per run: ~100
- Cumulative candidates evaluated: **300**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-20 01:15:38+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.4476** (min 0.4476, max 0.4476, over 3 runs)
- Verdict: **search is informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.0% | 17.4% | -16.5% | 0.155 | 0.202 | 33 | 0 |
| `sma_trend_vol_filter` | 13.6% | 13.0% | -10.5% | 0.119 | 0.503 | 99 | 0 |
| `ema_trend` | 9.4% | 11.1% | -15.2% | 0.119 | 0.155 | 18 | 0 |
| `sma_trend_fast_slow` | 4.8% | 7.9% | -16.5% | 0.127 | 0.187 | 30 | 0 |
| `ema_trend_regime` | 7.1% | 7.4% | -11.2% | 0.057 | 0.128 | 21 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.328 | 0.429 | 6 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.111 | 0.311 | 6 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 3 | 0 |

## Consistent winners (positive in every run seen)

| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |
|---|---|---|---|---|---|---|
| `sma_trend_period200` | 3 | 3 | 28.1% | 28.1% | 0.145 | 9.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` | 3 | 3 | 27.4% | 27.4% | 0.372 | 8.0 |
| `sma_trend_period50` | 3 | 3 | 25.9% | 25.9% | 0.202 | 8.0 |
| `sma_trend_period175` | 3 | 3 | 25.7% | 25.7% | 0.115 | 8.0 |
| `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` | 3 | 3 | 25.5% | 25.5% | 0.408 | 7.0 |
| `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct3.0` | 3 | 3 | 25.0% | 25.0% | 0.099 | 9.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct3.0` | 3 | 3 | 24.5% | 24.5% | 0.426 | 10.0 |
| `sma_trend_period225` | 3 | 3 | 23.1% | 23.1% | 0.142 | 9.0 |
| `sma_trend_vol_filter_period225_vol_lookback30_vol_max_pct4.0` | 3 | 3 | 22.7% | 22.7% | 0.388 | 8.0 |
| `sma_trend_vol_filter_period100_vol_lookback30_vol_max_pct4.0` | 3 | 3 | 20.8% | 20.8% | 0.444 | 9.0 |

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period150_fast_period10` | 3 | 4.9% | -3.0% |
| `sma_trend_fast_slow_slow_period250_fast_period10` | 3 | 7.1% | -7.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 3 | -1.4% | -9.0% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 3 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max70` | 3 | 0.5% | -5.6% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max80` | 3 | 12.2% | -5.4% |

## What to try next

- KEEP: `sma_trend_period200` was positive in 3/3 runs (mean holdout 28.1%, worst 28.1%, mean DSR 0.145)
- KEEP: `sma_trend_vol_filter_period200_vol_lookback30_vol_max_pct4.0` was positive in 3/3 runs (mean holdout 27.4%, worst 27.4%, mean DSR 0.372)
- KEEP: `sma_trend_period50` was positive in 3/3 runs (mean holdout 25.9%, worst 25.9%, mean DSR 0.202)
- KEEP: `sma_trend_period175` was positive in 3/3 runs (mean holdout 25.7%, worst 25.7%, mean DSR 0.115)
- KEEP: `sma_trend_vol_filter_period175_vol_lookback30_vol_max_pct4.0` was positive in 3/3 runs (mean holdout 25.5%, worst 25.5%, mean DSR 0.408)
- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.1%) - add more parameters to it
- FAMILY `sma_trend_fast_slow` has the best median holdout CAGR (7.9%) - add more parameters to it

