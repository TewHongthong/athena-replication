# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_o3mini_gscs_rename` (test split) was started from freeze `frozen_o3mini_gscs_rename.json` (sha256 77b9f7ecdde6).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | none | 366 | 100.0% | 23.0% [19-28] | 24.3% | 24.3% [20-29] | 20.3% | 2.2% | 0.990 -> 0.988 | - | 5.51 | 170946/235935 | 1.2262 |
| openai:openai/o3-mini | fulldoc | 366 | 100.0% | 78.4% [74-82] | 97.8% | 97.8% [96-99] | 100.0% | 0.0% | 0.990 -> 0.997 | - | 4.86 | 702378/208723 | 1.6910 |
| openai:openai/o3-mini | chunk | 366 | 100.0% | 38.8% [34-44] | 62.6% | 62.6% [58-67] | 86.1% | 0.8% | 0.990 -> 0.990 | - | 5.37 | 323652/228947 | 1.3634 |
| openai:openai/o3-mini | graph | 366 | 100.0% | 85.5% [82-89] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.998 | 100.0% | 4.10 | 217626/180523 | 1.0337 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/o3-mini | none | 30.2% [126] | 21.1% [123] | 21.4% [117] |
| openai:openai/o3-mini | fulldoc | 100.0% [126] | 99.2% [123] | 94.0% [117] |
| openai:openai/o3-mini | chunk | 64.3% [126] | 60.2% [123] | 63.2% [117] |
| openai:openai/o3-mini | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | fulldoc vs none | core_ok | 122 | 103 | 0 | 19 | +73.5 | 1.97e-31 | 1.18e-30 |
| openai:openai/o3-mini | chunk vs none | core_ok | 122 | 73 | 13 | 36 | +38.3 | 2.72e-11 | 5.44e-11 |
| openai:openai/o3-mini | graph vs none | core_ok | 122 | 103 | 0 | 19 | +75.7 | 1.97e-31 | 1.18e-30 |
| openai:openai/o3-mini | fulldoc vs none | exact_match | 122 | 87 | 5 | 30 | +55.5 | 2.1e-20 | 6.31e-20 |
| openai:openai/o3-mini | chunk vs none | exact_match | 122 | 51 | 21 | 50 | +15.8 | 0.000535 | 0.000535 |
| openai:openai/o3-mini | graph vs none | exact_match | 122 | 99 | 1 | 22 | +62.6 | 1.59e-28 | 6.37e-28 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
