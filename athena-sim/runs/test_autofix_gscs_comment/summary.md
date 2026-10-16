# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: test.

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| mock:autofix | none | 36 | 100.0% | 100.0% [90-100] | 100.0% | 0.0% | 100.0% | 0.539 | 0.00 | 0/0 |
| mock:autofix | fulldoc | 36 | 100.0% | 100.0% [90-100] | 100.0% | 0.0% | 100.0% | 0.539 | 0.00 | 0/0 |
| mock:autofix | chunk | 36 | 100.0% | 100.0% [90-100] | 100.0% | 0.0% | 100.0% | 0.539 | 0.00 | 0/0 |
| mock:autofix | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 0.0% | 100.0% | 0.539 | 0.00 | 0/0 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| mock:autofix | none | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| mock:autofix | fulldoc | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| mock:autofix | chunk | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| mock:autofix | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| mock:autofix | none | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | none | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | none | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | fulldoc | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | fulldoc | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | fulldoc | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | chunk | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | chunk | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| mock:autofix | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:autofix | fulldoc vs none | comment_ok | 12 | 0 | 0 | 12 | +0.0 | 1 | 1 |
| mock:autofix | chunk vs none | comment_ok | 12 | 0 | 0 | 12 | +0.0 | 1 | 1 |
| mock:autofix | graph vs none | comment_ok | 12 | 0 | 0 | 12 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
