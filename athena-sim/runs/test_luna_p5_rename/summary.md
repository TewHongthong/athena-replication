# Athena Sim summary

1200 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_luna_p5_rename` (test split) was started from freeze `frozen_luna_p5_rename.json` (sha256 51768b6987b5).

## rename - pack `public5`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 300 | 100.0% | 89.0% [85-92] | 100.0% | 99.7% [98-100] | - | 1.7% | 0.985 -> 0.998 | - | 3.81 | 126861/64052 | 0.0447 |
| openai:openai/gpt-6-luna | fulldoc | 300 | 100.0% | 87.0% [83-90] | 100.0% | 100.0% [99-100] | - | 1.0% | 0.985 -> 0.998 | - | 3.28 | 539301/51592 | 0.0797 |
| openai:openai/gpt-6-luna | chunk | 300 | 100.0% | 86.0% [82-89] | 99.0% | 99.0% [97-100] | - | 1.0% | 0.985 -> 0.998 | 90.0% | 3.40 | 182907/52974 | 0.0448 |
| openai:openai/gpt-6-luna | graph | 300 | 100.0% | 88.0% [84-91] | 100.0% | 100.0% [99-100] | - | 1.0% | 0.985 -> 0.998 | 100.0% | 3.10 | 175122/47905 | 0.0415 |

### By language (all core rules ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 100.0% [60] | 100.0% [60] | 98.3% [60] | 100.0% [60] | 100.0% [60] |
| openai:openai/gpt-6-luna | fulldoc | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:openai/gpt-6-luna | chunk | 100.0% [60] | 95.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:openai/gpt-6-luna | graph | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | fulldoc vs none | core_ok | 100 | 1 | 0 | 99 | +0.3 | 1 | 1 |
| openai:openai/gpt-6-luna | chunk vs none | core_ok | 100 | 1 | 1 | 98 | -0.7 | 1 | 1 |
| openai:openai/gpt-6-luna | graph vs none | core_ok | 100 | 1 | 0 | 99 | +0.3 | 1 | 1 |
| openai:openai/gpt-6-luna | fulldoc vs none | exact_match | 100 | 3 | 8 | 89 | -2.0 | 0.227 | 1 |
| openai:openai/gpt-6-luna | chunk vs none | exact_match | 100 | 6 | 8 | 86 | -3.0 | 0.791 | 1 |
| openai:openai/gpt-6-luna | graph vs none | exact_match | 100 | 8 | 9 | 83 | -1.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
