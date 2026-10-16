# Athena Sim summary

180 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_gemma4or_comment` (test split) was started from freeze `frozen_abl_gemma4or_comment.json` (sha256 d41d5b4d278f).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 36 | 100.0% | 0.0% [0-10] | 0.0% | - | 100.0% | 0.328 | 5.79 | 15132/7498 |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 36 | 100.0% | 100.0% [90-100] | 100.0% | 98.6% | 100.0% | 0.649 | 6.30 | 71364/8787 |
| openai:google/gemma-4-26b-a4b-it | chunk | 36 | 100.0% | 83.3% [68-92] | 83.3% | 87.2% | 100.0% | 0.602 | 6.26 | 30393/8404 |
| openai:google/gemma-4-26b-a4b-it | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 84.3% | 100.0% | 0.659 | 4.97 | 24384/8144 |
| openai:google/gemma-4-26b-a4b-it | graph_noex | 36 | 100.0% | 100.0% [90-100] | 100.0% | 100.0% | 100.0% | 0.639 | 5.62 | 19164/8610 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:google/gemma-4-26b-a4b-it | fulldoc | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| openai:google/gemma-4-26b-a4b-it | chunk | 100.0% [12] | 75.0% [12] | 75.0% [12] |
| openai:google/gemma-4-26b-a4b-it | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| openai:google/gemma-4-26b-a4b-it | graph_noex | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | none | cpp | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | none | java | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | none | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | fulldoc | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | fulldoc | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | fulldoc | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | chunk | java | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | chunk | python | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph_noex | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph_noex | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemma-4-26b-a4b-it | graph_noex | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemma-4-26b-a4b-it | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00195 |
| openai:google/gemma-4-26b-a4b-it | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +83.3 | 0.00195 | 0.00195 |
| openai:google/gemma-4-26b-a4b-it | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00195 |
| openai:google/gemma-4-26b-a4b-it | graph_noex vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00195 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
