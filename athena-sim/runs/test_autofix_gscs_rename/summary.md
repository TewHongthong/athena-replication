# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: test.

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mock:autofix | none | 366 | 100.0% | 18.9% [15-23] | 25.4% | 25.4% [21-30] | 0.0% | 0.0% | 0.990 -> 0.995 | - | 0.00 | 0/0 | - |
| mock:autofix | fulldoc | 366 | 100.0% | 18.9% [15-23] | 25.4% | 25.4% [21-30] | 0.0% | 0.0% | 0.990 -> 0.995 | - | 0.00 | 0/0 | - |
| mock:autofix | chunk | 366 | 100.0% | 18.9% [15-23] | 25.4% | 25.4% [21-30] | 0.0% | 0.0% | 0.990 -> 0.995 | - | 0.00 | 0/0 | - |
| mock:autofix | graph | 366 | 100.0% | 18.9% [15-23] | 25.4% | 25.4% [21-30] | 0.0% | 0.0% | 0.990 -> 0.995 | 100.0% | 0.00 | 0/0 | - |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| mock:autofix | none | 21.4% [126] | 29.3% [123] | 25.6% [117] |
| mock:autofix | fulldoc | 21.4% [126] | 29.3% [123] | 25.6% [117] |
| mock:autofix | chunk | 21.4% [126] | 29.3% [123] | 25.6% [117] |
| mock:autofix | graph | 21.4% [126] | 29.3% [123] | 25.6% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:autofix | fulldoc vs none | core_ok | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |
| mock:autofix | chunk vs none | core_ok | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |
| mock:autofix | graph vs none | core_ok | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |
| mock:autofix | fulldoc vs none | exact_match | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |
| mock:autofix | chunk vs none | exact_match | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |
| mock:autofix | graph vs none | exact_match | 122 | 0 | 0 | 122 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
