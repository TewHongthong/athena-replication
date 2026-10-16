# Athena Sim summary

1068 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_luna_p5_comment` (test split) was started from freeze `frozen_luna_p5_comment.json` (sha256 c8cb1a7e07b9).

## comment - pack `public5`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 267 | 99.6% | 99.6% [98-100] | - | - | 99.6% | 0.277 | 7.18 | 111351/149464 |
| openai:openai/gpt-6-luna | fulldoc | 267 | 100.0% | 98.8% [97-100] | - | - | 100.0% | 0.287 | 5.58 | 480066/112901 |
| openai:openai/gpt-6-luna | chunk | 267 | 100.0% | 99.6% [98-100] | - | - | 99.6% | 0.272 | 6.06 | 164307/123922 |
| openai:openai/gpt-6-luna | graph | 267 | 100.0% | 99.6% [98-100] | - | - | 100.0% | 0.300 | 4.77 | 162135/92609 |

### By language (structure ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 98.5% [66] | 100.0% [39] | 100.0% [6] | 100.0% [81] | 100.0% [66] |
| openai:openai/gpt-6-luna | fulldoc | 98.5% [66] | 94.9% [39] | 100.0% [6] | 100.0% [81] | 100.0% [66] |
| openai:openai/gpt-6-luna | chunk | 100.0% [66] | 97.4% [39] | 100.0% [6] | 100.0% [81] | 100.0% [66] |
| openai:openai/gpt-6-luna | graph | 100.0% [66] | 97.4% [39] | 100.0% [6] | 100.0% [81] | 100.0% [66] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | csharp | 66 | 98.5% [92-100] [66] | 98.5% | 0.0% |
| openai:openai/gpt-6-luna | none | java | 39 | 100.0% [91-100] [39] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | none | javascript | 9 | 100.0% [61-100] [6] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | none | python | 84 | 100.0% [95-100] [81] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | none | typescript | 69 | 100.0% [94-100] [66] | 100.0% | 4.3% |
| openai:openai/gpt-6-luna | fulldoc | csharp | 66 | 98.5% [92-100] [66] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | fulldoc | java | 39 | 94.9% [83-99] [39] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | fulldoc | javascript | 9 | 100.0% [61-100] [6] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | fulldoc | python | 84 | 100.0% [95-100] [81] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | fulldoc | typescript | 69 | 100.0% [94-100] [66] | 100.0% | 4.3% |
| openai:openai/gpt-6-luna | chunk | csharp | 66 | 100.0% [94-100] [66] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | chunk | java | 39 | 97.4% [87-100] [39] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | chunk | javascript | 9 | 100.0% [61-100] [6] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | chunk | python | 84 | 100.0% [95-100] [81] | 98.8% | 100.0% |
| openai:openai/gpt-6-luna | chunk | typescript | 69 | 100.0% [94-100] [66] | 100.0% | 4.3% |
| openai:openai/gpt-6-luna | graph | csharp | 66 | 100.0% [94-100] [66] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | graph | java | 39 | 97.4% [87-100] [39] | 100.0% | 0.0% |
| openai:openai/gpt-6-luna | graph | javascript | 9 | 100.0% [61-100] [6] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | graph | python | 84 | 100.0% [95-100] [81] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | graph | typescript | 69 | 100.0% [94-100] [66] | 100.0% | 4.3% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | fulldoc vs none | comment_ok | 86 | 1 | 2 | 83 | -0.8 | 1 | 1 |
| openai:openai/gpt-6-luna | chunk vs none | comment_ok | 86 | 1 | 1 | 84 | +0.0 | 1 | 1 |
| openai:openai/gpt-6-luna | graph vs none | comment_ok | 86 | 1 | 1 | 84 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
