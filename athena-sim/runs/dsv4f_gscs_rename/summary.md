# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `dsv4f_gscs_rename` (test split) was started from freeze `frozen_dsv4f_gscs_rename.json` (sha256 b191480f33e2).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 366 | 56.6% | 29.8% [25-35] | 30.3% | 30.3% [26-35] | 31.6% | 1.4% | 0.990 -> 0.994 | - | 220.75 | 200970/1742068 | - |
| openai:deepseek/deepseek-v4-flash | fulldoc | 366 | 97.0% | 89.6% [86-92] | 96.4% | 96.4% [94-98] | 98.3% | 0.0% | 0.990 -> 0.999 | - | 59.38 | 745579/427880 | - |
| openai:deepseek/deepseek-v4-flash | chunk | 366 | 88.5% | 54.9% [50-60] | 66.9% | 66.9% [62-72] | 89.0% | 0.0% | 0.990 -> 0.993 | - | 108.35 | 358437/840758 | - |
| openai:deepseek/deepseek-v4-flash | graph | 366 | 99.2% | 95.4% [93-97] | 99.2% | 99.2% [98-100] | 98.3% | 0.0% | 0.990 -> 0.999 | 100.0% | 41.52 | 251067/332814 | - |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 31.0% [126] | 32.5% [123] | 27.4% [117] |
| openai:deepseek/deepseek-v4-flash | fulldoc | 97.6% [126] | 97.6% [123] | 94.0% [117] |
| openai:deepseek/deepseek-v4-flash | chunk | 69.8% [126] | 67.5% [123] | 63.2% [117] |
| openai:deepseek/deepseek-v4-flash | graph | 100.0% [126] | 98.4% [123] | 99.1% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | fulldoc vs none | core_ok | 122 | 100 | 0 | 22 | +66.1 | 1.58e-30 | 9.47e-30 |
| openai:deepseek/deepseek-v4-flash | chunk vs none | core_ok | 122 | 76 | 14 | 32 | +36.6 | 1.78e-11 | 3.56e-11 |
| openai:deepseek/deepseek-v4-flash | graph vs none | core_ok | 122 | 101 | 1 | 20 | +68.9 | 4.06e-29 | 2.03e-28 |
| openai:deepseek/deepseek-v4-flash | fulldoc vs none | exact_match | 122 | 94 | 0 | 28 | +59.8 | 1.01e-28 | 4.04e-28 |
| openai:deepseek/deepseek-v4-flash | chunk vs none | exact_match | 122 | 62 | 15 | 45 | +25.1 | 6.08e-08 | 6.08e-08 |
| openai:deepseek/deepseek-v4-flash | graph vs none | exact_match | 122 | 99 | 3 | 20 | +65.6 | 6.98e-26 | 2.09e-25 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
