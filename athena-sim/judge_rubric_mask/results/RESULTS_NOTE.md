# Results note (written after rating)

Run in PowerShell (hosted API): 404/404 items per judge, not ok 0; cost muse $0.244, haiku $0.732
(total $0.98). Full output: mask_summary.md.

- Discrimination check passes: reference 4.68 vs fixer template 2.18; kappa (overall) on re-rated items 0.67.
- Masking raised graph retrieval for every model (+0.07 to +0.25; 4.40-4.90) and left the full document almost unchanged
  (-0.02 to +0.18).
- Graph vs full document: Gemma 4 26B -0.28 (0/11, Holm 0.006) -> -0.05 (3/5, p 0.73, Holm 1): gap explained by the
  author/date labels. Qwen3.5-9B -0.37 (1/11, Holm 0.032) -> -0.44 (1/11, Holm 0.038): gap remains; its graph comments
  left the Function Objective label empty in 26 of 36 (full document: 0 of 36). GPT-6 Luna +0.54 -> +0.72 (12/0).
  o3-mini, Gemini, DeepSeek stay non-significant.
- Graph vs none: unchanged conclusions (12/0 for five models, DeepSeek 10/2, Holm 0.19).
