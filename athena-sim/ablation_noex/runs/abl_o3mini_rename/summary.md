# Athena Sim summary

732 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_o3mini_rename` (test split) was started from freeze `frozen_abl_o3mini_rename.json` (sha256 dea84d09a71a).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | graph | 366 | 100.0% | 86.3% [82-89] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.998 | 100.0% | 5.72 | 217626/179631 | 1.0298 |
| openai:openai/o3-mini | graph_noex | 366 | 100.0% | 80.3% [76-84] | 95.4% | 95.4% [93-97] | 92.8% | 0.0% | 0.990 -> 0.997 | 100.0% | 5.81 | 203289/181949 | 1.0242 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/o3-mini | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |
| openai:openai/o3-mini | graph_noex | 96.8% [126] | 91.9% [123] | 97.4% [117] |

### Paired comparison against `graph` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | graph_noex vs graph | core_ok | 122 | 0 | 8 | 114 | -4.6 | 0.00781 | 0.00781 |
| openai:openai/o3-mini | graph_noex vs graph | exact_match | 122 | 9 | 28 | 85 | -6.0 | 0.00256 | 0.00513 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
