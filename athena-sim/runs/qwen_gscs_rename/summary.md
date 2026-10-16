# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `qwen_gscs_rename` (test split) was started from freeze `frozen_qwen_gscs_rename.json` (sha256 67915cf24ab4).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | none | 366 | 97.5% | 13.4% [10-17] | 20.2% | 20.2% [16-25] | 13.1% | 4.6% | 0.990 -> 0.987 | - | 12.95 | 184119/70611 | - |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | 366 | 96.2% | 51.9% [47-57] | 87.4% | 87.4% [84-90] | 94.1% | 1.1% | 0.990 -> 0.994 | - | 24.38 | 738975/68843 | - |
| openai:Qwen3.5-9B-Q4_K_M | chunk | 366 | 98.6% | 30.3% [26-35] | 47.5% | 47.5% [42-53] | 63.7% | 2.2% | 0.990 -> 0.988 | - | 17.45 | 344682/65838 | - |
| openai:Qwen3.5-9B-Q4_K_M | graph | 366 | 99.7% | 60.9% [56-66] | 93.7% | 93.7% [91-96] | 86.5% | 0.0% | 0.990 -> 0.997 | 100.0% | 13.09 | 231660/58283 | - |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | none | 23.0% [126] | 22.8% [123] | 14.5% [117] |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | 90.5% [126] | 87.0% [123] | 84.6% [117] |
| openai:Qwen3.5-9B-Q4_K_M | chunk | 54.0% [126] | 38.2% [123] | 50.4% [117] |
| openai:Qwen3.5-9B-Q4_K_M | graph | 97.6% [126] | 91.1% [123] | 92.3% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | fulldoc vs none | core_ok | 122 | 102 | 0 | 20 | +67.2 | 3.94e-31 | 1.97e-30 |
| openai:Qwen3.5-9B-Q4_K_M | chunk vs none | core_ok | 122 | 61 | 22 | 39 | +27.3 | 2.18e-05 | 4.36e-05 |
| openai:Qwen3.5-9B-Q4_K_M | graph vs none | core_ok | 122 | 109 | 0 | 13 | +73.5 | 3.08e-33 | 1.85e-32 |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc vs none | exact_match | 122 | 73 | 5 | 44 | +38.5 | 1.5e-16 | 4.49e-16 |
| openai:Qwen3.5-9B-Q4_K_M | chunk vs none | exact_match | 122 | 44 | 17 | 61 | +16.9 | 0.00073 | 0.00073 |
| openai:Qwen3.5-9B-Q4_K_M | graph vs none | exact_match | 122 | 88 | 3 | 31 | +47.5 | 1.02e-22 | 4.06e-22 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
