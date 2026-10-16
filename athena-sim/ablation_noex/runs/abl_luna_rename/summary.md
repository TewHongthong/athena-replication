# Athena Sim summary

732 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_luna_rename` (test split) was started from freeze `frozen_abl_luna_rename.json` (sha256 233d4b2cd810).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | graph | 366 | 100.0% | 99.5% [98-100] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 1.000 | 100.0% | 4.02 | 217626/61454 | 0.0525 |
| openai:openai/gpt-6-luna | graph_noex | 366 | 100.0% | 92.6% [89-95] | 98.6% | 98.6% [97-99] | 97.9% | 0.0% | 0.990 -> 1.000 | 100.0% | 3.92 | 203289/62737 | 0.0517 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/gpt-6-luna | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |
| openai:openai/gpt-6-luna | graph_noex | 100.0% [126] | 95.9% [123] | 100.0% [117] |

### Paired comparison against `graph` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | graph_noex vs graph | core_ok | 122 | 0 | 2 | 120 | -1.4 | 0.5 | 0.5 |
| openai:openai/gpt-6-luna | graph_noex vs graph | exact_match | 122 | 1 | 11 | 110 | -6.8 | 0.00635 | 0.0127 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
