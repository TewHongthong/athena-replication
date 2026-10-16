# Athena Sim summary

1200 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `p5x_gemini31fl_p5_rename` (test split) was started from freeze `frozen_p5x_gemini31fl_p5_rename.json` (sha256 7dca9c8e57da).

## rename - pack `public5`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 300 | 100.0% | 80.7% [76-85] | 100.0% | 100.0% [99-100] | - | 0.7% | 0.985 -> 0.997 | - | 1.85 | 139164/34243 | 0.0862 |
| openai:google/gemini-3.1-flash-lite | fulldoc | 300 | 100.0% | 88.3% [84-91] | 100.0% | 100.0% [99-100] | - | 0.0% | 0.985 -> 0.998 | - | 2.02 | 561144/37454 | 0.1965 |
| openai:google/gemini-3.1-flash-lite | chunk | 300 | 100.0% | 82.7% [78-87] | 100.0% | 100.0% [99-100] | - | 0.0% | 0.985 -> 0.997 | 90.0% | 1.80 | 196734/35421 | 0.1023 |
| openai:google/gemini-3.1-flash-lite | graph | 300 | 100.0% | 86.0% [82-89] | 100.0% | 100.0% [99-100] | - | 0.0% | 0.985 -> 0.998 | 100.0% | 1.85 | 188397/35871 | 0.1009 |

### By language (all core rules ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemini-3.1-flash-lite | fulldoc | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemini-3.1-flash-lite | chunk | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:google/gemini-3.1-flash-lite | graph | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | fulldoc vs none | core_ok | 100 | 0 | 0 | 100 | +0.0 | 1 | 1 |
| openai:google/gemini-3.1-flash-lite | chunk vs none | core_ok | 100 | 0 | 0 | 100 | +0.0 | 1 | 1 |
| openai:google/gemini-3.1-flash-lite | graph vs none | core_ok | 100 | 0 | 0 | 100 | +0.0 | 1 | 1 |
| openai:google/gemini-3.1-flash-lite | fulldoc vs none | exact_match | 100 | 16 | 6 | 78 | +7.7 | 0.0525 | 0.315 |
| openai:google/gemini-3.1-flash-lite | chunk vs none | exact_match | 100 | 11 | 5 | 84 | +2.0 | 0.21 | 0.84 |
| openai:google/gemini-3.1-flash-lite | graph vs none | exact_match | 100 | 14 | 6 | 80 | +5.3 | 0.115 | 0.577 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
