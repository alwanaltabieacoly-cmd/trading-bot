# Replay evaluation results

- replay records read: 89
- pair decisions with forward returns: 445
- generated: 2026-10-17T02:17:53.636594+00:00
- forward returns: 1h candles, 24h and 7d after asof

## source: llm

- decisions: 115 (allow 38, block 77)

| metric | allowed | blocked | always allow |
| --- | --- | --- | --- |
| mean 24h return | -0.18% | 0.37% | 0.19% |
| median 24h return | -0.59% | 0.11% | -0.06% |
| mean 7d return | 2.33% | 0.48% | 1.09% |
| median 7d return | 2.60% | 0.55% | 1.38% |
| hit rate 7d > 0 | 0.605 | 0.571 | 0.583 |

## source: rule

- decisions: 330 (allow 96, block 234)

| metric | allowed | blocked | always allow |
| --- | --- | --- | --- |
| mean 24h return | -0.14% | 0.39% | 0.24% |
| median 24h return | -0.31% | 0.26% | 0.07% |
| mean 7d return | -0.26% | 0.16% | 0.04% |
| median 7d return | -1.41% | -0.35% | -0.62% |
| hit rate 7d > 0 | 0.417 | 0.474 | 0.458 |

