# Review E analyses - results note (exploratory; ADDENDUM.md written before computing)

K1 identifier kind without the original name
- GSCS test (122 units): syntax-only classifier (clang 18 JSON AST, tree-sitter-java, Python ast) matched the
  recorded kind for 114; the 8 others are Python constants (no syntax for constants) -> read as variables.
  Variant B (a name bound once to a literal = constant) matched all 122. Expectation met.
- Worst-case bound for condition (iv) (every trial of a disagreeing unit counted as failure), variant A:
  o3-mini 93.4, Luna 93.4, Qwen 87.2, Gemini 93.4, DeepSeek 92.6, Gemma 93.4 (reported 93.7-100); variant B = reported.
- Public5 test (100 units), benchmark extractor on snippet before/after the injected rename: 7 kind changes caused
  by the name alone (3 Python constants -> field, 3 Python fields -> constant, 1 TypeScript variable -> constant);
  11 excerpts (methods/members outside their class) not analysable alone by the extractor; 1 method excerpt read
  as a function before the rename too. Name-dependent-only bound 92.7-93.0 vs reported 99.7-100.
  Expectation partly met (also fields read as constants, and one TS variable).

K2 BM25 (GSCS test units, section-level hit, top 3): TF-IDF 17.2% (recomputation reproduced all 122 logged
retrievals), BM25 5.7% (k1 1.2 and 1.5 alike). Dense retrieval not evaluated (no embedding model offline).

K4 by rule (GSCS): without the standard 0% on BOOL, FUNC, PROC, TYPE for all six models; CONST 54.5-92.4;
VAR 20.6-66.1. Chunk: CONST 9.1-19.7 (below none), PROC 0-61.1, TYPE 7.4-37.0. Rule selection >= 96% on every
rule for every model except Qwen on VAR (87.3). Ablation: without examples only BOOL drops (o3-mini 52.8,
Luna 86.1, Gemini 83.3; Gemma 100). Post hoc: 295 of 332 chunk failures on constants carried a type prefix.

K5 latency: ontology query 0.019 ms per call (median of 1,000 passes); P50/P95 in results2.md. Median order
agrees with the means except Gemini (chunk P50 1.73 vs selection 1.76 s) and Qwen (none 11.8 vs selection 13.3 s).
