# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `gemma4_gscs_rename` (test split) was started from freeze `frozen_gemma4_gscs_rename.json` (sha256 7fd8549c608d).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:gemma4:26b | none | 366 | 99.7% | 32.5% [28-37] | 35.8% | 35.8% [31-41] | 36.3% | 3.8% | 0.990 -> 0.994 | - | 2.34 | 194526/59061 | - |
| openai:gemma4:26b | fulldoc | 366 | 100.0% | 92.3% [89-95] | 96.2% | 96.2% [94-98] | 100.0% | 0.0% | 0.990 -> 0.999 | - | 2.52 | 766218/46845 | - |
| openai:gemma4:26b | chunk | 366 | 99.7% | 51.4% [46-56] | 67.2% | 67.2% [62-72] | 85.2% | 0.0% | 0.990 -> 0.992 | - | 2.30 | 361587/53438 | - |
| openai:gemma4:26b | graph | 366 | 100.0% | 89.6% [86-92] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.999 | 100.0% | 1.89 | 242685/48553 | - |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:gemma4:26b | none | 36.5% [126] | 32.5% [123] | 38.5% [117] |
| openai:gemma4:26b | fulldoc | 99.2% [126] | 96.7% [123] | 92.3% [117] |
| openai:gemma4:26b | chunk | 73.0% [126] | 66.7% [123] | 61.5% [117] |
| openai:gemma4:26b | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:gemma4:26b | fulldoc vs none | core_ok | 122 | 79 | 0 | 43 | +60.4 | 3.31e-24 | 1.65e-23 |
| openai:gemma4:26b | chunk vs none | core_ok | 122 | 55 | 12 | 55 | +31.4 | 1.03e-07 | 2.05e-07 |
| openai:gemma4:26b | graph vs none | core_ok | 122 | 83 | 0 | 39 | +64.2 | 2.07e-25 | 1.24e-24 |
| openai:gemma4:26b | fulldoc vs none | exact_match | 122 | 80 | 3 | 39 | +59.8 | 1.97e-20 | 5.92e-20 |
| openai:gemma4:26b | chunk vs none | exact_match | 122 | 45 | 17 | 60 | +18.9 | 0.000497 | 0.000497 |
| openai:gemma4:26b | graph vs none | exact_match | 122 | 76 | 1 | 45 | +57.1 | 1.03e-21 | 4.13e-21 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
