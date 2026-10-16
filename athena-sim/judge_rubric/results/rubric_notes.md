# Notes on the rubric results (see rubric_summary.md and ../ADDENDUM.md)

Run: hosted API, 1,962 items per judge, 0 failed or unparsed calls, strict JSON schema used throughout.
Cost: muse (Muse Glimmer 30B) $1.12; haiku (Claude Haiku 4.5) $3.57; total $4.69.

Validity checks
- Discrimination: GSCS reference 4.79 vs linter-autofix floor 1.81 -> PASS.
- Agreement (quadratic-weighted kappa / exact / within 1): overall 0.52 / 61.7% / 99.2%; conformance 0.78; completeness 0.54;
  clarity 0.49; accuracy 0.23 with 87.4% exact agreement (low kappa because almost every comment scores 5 on accuracy).
- Public5 developer comments score 3.80 overall, below the generated ones (4.6-4.7): they are terse (completeness 2.96).
  They are a ceiling on GSCS only, not on Public5.

Findings (GSCS, 12 units; exploratory)
- Graph vs no standard: overall +0.98 to +1.31 (of 5) for all six models; 12/12 units better for five models (Holm p = 0.007);
  DeepSeek 10 better / 2 worse (Holm p = 0.19; its unanswered condition-(i) trials count as 1).
  Most of the gain is conformance (about 1.0 -> 3.7-4.4) and completeness; accuracy stays 4.6-5.0 in every condition.
- Graph reaches 4.33-4.71 overall, close to the reference comments (4.79).
- Graph vs full document is mixed: better for GPT-6 Luna (+0.54, 12/0, Holm 0.007), worse for Gemma 4 26B (-0.28, 0/11, Holm 0.008)
  and Qwen3.5-9B (-0.37, 1/11, Holm 0.038), no significant difference for o3-mini, Gemini 3.1 Flash-Lite and DeepSeek V4 Flash.
- Why graph trails full document for Gemma and Qwen: their graph comments keep every required label but leave some empty
  (Function Objective, Created By, Create Date); with the full document they copy the template's sample values. The judges
  penalised empty author/date labels although the rubric exempts them, so part of this gap is judge strictness on metadata.
- Public5 (GPT-6 Luna): all conditions 4.62-4.70; graph vs full document -0.08 (Holm 0.038), negligible in size.
