# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_luna_gscs_rename` (test split) was started from freeze `frozen_luna_gscs_rename.json` (sha256 868f7634fdd2).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 366 | 100.0% | 43.2% [38-48] | 46.4% | 46.4% [41-52] | 44.7% | 3.0% | 0.990 -> 0.996 | - | 5.56 | 170946/134899 | 0.0845 |
| openai:openai/gpt-6-luna | fulldoc | 366 | 100.0% | 88.8% [85-92] | 99.5% | 99.5% [98-100] | 100.0% | 0.0% | 0.990 -> 0.999 | - | 3.39 | 702378/64160 | 0.1023 |
| openai:openai/gpt-6-luna | chunk | 366 | 100.0% | 56.6% [51-62] | 76.8% | 76.8% [72-81] | 92.8% | 0.0% | 0.990 -> 0.993 | - | 3.67 | 323652/74715 | 0.0697 |
| openai:openai/gpt-6-luna | graph | 366 | 100.0% | 99.5% [98-100] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 1.000 | 100.0% | 3.10 | 217626/60786 | 0.0522 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 57.9% [126] | 44.7% [123] | 35.9% [117] |
| openai:openai/gpt-6-luna | fulldoc | 100.0% [126] | 100.0% [123] | 98.3% [117] |
| openai:openai/gpt-6-luna | chunk | 79.4% [126] | 77.2% [123] | 73.5% [117] |
| openai:openai/gpt-6-luna | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | fulldoc vs none | core_ok | 122 | 72 | 0 | 50 | +53.0 | 4.24e-22 | 2.12e-21 |
| openai:openai/gpt-6-luna | chunk vs none | core_ok | 122 | 64 | 18 | 40 | +30.3 | 3.32e-07 | 6.63e-07 |
| openai:openai/gpt-6-luna | graph vs none | core_ok | 122 | 72 | 0 | 50 | +53.6 | 4.24e-22 | 2.12e-21 |
| openai:openai/gpt-6-luna | fulldoc vs none | exact_match | 122 | 65 | 3 | 54 | +45.6 | 3.56e-16 | 1.07e-15 |
| openai:openai/gpt-6-luna | chunk vs none | exact_match | 122 | 46 | 22 | 54 | +13.4 | 0.0049 | 0.0049 |
| openai:openai/gpt-6-luna | graph vs none | exact_match | 122 | 75 | 0 | 47 | +56.3 | 5.29e-23 | 3.18e-22 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
