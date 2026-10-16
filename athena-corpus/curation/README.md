# Athena Task C curation (corpus -> benchmark)

Turns the 792 raw corpus files (`../corpus/`) into `../benchmark/snippets/<lang>/*.json` and
`../benchmark/violations/<lang>/*.json` following `benchmark_schema.md`. No LLM is used anywhere; every step is
deterministic (two runs give byte-identical files). Results and caveats: `../benchmark/curation_report.md`.

## Files

| File | Role |
|---|---|
| `curate.py` | main pipeline (parse -> gate -> pick targets -> inject + verify rename -> select -> write) |
| `rules.py` | ontology reader, the `CORE` rule table (which NamingRules gate/target which kinds), `EXCLUDED` rules with reasons |
| `lang_python.py` | Python extractor (stdlib `ast` + `tokenize`) |
| `lang_ts.py` | Java / C# / TypeScript(+TSX) / JavaScript(+JSX) extractors (tree-sitter) |
| `tsbind.py`, `tools/build_treesitter.sh` | tiny ctypes binding + script that builds the tree-sitter library from pinned GitHub commits |
| `facts.py` | shared data model |
| `validate_benchmark.py` | independent validator, **standard library only** (runs on any machine, no parsers needed) |
| `syntax_check.py` | every snippet and violated context parses standalone (needs the tree-sitter library) |
| `make_comment_units.py` | builds the comment-generation units (Task C, RQ2) in `../benchmark/comment_units/` from the curated snippets plus, where a language has fewer than 30 qualifying snippets, extra units mined from the 792-file corpus |
| `validate_comment_units.py` | independent validator for `comment_units/`, **standard library only** (skips the tree-sitter-dependent `expectedElements` re-check when the library is unavailable) |
| `make_report.py` | regenerates `../benchmark/curation_report.md` from `curation_stats.json` |
| `pipeline/` | vendored copies of the project's `violation_injector.py`, `output_validator.py`, `graph_loader.py`, `graph_rag.py` and the ontology used |

Vendored copies (from the project's ontology and pipeline folder; the ontology is the newer 206,806-byte version):

| File | sha256 (first 16) |
|---|---|
| `pipeline/violation_injector.py` | `f939131cc09a78c4…` |
| `pipeline/output_validator.py` | `d154237dfca677ea…` |
| `pipeline/graph_loader.py` | `a4b1b62954bb3baa…` |
| `pipeline/graph_rag.py` | `ac87c33552a180fa…` |
| `pipeline/athena_ontology.json` | `716026bb9e8fa0a6…` |

## Check the delivered benchmark (any machine, Python 3.10+)

```
cd athena-corpus/curation
python validate_benchmark.py --benchmark ../benchmark --corpus ..
```

## Re-run from scratch (Linux / WSL; needs git, gcc, network to github.com)

```
cd athena-corpus/curation
bash tools/build_treesitter.sh                      # writes libtsall.so here (pinned commits)
python curate.py --corpus .. --out ../benchmark_rerun --per-language 100
python validate_benchmark.py --benchmark ../benchmark_rerun --corpus ..
python syntax_check.py --benchmark ../benchmark_rerun
diff -r ../benchmark/snippets ../benchmark_rerun/snippets   # expect no differences
```

`pip install tree-sitter tree-sitter-java ...` (py-tree-sitter) was not available in the build session (PyPI/npm blocked),
which is why the library is built from source; an adapter for py-tree-sitter would be straightforward but has not been written or tested.

## Tuning knobs (top of `curate.py`)

`MIN_LINES`/`MAX_LINES` (6/40), `MAX_TARGETS` (6 identifiers per snippet), `MIN_TARGET_LEN` (3), `--per-language` (100).
Change the rule policy in `rules.py` (`CORE`, `rules_for_check`, `name_for_check`); the start-up check refuses a `CORE` entry the ontology cannot retrieve.

## Comment units (Task C, RQ2)

```
cd athena-corpus/curation
python make_comment_units.py --corpus .. --out ../benchmark      # writes benchmark/comment_units/
python validate_comment_units.py --benchmark ../benchmark --corpus ..
```

Deterministic, no LLM. One unit per qualifying snippet (kind `function`/`method`/`class` only;
`interface`/`enum`/`const`/`constructor` are skipped) plus, for languages with fewer than 30 such
units, extra units mined directly from the 792-file corpus (`origin: "extra"`, id `cx_<lang>_NNN`,
deterministic selection order, capped at 2 per file / 25% per repo / 40 per language). The
reference comment is read from the **pinned corpus file**, not the already-dedented snippet text,
since for every language but Python the doc comment sits above the snippet's own line range
(Python's docstring is the unit's first body statement, so it comes from the snippet's own
`codeContext`). `signature`/`expectedElements` (params/returns/throws) are inferred from the code
itself (`ast` for Python, tree-sitter elsewhere), never from the comment, so grading can tell a void
method apart from one that must document a return value. See `curation_report.md` for counts,
rejection reasons and known gaps (several CommentRule formats have no mechanical check at all).
