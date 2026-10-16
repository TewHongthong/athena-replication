# Athena Sim summary

1200 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `p5x_gemma4or_p5_rename` (test split) was started from freeze `frozen_p5x_gemma4or_p5_rename.json` (sha256 db8b8a1a6c35).

## rename - pack `public5`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 300 | 100.0% | 87.7% [83-91] | 100.0% | 100.0% [99-100] | - | 1.0% | 0.985 -> 0.998 | - | 3.18 | 143115/32613 | 0.0132 |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 300 | 100.0% | 90.0% [86-93] | 100.0% | 100.0% [99-100] | - | 1.0% | 0.985 -> 0.998 | - | 4.20 | 565095/37820 | 0.0321 |
| openai:google/gemma-4-26b-a4b-it | chunk | 300 | 100.0% | 88.7% [85-92] | 98.0% | 98.0% [96-99] | - | 1.0% | 0.985 -> 0.998 | 90.0% | 3.82 | 200685/36779 | 0.0165 |
| openai:google/gemma-4-26b-a4b-it | graph | 300 | 99.7% | 91.3% [88-94] | 99.7% | 99.7% [98-100] | - | 1.0% | 0.985 -> 0.999 | 100.0% | 3.86 | 192348/38408 | 0.0165 |

### By language (all core rules ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemma-4-26b-a4b-it | chunk | 100.0% [60] | 90.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemma-4-26b-a4b-it | graph | 98.3% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | fulldoc vs none | core_ok | 100 | 0 | 0 | 100 | +0.0 | 1 | 1 |
| openai:google/gemma-4-26b-a4b-it | chunk vs none | core_ok | 100 | 0 | 2 | 98 | -2.0 | 0.5 | 1 |
| openai:google/gemma-4-26b-a4b-it | graph vs none | core_ok | 100 | 0 | 1 | 99 | -0.3 | 1 | 1 |
| openai:google/gemma-4-26b-a4b-it | fulldoc vs none | exact_match | 100 | 6 | 4 | 90 | +2.3 | 0.754 | 1 |
| openai:google/gemma-4-26b-a4b-it | chunk vs none | exact_match | 100 | 7 | 6 | 87 | +1.0 | 1 | 1 |
| openai:google/gemma-4-26b-a4b-it | graph vs none | exact_match | 100 | 7 | 3 | 90 | +3.7 | 0.344 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
