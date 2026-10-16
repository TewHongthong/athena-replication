# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `dsv4f_gscs_comment` (test split) was started from freeze `frozen_dsv4f_gscs_comment.json` (sha256 cfffc847bc16).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 36 | 77.8% | 0.0% [0-10] | 0.0% | - | 72.2% | 0.249 | 102.43 | 15341/139711 |
| openai:deepseek/deepseek-v4-flash | fulldoc | 36 | 91.7% | 86.1% [71-94] | 97.0% | 78.9% | 91.7% | 0.547 | 83.06 | 68427/110238 |
| openai:deepseek/deepseek-v4-flash | chunk | 36 | 100.0% | 77.8% [62-88] | 80.6% | 76.7% | 97.2% | 0.572 | 70.90 | 29293/93793 |
| openai:deepseek/deepseek-v4-flash | graph | 36 | 91.7% | 91.7% [78-97] | 100.0% | 75.3% | 91.7% | 0.579 | 97.03 | 24612/120391 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:deepseek/deepseek-v4-flash | fulldoc | 100.0% [12] | 91.7% [12] | 66.7% [12] |
| openai:deepseek/deepseek-v4-flash | chunk | 100.0% [12] | 66.7% [12] | 66.7% [12] |
| openai:deepseek/deepseek-v4-flash | graph | 100.0% [12] | 100.0% [12] | 75.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | cpp | 12 | 0.0% [0-24] [12] | 75.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | none | java | 12 | 0.0% [0-24] [12] | 66.7% | 100.0% |
| openai:deepseek/deepseek-v4-flash | none | python | 12 | 0.0% [0-24] [12] | 75.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | fulldoc | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | fulldoc | java | 12 | 91.7% [65-99] [12] | 91.7% | 100.0% |
| openai:deepseek/deepseek-v4-flash | fulldoc | python | 12 | 66.7% [39-86] [12] | 83.3% | 100.0% |
| openai:deepseek/deepseek-v4-flash | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | chunk | java | 12 | 66.7% [39-86] [12] | 100.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | chunk | python | 12 | 66.7% [39-86] [12] | 91.7% | 100.0% |
| openai:deepseek/deepseek-v4-flash | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:deepseek/deepseek-v4-flash | graph | python | 12 | 75.0% [47-91] [12] | 75.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +86.1 | 0.000488 | 0.00146 |
| openai:deepseek/deepseek-v4-flash | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +77.8 | 0.00195 | 0.00195 |
| openai:deepseek/deepseek-v4-flash | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +91.7 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
