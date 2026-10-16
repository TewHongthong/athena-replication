# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `gemma4_gscs_comment` (test split) was started from freeze `frozen_gemma4_gscs_comment.json` (sha256 484c991bd385).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:gemma4:26b | none | 36 | 100.0% | 0.0% [0-10] | 0.0% | - | 100.0% | 0.326 | 2.73 | 15132/7512 |
| openai:gemma4:26b | fulldoc | 36 | 100.0% | 100.0% [90-100] | 100.0% | 97.7% | 100.0% | 0.634 | 3.90 | 71364/9036 |
| openai:gemma4:26b | chunk | 36 | 100.0% | 83.3% [68-92] | 83.3% | 87.8% | 100.0% | 0.603 | 3.15 | 30393/8319 |
| openai:gemma4:26b | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 83.3% | 100.0% | 0.659 | 2.97 | 24384/8046 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:gemma4:26b | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:gemma4:26b | fulldoc | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| openai:gemma4:26b | chunk | 100.0% [12] | 75.0% [12] | 75.0% [12] |
| openai:gemma4:26b | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:gemma4:26b | none | cpp | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | none | java | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | none | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | fulldoc | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | fulldoc | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | fulldoc | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | chunk | java | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | chunk | python | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:gemma4:26b | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:gemma4:26b | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |
| openai:gemma4:26b | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +83.3 | 0.00195 | 0.00195 |
| openai:gemma4:26b | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
