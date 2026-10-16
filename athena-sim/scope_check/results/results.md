# Scope-aware name-conflict check (exploratory; see ADDENDUM.md)

Front ends: {"clang": "Ubuntu clang version 18.1.3 (1ubuntu1)", "java": "openjdk version \"21.0.12.1\" 2026-08-18", "python": "3.13.16"}

Trials: 10248; applied (compiled and run in semantic_check): 8898; distinct renames analysed: 1140

## Each check against the compile-and-run outcome (applied trials)

| check | flagged | flagged, behaviour changed | flagged, behaviour unchanged (false alarm) | not flagged, behaviour changed |
|---|---|---|---|---|
| 1 scope-blind collision (frozen) | 81 | 7 | 74 | 0 |
| 2 scope-aware conflict (binding) | 7 | 7 | 0 | 0 |
| 3 scope-aware declaration (IDE-style) | 7 | 7 | 0 | 0 |

## Per model and condition (all 366 trials; not applied = failure)

| Model | Condition | core-rule % | collision-screened (scope-blind) % | scope-screened (check 2) % | core_ok AND pass % | blind flags | check 2 flags |
|---|---|---|---|---|---|---|---|
| o3-mini | none | 24.3 | 24.3 | 24.3 | 24.3 | 8 | 0 |
| o3-mini | fulldoc | 97.8 | 97.8 | 97.8 | 97.8 | 0 | 0 |
| o3-mini | chunk | 62.6 | 62.6 | 62.6 | 62.6 | 3 | 0 |
| o3-mini | graph | 100.0 | 100.0 | 100.0 | 100.0 | 0 | 0 |
| GPT-6 Luna | none | 46.4 | 46.2 | 46.4 | 46.4 | 11 | 0 |
| GPT-6 Luna | fulldoc | 99.5 | 99.5 | 99.5 | 99.5 | 0 | 0 |
| GPT-6 Luna | chunk | 76.8 | 76.8 | 76.8 | 76.8 | 0 | 0 |
| GPT-6 Luna | graph | 100.0 | 100.0 | 100.0 | 100.0 | 0 | 0 |
| Qwen3.5-9B | none | 20.2 | 20.2 | 20.2 | 20.2 | 17 | 0 |
| Qwen3.5-9B | fulldoc | 87.4 | 86.3 | 86.3 | 86.3 | 4 | 4 |
| Qwen3.5-9B | chunk | 47.5 | 46.7 | 46.7 | 46.7 | 8 | 3 |
| Qwen3.5-9B | graph | 93.7 | 93.7 | 93.7 | 93.7 | 0 | 0 |
| Gemini 3.1 Flash-Lite | none | 39.1 | 39.1 | 39.1 | 39.1 | 11 | 0 |
| Gemini 3.1 Flash-Lite | fulldoc | 99.2 | 99.2 | 99.2 | 99.2 | 0 | 0 |
| Gemini 3.1 Flash-Lite | chunk | 68.9 | 68.9 | 68.9 | 68.9 | 0 | 0 |
| Gemini 3.1 Flash-Lite | graph | 100.0 | 100.0 | 100.0 | 100.0 | 0 | 0 |
| DeepSeek V4 Flash | none | 30.3 | 30.3 | 30.3 | 30.3 | 5 | 0 |
| DeepSeek V4 Flash | fulldoc | 96.4 | 96.4 | 96.4 | 96.4 | 0 | 0 |
| DeepSeek V4 Flash | chunk | 66.9 | 66.9 | 66.9 | 66.9 | 0 | 0 |
| DeepSeek V4 Flash | graph | 99.2 | 99.2 | 99.2 | 99.2 | 0 | 0 |
| Gemma 4 26B | none | 35.8 | 35.8 | 35.8 | 35.8 | 14 | 0 |
| Gemma 4 26B | fulldoc | 96.2 | 96.2 | 96.2 | 96.2 | 0 | 0 |
| Gemma 4 26B | chunk | 67.2 | 67.2 | 67.2 | 67.2 | 0 | 0 |
| Gemma 4 26B | graph | 100.0 | 100.0 | 100.0 | 100.0 | 0 | 0 |
| linter autofix | none | 25.4 | 25.4 | 25.4 | 25.4 | 0 | 0 |
| linter autofix | fulldoc | 25.4 | 25.4 | 25.4 | 25.4 | 0 | 0 |
| linter autofix | chunk | 25.4 | 25.4 | 25.4 | 25.4 | 0 | 0 |
| linter autofix | graph | 25.4 | 25.4 | 25.4 | 25.4 | 0 | 0 |

## Every rename flagged by check 2 (distinct unit and suggestion)

| unit | injected -> suggested | trials | outcomes | blind | check 3 | reason |
|---|---|---|---|---|---|---|
| gscs_cpp_004__str_new_name__strip_prefix | new_name -> str_student_name | 3 | {'wrong_output': 3} | True | True | split: ('src', 'FieldDecl', 62) -> ["('src', 'FieldDecl', 62)", "('src', 'ParmVarDecl', 479)"]; merge/capture: ["('src', 'FieldDecl', 62)", "('src', 'ParmVarDec |
| gscs_python_005__str_price_text__camel_no_prefix | priceText -> f_price | 4 | {'wrong_output': 4} | True | True | merge/capture: ["('local', ('FunctionDef', 335), 'f_price')", "('local', ('FunctionDef', 335), 'priceText')"] -> ('local', ('FunctionDef', 335), 'f_price') |

## Scope-blind flags that check 2 does not raise (distinct renames)

| unit | injected -> suggested | trials | name outside comments/strings | check 3 | check 3 reason |
|---|---|---|---|---|---|
| gscs_cpp_001__student_Type__glued_suffix | studentType -> student | 1 | False | False |  |
| gscs_cpp_005__f_value_list__strip_prefix | value_list -> values | 1 | False | False |  |
| gscs_cpp_005__i_value_total__camel_no_prefix | valueTotal -> f_value_total | 1 | False | False |  |
| gscs_java_001__f_credit_total__camel_no_prefix | creditTotal -> credits | 1 | False | False |  |
| gscs_java_001__f_credit_total__strip_prefix | credit_total -> credits | 1 | False | False |  |
| gscs_java_004__Deposit_Money__lower_camel | depositMoney -> deposit | 6 | False | False |  |
| gscs_java_004__d_amount__glued_prefix | dAmount -> amount | 13 | False | False |  |
| gscs_java_004__d_balance__glued_prefix | dBalance -> balance | 23 | False | False |  |
| gscs_java_005__str_text__glued_prefix | strText -> text | 6 | False | False |  |
| gscs_python_001__student_Type__glued_suffix | studentType -> student | 1 | False | False |  |
| gscs_python_002__str_student_name__strip_prefix | student_name -> name | 1 | False | False |  |
| gscs_python_002__str_student_name__strip_prefix | student_name -> student | 1 | False | False |  |
| gscs_python_004__counter_Type__glued_suffix | counterType -> counter | 1 | False | False |  |
| gscs_python_004__i_count_total__strip_prefix | count_total -> count | 1 | False | False |  |
| gscs_python_004__i_step_size__camel_no_prefix | stepSize -> step | 1 | False | False |  |
| gscs_python_004__i_step_size__strip_prefix | step_size -> step | 1 | False | False |  |
| gscs_python_005__f_price__glued_prefix | fPrice -> price | 14 | False | False |  |

Trials by category (where the name occurs, check 3 flag): {"comments/strings only, check3=False": 74}

## Check 3 flags without a check 2 flag: 0 distinct renames, 0 trials

