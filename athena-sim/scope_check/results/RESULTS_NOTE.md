# Scope-aware check: results note (after scoring)

- Front ends: clang 18.1.3 (C++), javac/OpenJDK 21 compiler Tree API (Java), Python 3.13 ast + symtable.
  Run in the cloud workspace (no package registry on the device; clang only there); inputs were the 122 GSCS test
  violation units, `semantic_check/results/trial_results.csv`, and the rename function of `athena/evaluate.py`
  (bundle `_inputs.tar.gz`). No model called; no frozen file changed.
- Controls (before scoring): fresh-name rename of all 122 units -> 0 flags; 13/13 hand-made conflicts flagged.
- 8,898 applied trials, 1,140 distinct renames:
  - check 1 scope-blind collision (frozen): 81 flags = 7 behaviour changes + 74 false alarms (reproduces phase5).
  - check 2 scope-aware binding check: 7 flags = exactly the 7 behaviour changes (Qwen3.5-9B; gscs_cpp_004
    new_name -> str_student_name x3, parameter captures field; gscs_python_005 priceText -> f_price x4, parameter
    merged with local); 0 false alarms; 0 misses.
  - check 3 IDE-style declaration check: the same 7, nothing else.
- All 74 scope-blind false alarms (17 distinct renames) are names that occur in the snippet only inside comments
  (e.g. balance, amount, text, price in the header comment). Because each case-study snippet holds one function or
  class, this case study cannot separate the scope-aware check from a textual check that ignores comments and
  strings (which would flag the same 7); the difference would show only with same-named identifiers in other scopes.
- Per model x condition, compliance screened by check 2 equals "core_ok AND pass" in all 28 cells; graph retrieval:
  0 flags for every model.
