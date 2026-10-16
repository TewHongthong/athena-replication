# Athena Sim summary

732 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_gemini31fl_rename` (test split) was started from freeze `frozen_abl_gemini31fl_rename.json` (sha256 a249db4977ba).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | graph | 366 | 100.0% | 91.5% [88-94] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.999 | 100.0% | 1.53 | 237927/48696 | 0.1325 |
| openai:google/gemini-3.1-flash-lite | graph_noex | 366 | 100.0% | 84.7% [81-88] | 98.4% | 98.4% [96-99] | 97.5% | 0.0% | 0.990 -> 0.999 | 100.0% | 1.56 | 222657/48391 | 0.1283 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |
| openai:google/gemini-3.1-flash-lite | graph_noex | 100.0% [126] | 95.1% [123] | 100.0% [117] |

### Paired comparison against `graph` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | graph_noex vs graph | core_ok | 122 | 0 | 2 | 120 | -1.6 | 0.5 | 0.5 |
| openai:google/gemini-3.1-flash-lite | graph_noex vs graph | exact_match | 122 | 5 | 16 | 101 | -6.8 | 0.0266 | 0.0532 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
