# Athena Sim summary

1830 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_gemma4or_rename` (test split) was started from freeze `frozen_abl_gemma4or_rename.json` (sha256 e0dfd139fd72).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 366 | 98.4% | 32.2% [28-37] | 33.9% | 33.9% [29-39] | 38.0% | 3.6% | 0.990 -> 0.993 | - | 3.98 | 194526/59086 | 0.0212 |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 366 | 100.0% | 91.8% [89-94] | 95.9% | 95.9% [93-98] | 100.0% | 0.0% | 0.990 -> 0.999 | - | 3.48 | 766218/47892 | 0.0427 |
| openai:google/gemma-4-26b-a4b-it | chunk | 366 | 100.0% | 51.4% [46-56] | 66.9% | 66.9% [62-72] | 86.9% | 0.0% | 0.990 -> 0.992 | - | 3.70 | 361587/53963 | 0.0271 |
| openai:google/gemma-4-26b-a4b-it | graph | 366 | 100.0% | 91.3% [88-94] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.999 | 100.0% | 3.07 | 242685/49238 | 0.0210 |
| openai:google/gemma-4-26b-a4b-it | graph_noex | 366 | 100.0% | 88.8% [85-92] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.999 | 100.0% | 3.07 | 227415/49862 | 0.0205 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 39.7% [126] | 33.3% [123] | 28.2% [117] |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 99.2% [126] | 97.6% [123] | 90.6% [117] |
| openai:google/gemma-4-26b-a4b-it | chunk | 69.8% [126] | 67.5% [123] | 63.2% [117] |
| openai:google/gemma-4-26b-a4b-it | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |
| openai:google/gemma-4-26b-a4b-it | graph_noex | 100.0% [126] | 100.0% [123] | 100.0% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | fulldoc vs none | core_ok | 122 | 85 | 0 | 37 | +62.0 | 5.17e-26 | 3.1e-25 |
| openai:google/gemma-4-26b-a4b-it | chunk vs none | core_ok | 122 | 63 | 11 | 48 | +33.1 | 5.32e-10 | 1.06e-09 |
| openai:google/gemma-4-26b-a4b-it | graph vs none | core_ok | 122 | 88 | 0 | 34 | +66.1 | 6.46e-27 | 5.17e-26 |
| openai:google/gemma-4-26b-a4b-it | graph_noex vs none | core_ok | 122 | 88 | 0 | 34 | +66.1 | 6.46e-27 | 5.17e-26 |
| openai:google/gemma-4-26b-a4b-it | fulldoc vs none | exact_match | 122 | 86 | 4 | 32 | +59.6 | 4.32e-21 | 1.3e-20 |
| openai:google/gemma-4-26b-a4b-it | chunk vs none | exact_match | 122 | 50 | 15 | 57 | +19.1 | 1.57e-05 | 1.57e-05 |
| openai:google/gemma-4-26b-a4b-it | graph vs none | exact_match | 122 | 83 | 1 | 38 | +59.0 | 8.79e-24 | 4.39e-23 |
| openai:google/gemma-4-26b-a4b-it | graph_noex vs none | exact_match | 122 | 80 | 1 | 41 | +56.6 | 6.78e-23 | 2.71e-22 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
