# Athena Sim summary

290 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: dev.

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mock:echo | none | 58 | 100.0% | 0.0% [0-6] | 0.0% | 0.0% [0-6] | 0.0% | 0.0% | 0.993 -> 0.993 | - | 0.00 | 0/0 | - |
| mock:echo | fulldoc | 58 | 100.0% | 0.0% [0-6] | 0.0% | 0.0% [0-6] | 0.0% | 0.0% | 0.993 -> 0.993 | - | 0.00 | 0/0 | - |
| mock:echo | chunk | 58 | 100.0% | 0.0% [0-6] | 0.0% | 0.0% [0-6] | 0.0% | 0.0% | 0.993 -> 0.993 | - | 0.00 | 0/0 | - |
| mock:echo | graph | 58 | 100.0% | 0.0% [0-6] | 0.0% | 0.0% [0-6] | 0.0% | 0.0% | 0.993 -> 0.993 | 100.0% | 0.00 | 0/0 | - |
| mock:echo | graph_noex | 58 | 100.0% | 0.0% [0-6] | 0.0% | 0.0% [0-6] | 0.0% | 0.0% | 0.993 -> 0.993 | 100.0% | 0.00 | 0/0 | - |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| mock:echo | none | 0.0% [20] | 0.0% [21] | 0.0% [17] |
| mock:echo | fulldoc | 0.0% [20] | 0.0% [21] | 0.0% [17] |
| mock:echo | chunk | 0.0% [20] | 0.0% [21] | 0.0% [17] |
| mock:echo | graph | 0.0% [20] | 0.0% [21] | 0.0% [17] |
| mock:echo | graph_noex | 0.0% [20] | 0.0% [21] | 0.0% [17] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:echo | fulldoc vs none | core_ok | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | chunk vs none | core_ok | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | graph vs none | core_ok | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | graph_noex vs none | core_ok | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | fulldoc vs none | exact_match | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | chunk vs none | exact_match | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | graph vs none | exact_match | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |
| mock:echo | graph_noex vs none | exact_match | 58 | 0 | 0 | 58 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
