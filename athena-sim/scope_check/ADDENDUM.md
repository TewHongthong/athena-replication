# Addendum (post-freeze, exploratory): scope-aware name-conflict check on GSCS renames

Written before any scope-aware result was computed. Prompted by review feedback
(reviewer 3, item 5): the frozen collision flag is scope-blind, and all 7 behaviour-changing renames found by
`semantic_check/` were core-rule compliant. Exploratory, not part of HYPOTHESES.md. No model is called and no
frozen file or score is changed; the check is applied offline to suggestions that already exist. Because the
validator only gives a verdict (it never rejects or re-prompts), applying the check offline gives the same
verdicts as re-running the pipeline with the check inside the validator.

## Scope
- GSCS renaming, test split: 12 seed snippets, 122 units; the 10,248 trials of `semantic_check/results/trial_results.csv`
  (6 LLMs + linter autofix x 4 conditions x 3 repeats). Analysed: the 8,898 "applied" trials (valid identifier
  different from the injected name), the same set that was compiled and run.
- Code analysed: the unit's `codeContextWithViolation` (the snippet the model and the validator see), not the
  test driver. Public5 is out of scope (no behaviour ground truth).

## Checks (static, on the snippet; parser: tree-sitter grammars for C++, Java, Python; versions recorded in results)
1. Scope-blind collision (frozen, `athena/evaluate.py`): suggested name occurs as a whole word anywhere in the
   snippet, comments and strings included. Recomputed here and checked against the 81 flags (74 + 7) of
   `phase5_stats/results_collision.md`.
2. Scope-aware conflict (primary). Scopes: file/module, class body, function or method (parameters + body), and in
   C++/Java blocks (compound statements, for/catch headers). Declarations: types, fields, methods/functions,
   parameters, local variables and constants; Python also assignment targets (function-level, no block scope),
   for/with/except targets, imports, and `self.<attr>` assignments as attributes of the enclosing class.
   Name resolution: C++/Java innermost enclosing scope, locals visible from their declaration on, class members
   visible in all member functions (implicit this), `this.x`/`this->x` resolved in the class; Python LEGB
   (class body not visible from methods; `self.x` resolved in the class attribute namespace).
   Unqualified identifiers that resolve to no declaration in the snippet bind to "external" (library or builtin).
   A rename injected -> suggested is a conflict if, after the rename, (a) two declarations of the suggested name
   share one scope (Python: one namespace), or (b) any identifier occurrence binds to a different declaration
   than before (the renamed declaration counts as the same declaration), including capture of an external name,
   or (c) the suggested name is a reserved word of the language, or the snippet no longer parses to the same
   identifier sequence. Member accesses on other objects (`obj.x`, `s.size()`) are not resolved and are counted.
3. Scope-aware declaration check (secondary, IDE-style, more conservative): conflict if the suggested name is
   declared, other than by the renamed declarations, in the scope of a renamed declaration, in a scope enclosing
   it (C++/Java: class scope encloses methods; Python: not), or in a scope nested inside it, or is a reserved word,
   or is an external name used inside that scope.

## Measures
- Contingency of each check against the compile-and-run outcome (pass vs wrong_output/compile_error/runtime_error):
  caught behaviour changes (of 7), false alarms (flag but pass), and the remaining flags.
- Per model x condition: core-rule compliant AND no scope-aware conflict, over all 366 trials (not applied =
  failure), next to "core_ok AND pass" from `semantic_check/` and the scope-blind collision-screened compliance.
- Every flag of check 2 is listed with its reason, so it can be inspected by hand.

## Expectations (stated before computing)
- Check 2 flags all 7 behaviour-changing renames (gscs_cpp_004: parameter renamed to the field it shadows;
  gscs_python_005: parameter renamed to an existing local) and fewer than the 74 scope-blind false alarms,
  because most of those are expected to be names that occur only in comments or in another function.
- Check 3 flags at least as many trials as check 2.
- If check 2 misses a behaviour change, that is reported as is and the miss explained; the check is not tuned
  after seeing results. Any change to the rules above after the first computation is recorded below with a time.

## Change before computing
tree-sitter could not be installed (no package-registry access in either environment), so no result has been
computed with it. Check 2 instead uses the languages' own front ends, which resolve names by the language rules
rather than by the simplified rules above: C++ = clang 18 `-fsyntax-only -Xclang -ast-dump=json` (DeclRefExpr /
MemberExpr -> referenced declaration), Java = javac compiler Tree API after attribution (Trees.getElement on
identifiers and member selects), Python = ast + symtable (stdlib). Criterion for check 2, unchanged in intent:
align every name occurrence (declarations and references) of the snippet before and after the rename by source
position; the rename is a conflict if the front end reports an error after the rename (but not before), or if the
mapping from before-declarations to after-declarations over all aligned occurrences is not one-to-one (a
reference captured by another declaration, or two declarations merged). C++ type references inside declarations
are not occurrences in the clang JSON dump; they are covered only through the compile check. Check 3 uses the same
front-end output for scopes and declarations. Controls before scoring model output: (i) renaming every unit's
injected name to a fresh name must give no conflict; (ii) hand-made collisions (the frozen negative controls of
semantic_check plus field shadowing and local merging) must be flagged.

## Controls passed, before scoring any model output
Positive control: all 122 units renamed to a fresh name -> 0 flags (check 2 and check 3). Negative controls: 13 of
13 flagged by check 2 (field shadowing C++/Java, local redeclaration/merge C++/Java/Python, builtin capture in
Python, attribute merged with a method in Python, keywords in all three languages, a local shadowing Math in Java).
One control initially named the Python method as addCount, which is the name in another unit's variant; the test
seed's method is Add_Count, so the control was corrected to Add_Count (analyser unchanged). Scoring follows.
