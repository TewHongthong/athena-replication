# Addendum (post-freeze, exploratory): review E analyses K1, K2, K4, K5

Written before any result below was computed. Prompted by
review E (`Athena_Research_Review_and_Recommendations.md`, items 6, 7, 14, 15 of its roadmap). Exploratory, not
part of HYPOTHESES.md. No model is called and no frozen file, run or score is changed; everything is computed
offline from the existing benchmark files and trial logs.

## K1 - identifier kind inferred without the original name (review item 6, "oracle-like metadata")
Question: condition (iv) is keyed on the identifier kind recorded in the benchmark. Would the kind, and hence the
rules retrieved, be the same if the kind were inferred from the code the model is shown (which carries the
injected, non-compliant name)?

GSCS (test split, 122 units). Name-blind classifier, rules fixed here. The declaration of the injected name in
`codeContextWithViolation` is found with a language front end (C++: `clang++ -std=c++17 -fsyntax-only -Xclang
-ast-dump=json`; Java: tree-sitter-java through the benchmark's own `curation/tsbind.py`; Python: `ast`), and:
- type declaration (class, struct, interface, enum) -> class
- function or method: declared return type `void` (C++/Java), or in Python no `return <expr>` whose value is not
  `None` -> procedure; otherwise function
- parameter -> parameter (whatever its type)
- member variable of a class (C++/Java field; Python `self.<name>` assignment): declared `const`/`constexpr`
  (C++) or `final` (Java) -> constant; declared type `bool`/`boolean` -> boolean_variable; otherwise field
- other variable: `const`/`constexpr` (C++) or `final` (Java) -> constant; declared `bool`/`boolean` ->
  boolean_variable; Python: if every value bound to the name is a bool literal, a comparison, a `not`, or an
  `and`/`or` of these -> boolean_variable; otherwise variable. Python has no constant declaration, so variant A
  never returns constant for Python.
- Variant B (secondary): variant A plus a Python convention heuristic: a name bound exactly once in its scope, to
  a numeric, string, tuple or list literal, and never rebound -> constant.

Measures: kind accuracy (exact match with the recorded kind) with a confusion table; retrieval agreement (the
predicted kind maps to the same core-rule set as the recorded kind; this is what decides the prompt, since
parameter, variable and field share one GSCS rule). End-to-end bounds for condition (iv), per model: a unit with
retrieval agreement receives the identical prompt, so its logged trials stand; for a unit without agreement the
lower bound counts its trials as failures and the upper bound keeps them (= reported value). No re-run here.

Public5 (test split, 100 units, secondary). The benchmark's own extraction code (`curation/curate.analyze`) is
run on the snippet before and after the injected rename (`athena.evaluate.apply_rename`), and the kind at the
target's declaration is compared; agreement on core rules via `pack.core_rules`; bounds as above for the four
Public5 models. If a snippet does not parse on its own, it is dedented first; if it still fails, it is reported.

Expectations (stated before computing): on GSCS, disagreements fall on the Python constants (8 test units), so
the end-to-end lower bound for (iv) lies about 6-7 points below the reported value; variant B recovers some of
them; C++ and Java agree almost everywhere. On Public5, disagreements only on Python constants (3 units).

## K2 - BM25 retrieval hit rate on GSCS (review item 7)
Same chunks and same query tokens as condition (iii) (`athena/retrieval.py`: `words()`; query = language +
kind x3 + injected name x2 + code). Okapi BM25 with k1 = 1.2, b = 0.75 (k1 = 1.5 as sensitivity), top 3, ties
by chunk order. Measure: section-level hit as in phase9_stats 9.5 (every source section of the unit's core rules
among the top 3), per unit, since retrieval is deterministic. Sanity check first: the TF-IDF index recomputed
with the same code must reproduce the logged `retrieved_ids` of every chunk trial. Dense embedding retrieval is
not evaluated: no embedding model is available offline in either environment (no package-registry access).
Expectation: BM25 hit rate of the same order as TF-IDF (17.2% of units), far below 100%.

## K4 - compliance by rule and by language (review item 15)
GSCS test, six models, conditions (i)-(iv) (and (v) for the four ablation models): core-rule compliance grouped
by the violated rule (six rules) and by language. Descriptive only, no tests.

## K5 - latency distribution (review items 14, 20)
GSCS renaming: P50 and P95 of the logged per-call `latency_s`, by model x condition; retrieval time of
condition (iv) measured by timing `Retriever.context` over the 122 test units (1,000 repetitions, median per
call) on the user's machine. Descriptive.

Outputs: `review_e/results.md`, `review_e/results.json`. Any change to the rules above after the first
computation is recorded below.

## Recorded after the first computation
- K4 showed chunk retrieval below no standard on the constant rule. An extra descriptive check was added after
  seeing this (so it is post hoc): among chunk-condition failures on GSCS-CONST-UPPER units, the share whose
  proposed name starts with a GSCS type prefix (regex ^(i|f|d|str|bln|c|l|s|b|arr|lst|ch|n)_ , case-insensitive).
  Script: review_e/const_prefix.py. No other rule above was changed.
- After a blind pre-submission check of the manuscript, one more descriptive count was
  added (post hoc): which GSCS document sections condition (iii) retrieved, from the logged retrieved_ids of the
  o3-mini chunk trials (retrieval is deterministic, so per unit): Naming Variables 91/122 units, Naming Constants 2,
  Naming Boolean variables 4, Naming Types 1. No rule above was changed.
