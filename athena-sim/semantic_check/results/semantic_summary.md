# Semantic preservation of GSCS renames (exploratory; see ADDENDUM.md)

Units excluded by sanity check: 0. Trials scored: 10248.

| Model | Condition | n | applied | build ok % | behavior ok % (applied) | core_ok % | core_ok AND pass % [95% CI] | failures |
|---|---|---|---|---|---|---|---|---|
| o3-mini | none | 366 | 366 | 100.0 | 100.0 | 24.3 | 24.3 [20-29] | - |
| o3-mini | fulldoc | 366 | 366 | 100.0 | 100.0 | 97.8 | 97.8 [96-99] | - |
| o3-mini | chunk | 366 | 366 | 100.0 | 100.0 | 62.6 | 62.6 [58-67] | - |
| o3-mini | graph | 366 | 366 | 100.0 | 100.0 | 100.0 | 100.0 [99-100] | - |
| GPT-6 Luna | none | 366 | 366 | 100.0 | 100.0 | 46.4 | 46.4 [41-52] | - |
| GPT-6 Luna | fulldoc | 366 | 366 | 100.0 | 100.0 | 99.5 | 99.5 [98-100] | - |
| GPT-6 Luna | chunk | 366 | 366 | 100.0 | 100.0 | 76.8 | 76.8 [72-81] | - |
| GPT-6 Luna | graph | 366 | 366 | 100.0 | 100.0 | 100.0 | 100.0 [99-100] | - |
| Qwen3.5-9B | none | 366 | 354 | 100.0 | 100.0 | 20.2 | 20.2 [16-25] | - |
| Qwen3.5-9B | fulldoc | 366 | 349 | 100.0 | 98.9 | 87.4 | 86.3 [82-89] | wrong_output 4 |
| Qwen3.5-9B | chunk | 366 | 361 | 100.0 | 99.2 | 47.5 | 46.7 [42-52] | wrong_output 3 |
| Qwen3.5-9B | graph | 366 | 364 | 100.0 | 100.0 | 93.7 | 93.7 [91-96] | - |
| Gemini 3.1 Flash-Lite | none | 366 | 362 | 100.0 | 100.0 | 39.1 | 39.1 [34-44] | - |
| Gemini 3.1 Flash-Lite | fulldoc | 366 | 366 | 100.0 | 100.0 | 99.2 | 99.2 [98-100] | - |
| Gemini 3.1 Flash-Lite | chunk | 366 | 365 | 100.0 | 100.0 | 68.9 | 68.9 [64-73] | - |
| Gemini 3.1 Flash-Lite | graph | 366 | 366 | 100.0 | 100.0 | 100.0 | 100.0 [99-100] | - |
| DeepSeek V4 Flash | none | 366 | 207 | 100.0 | 100.0 | 30.3 | 30.3 [26-35] | - |
| DeepSeek V4 Flash | fulldoc | 366 | 355 | 100.0 | 100.0 | 96.4 | 96.4 [94-98] | - |
| DeepSeek V4 Flash | chunk | 366 | 324 | 100.0 | 100.0 | 66.9 | 66.9 [62-72] | - |
| DeepSeek V4 Flash | graph | 366 | 363 | 100.0 | 100.0 | 99.2 | 99.2 [98-100] | - |
| Gemma 4 26B | none | 366 | 365 | 100.0 | 100.0 | 35.8 | 35.8 [31-41] | - |
| Gemma 4 26B | fulldoc | 366 | 366 | 100.0 | 100.0 | 96.2 | 96.2 [94-98] | - |
| Gemma 4 26B | chunk | 366 | 365 | 100.0 | 100.0 | 67.2 | 67.2 [62-72] | - |
| Gemma 4 26B | graph | 366 | 366 | 100.0 | 100.0 | 100.0 | 100.0 [99-100] | - |
| linter autofix | none | 366 | 93 | 100.0 | 100.0 | 25.4 | 25.4 [21-30] | - |
| linter autofix | fulldoc | 366 | 93 | 100.0 | 100.0 | 25.4 | 25.4 [21-30] | - |
| linter autofix | chunk | 366 | 93 | 100.0 | 100.0 | 25.4 | 25.4 [21-30] | - |
| linter autofix | graph | 366 | 93 | 100.0 | 100.0 | 25.4 | 25.4 [21-30] | - |

Paired exact sign tests on per-unit means of core_ok AND pass (Holm across all 12):

| Model | graph vs | mean diff (pp) | units better | units worse | p | Holm p |
|---|---|---|---|---|---|---|
| o3-mini | none | +75.7 | 103 | 0 | 1.97e-31 | 2.17e-30 |
| o3-mini | fulldoc | +2.2 | 5 | 0 | 0.0625 | 0.229 |
| GPT-6 Luna | none | +53.6 | 72 | 0 | 4.24e-22 | 2.96e-21 |
| GPT-6 Luna | fulldoc | +0.5 | 2 | 0 | 0.5 | 1 |
| Qwen3.5-9B | none | +73.5 | 109 | 0 | 3.08e-33 | 3.7e-32 |
| Qwen3.5-9B | fulldoc | +7.4 | 27 | 13 | 0.0385 | 0.192 |
| Gemini 3.1 Flash-Lite | none | +60.9 | 83 | 0 | 2.07e-25 | 1.86e-24 |
| Gemini 3.1 Flash-Lite | fulldoc | +0.8 | 2 | 0 | 0.5 | 1 |
| DeepSeek V4 Flash | none | +68.9 | 101 | 1 | 4.06e-29 | 4.06e-28 |
| DeepSeek V4 Flash | fulldoc | +2.7 | 11 | 3 | 0.0574 | 0.229 |
| Gemma 4 26B | none | +64.2 | 83 | 0 | 2.07e-25 | 1.86e-24 |
| Gemma 4 26B | fulldoc | +3.8 | 6 | 0 | 0.0312 | 0.188 |

## Notes
- core_ok rates reproduce Table 2 of the manuscript exactly for all six LLMs and the autofix baseline, so the same trials were scored.
- Every applied rename compiled (build ok 100% in every cell). 822 distinct programs were built and run; harness checks: 12/12 seed programs run, 113/113 violation programs reproduce the golden output, negative controls (collision, keyword, builtin shadowing) fail as expected.
- All 7 behavior failures are Qwen3.5-9B under full document (4) or chunk retrieval (3), and all 7 were core_ok: the name follows the standard but silently changes behavior.
  - gscs_cpp_004: parameter new_name -> str_student_name, the class field's name; the parameter shadows the field, so Set_Name assigns the parameter to itself and the field stays empty.
  - gscs_python_005: parameter priceText -> f_price, an existing local; the local overwrites the parameter before it is read, so every price parses as 0.0.
  The frozen collision metric flags these names, but core_ok does not, so compliance alone overstates these 7 trials.
- Graph retrieval produced no behavior-changing rename for any model.
- Harness detail: C++ programs are prefixed with `#define private public` so the driver can read a private field (gscs_cpp_004); Java reads the private field of gscs_java_004 by reflection.
