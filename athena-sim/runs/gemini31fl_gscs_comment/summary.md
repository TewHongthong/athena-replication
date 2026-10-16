# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `gemini31fl_gscs_comment` (test split) was started from freeze `frozen_gemini31fl_gscs_comment.json` (sha256 fc2a84a22387).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 36 | 97.2% | 0.0% [0-10] | 0.0% | - | 97.2% | 0.343 | 2.20 | 14271/6687 |
| openai:google/gemini-3.1-flash-lite | fulldoc | 36 | 94.4% | 94.4% [82-98] | 100.0% | 95.1% | 94.4% | 0.622 | 2.05 | 66991/7057 |
| openai:google/gemini-3.1-flash-lite | chunk | 36 | 100.0% | 83.3% [68-92] | 83.3% | 92.8% | 100.0% | 0.614 | 2.41 | 29925/7547 |
| openai:google/gemini-3.1-flash-lite | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 83.3% | 100.0% | 0.653 | 3.07 | 23916/7978 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:google/gemini-3.1-flash-lite | fulldoc | 100.0% [12] | 91.7% [12] | 91.7% [12] |
| openai:google/gemini-3.1-flash-lite | chunk | 100.0% [12] | 75.0% [12] | 75.0% [12] |
| openai:google/gemini-3.1-flash-lite | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | cpp | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | none | java | 12 | 0.0% [0-24] [12] | 91.7% | 100.0% |
| openai:google/gemini-3.1-flash-lite | none | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | fulldoc | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | fulldoc | java | 12 | 91.7% [65-99] [12] | 91.7% | 100.0% |
| openai:google/gemini-3.1-flash-lite | fulldoc | python | 12 | 91.7% [65-99] [12] | 91.7% | 100.0% |
| openai:google/gemini-3.1-flash-lite | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | chunk | java | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | chunk | python | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:google/gemini-3.1-flash-lite | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +94.4 | 0.000488 | 0.00146 |
| openai:google/gemini-3.1-flash-lite | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +83.3 | 0.00195 | 0.00195 |
| openai:google/gemini-3.1-flash-lite | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
