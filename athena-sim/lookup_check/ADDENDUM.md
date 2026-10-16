# ADDENDUM — graph retrieval vs structured lookup (Phase 1, task 1.2)

Written before running the comparison. Post-freeze, exploratory. No LLM is called and no
trial is re-scored: this check only regenerates the CODING STANDARD block of the prompt.

## Question
Does Athena's "graph" condition retrieve anything that a flat lookup table keyed by
(standard, language, identifier kind, task) would not? (Review feedback: "why a graph?")

## Method (fixed before running)
1. Flatten each ontology JSON (GSCS pack; Public5 `athena-corpus/curation/pipeline/athena_ontology.json`)
   into a table, one row per rule: type, standard, languages, identifier kinds, severity, check fields,
   examples (in file order). Written to `rule_table_<pack>.json`, plus a precomputed index
   `lookup_<pack>.json`: key "standard|language|kind|task" -> ordered rule ids.
   Order = severity (MUST > SHOULD > MAY), then number of specific fields, then rule id
   (the same ordering the graph retriever states in Section 3.6). Task types: rename -> NamingRule;
   comment -> CommentRule (+ StructureRule in GSCS, as the retriever does).
   Examples: up to 2 per rule, compliant/non-compliant interleaved (same cap as the frozen runs).
   The lookup code reads the JSON directly and does not use the `Ontology` class or any graph edge walk.
2. Render each looked-up rule with the same `render_rule()` text template (formatting, not retrieval)
   and the same header lines as the graph condition.
3. Units: every TEST unit of GSCS rename (122), GSCS comment (12), Public5 rename (100),
   Public5 comment (89).
4. Compare the lookup block against (a) the CODING STANDARD block of the prompt actually logged in
   `trials.jsonl` for the graph condition (GPT-6 Luna runs: all four sets; o3-mini runs: GSCS),
   and (b) the live `Retriever.context("graph")`.
   Report per set: % units with the same rule set, same order, same examples, identical text
   (character for character), and the number of distinct lookup keys the units fall into.
5. Separately, record which edge relations the retriever reads and which relations exist in each
   ontology file (code inspection + edge counts).

## Reporting
Result goes to Phase 2 (framing) of the revision plan. If the blocks are identical, the paper states that
retrieval reduces to a keyed lookup over the ontology and reframes the contribution accordingly.

## Extension (after the first run, before the manuscript edit)
The first run covered the logged prompts of GPT-6 Luna and o3-mini only. To support the manuscript's statement that
every LLM receives identical retrieved context, the same comparison is repeated on the logged graph-condition prompts
of the other four GSCS runs (Qwen3.5-9B, Gemini 3.1 Flash-Lite, DeepSeek V4 Flash `dsv4f_v2`, Gemma 4 26B), using
the unchanged functions of `lookup_compare.py` (`lookup_allmodels.py` → `results_allmodels.md`). Still no LLM call or scoring.
