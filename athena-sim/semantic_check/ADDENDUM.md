# Addendum (post-freeze, exploratory): semantic preservation of GSCS renames

Written after the frozen GSCS test runs finished and before any compile/test scoring of their outputs.
This analysis is NOT part of the frozen HYPOTHESES.md. It is exploratory and must be reported as such.
It re-scores outputs that already exist; no model is called again and no frozen file is changed.

## Motivation
Advisor recommendation: define the metrics and run test programs. The frozen evaluation checks the proposed
name against the standard (core_ok) but never runs the code after the rename (Table 5 construct threat).

## Scope
- Pack GSCS, task rename, split test: 12 seed snippets (cpp/java/python 001, 002, 004, 005), 122 units.
- Runs (all trials, 4 conditions x 3 repeats = 1,464 each): o3-mini, GPT-6 Luna, Qwen3.5-9B, Gemini 3.1 Flash-Lite,
  DeepSeek V4 Flash (dsv4f_v2 bundle), Gemma 4 26B, and the linter-autofix baseline.
- Public5 is out of scope: its snippets are excerpts that do not compile on their own.

## Procedure
1. One deterministic test driver per seed, written from the seed code only (no model output consulted). It calls the
   seed's functions with fixed inputs covering both branches and prints the results.
2. program_orig = prelude + seed + driver (Java: driver class first). golden = stdout of program_orig.
3. program_viol = apply_rename(program_orig, original, injected), using athena.evaluate.apply_rename (the same
   whole-word rename used for the Similarity Index). Sanity: program_viol must compile and reproduce golden;
   units that fail sanity are excluded and listed.
4. For each trial whose suggestion is a valid identifier different from the injected name ("applied"):
   program_after = apply_rename(program_viol, injected, suggested). Build (g++ -std=c++17; Java 11 single-file
   source launcher; python3 -m py_compile), run with a 10 s timeout.
   Outcome: pass (exit 0 and stdout == golden), compile_error, runtime_error, wrong_output, timeout.
   Trials with no valid or no changed suggestion are "not_applied" (the editor would leave the code unchanged).

## Metrics (per model x condition)
- build_ok and behavior_ok: share of applied trials that compile / pass.
- compliant_and_preserved: core_ok AND pass, over ALL trials (not_applied counts as false).
- Rates with Wilson 95% CIs.

## Analysis
- Exact two-sided sign test on per-unit means (over 3 repeats) of compliant_and_preserved:
  graph vs none and graph vs fulldoc, for each of the 6 LLMs; Holm correction across these 12 tests.
- Everything here is exploratory and secondary to the single confirmatory test in HYPOTHESES.md.

## Frozen before scoring
```
c1fc135150c5c593  run_semantic.py
49eb67cc14e8a48e  drivers/gscs_cpp_001.cpp
d7530e3f9840f88c  drivers/gscs_cpp_002.cpp
8e102404ac3d7c2b  drivers/gscs_cpp_004.cpp
5d06d0e759db1347  drivers/gscs_cpp_005.cpp
d2c3ba5bee4f74a5  drivers/gscs_java_001.java
f1a8b356cb2d171c  drivers/gscs_java_002.java
780aa1879f1d5374  drivers/gscs_java_004.java
7aabe4b3cd6ce6b0  drivers/gscs_java_005.java
dae79a91242dab7d  drivers/gscs_python_001.py
976bb77239c10c74  drivers/gscs_python_002.py
4d20a1af0b12204e  drivers/gscs_python_004.py
a18312bce4e902f4  drivers/gscs_python_005.py
```

## Script revised before scoring any model output
Added an execution cache, 2 parallel workers and time-budgeted resumable runs (Java 11 single-file runs take ~2.6 s each). Procedure, metrics and analysis unchanged. Golden + sanity done: 12/12 seeds run, 113/113 violation programs reproduce golden.
```
30fa4c88a8ddd7ce  run_semantic.py
```
Negative controls (collision, keyword, builtin shadowing) fail as expected: compile_error x3, runtime_error x1; a benign rename passes.
