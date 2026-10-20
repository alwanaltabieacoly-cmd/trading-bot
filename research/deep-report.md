# Deep research report

- Runs analysed: **1**
- Candidates per run: ~100
- Cumulative candidates evaluated: **100**
- Window: 2026-10-20 00:41:09+00:00 -> 2026-10-20 00:41:09+00:00

## Is the search actually working?

- Train-vs-holdout rank correlation: **0.4476** (min 0.4476, max 0.4476, over 1 runs)
- Verdict: **search is informative**

> A correlation near 0 means the backtest ranking carries no information about future performance - the search is noise. Above 0.3 means the search genuinely finds something.

## Strategy families

| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |
|---|---|---|---|---|---|---|---|
| `sma_trend` | 18.0% | 17.4% | -16.5% | 0.155 | 0.202 | 11 | 0 |
| `sma_trend_vol_filter` | 13.6% | 13.0% | -10.5% | 0.119 | 0.503 | 33 | 0 |
| `ema_trend` | 9.4% | 11.1% | -15.2% | 0.119 | 0.155 | 6 | 0 |
| `sma_trend_fast_slow` | 4.8% | 7.9% | -16.5% | 0.127 | 0.187 | 10 | 0 |
| `ema_trend_regime` | 7.1% | 7.4% | -11.2% | 0.057 | 0.128 | 7 | 0 |
| `donchian_trend` | 2.4% | 1.7% | -4.3% | 0.328 | 0.429 | 2 | 0 |
| `donchian_trend_vol_filter` | 1.5% | 0.9% | -3.0% | 0.111 | 0.311 | 2 | 0 |
| `sma_trend_rsi_filter` | -5.2% | -5.7% | -16.8% | 0.036 | 0.097 | 1 | 0 |

## Consistent winners (positive in every run seen)

None yet - not enough runs, or nothing survives every window.

## Repeat overfits

| strategy | times | mean train | mean holdout |
|---|---|---|---|
| `sma_trend_fast_slow_slow_period150_fast_period10` | 1 | 4.9% | -3.0% |
| `sma_trend_fast_slow_slow_period250_fast_period10` | 1 | 7.1% | -7.2% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max70` | 1 | -1.4% | -9.0% |
| `sma_trend_rsi_filter_period150_rsi_period14_rsi_max80` | 1 | 10.5% | -2.5% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max70` | 1 | 0.5% | -5.6% |
| `sma_trend_rsi_filter_period250_rsi_period14_rsi_max80` | 1 | 12.2% | -5.4% |

## What to try next

- FAMILY `sma_trend` has the best median holdout CAGR (17.4%) - add more parameters to it
- FAMILY `sma_trend_vol_filter` has the best median holdout CAGR (13.0%) - add more parameters to it
- FAMILY `ema_trend` has the best median holdout CAGR (11.1%) - add more parameters to it
- FAMILY `sma_trend_fast_slow` has the best median holdout CAGR (7.9%) - add more parameters to it

