# ADDENDUM — rubric sensitivity with non-inferable label values masked (review D #9)

Written before any judge call for this analysis. Exploratory sensitivity analysis of RQ2 (comment content).
No comment is regenerated; frozen runs and the original ratings in ../judge_rubric are not changed.

## Why
In the original rating (../judge_rubric, Table 5), graph retrieval scored below the full document for Gemma 4 26B
(-0.28) and Qwen3.5-9B (-0.37). With the full document these models copied the template's sample values into the
GSCS header labels, while with graph retrieval they left some labels empty; the judges penalised empty author/date
labels although the rubric exempts them. This analysis removes that difference.

## What changes (only this)
- In every GSCS comment (six LLMs, all conditions, rule-based fixer template, developer reference comments), the
  value of each of the four labels the code cannot reveal — Created By, Create Date, Revised By, Revised Date
  (case-insensitive; also "Created by", "Creation Date", "Revision Date") — is replaced by the fixed token
  "[not inferable from code]" (build_masked.py). Missing labels stay missing (presence is a rule requirement);
  comment terminators are never touched (checked: 0 mismatches). 702 of 1,020 GSCS rows change; the rest
  (mostly no-standard comments without the template) are byte-identical.
- Judge input is otherwise identical to the original: same judges (muse = Meta Muse Glimmer 30B, haiku = Claude
  Haiku 4.5), same judge.py (byte-identical copy, sha256 3ce4f634...), same rubric text (which already allows
  placeholders in these labels), same settings; only the cost caps in judges.json differ.
- Re-rated: the 404 masked items whose text changed and that occur under none, full document, graph retrieval, the
  developer reference, or the fixer template (items_to_rate.jsonl). Rows whose comment did not change keep their
  original ratings (identical input). Chunk retrieval is not re-rated (not part of the paper's rubric tests).
- Estimated cost from the original run: about $0.24 (muse) + $0.73 (haiku); caps $0.50 and $1.20.

## Analysis (aggregate_mask.py), fixed now
- Overall score as before: mean of the four criteria and the two judges; trials without a comment score 1.
- Per model x condition: original vs masked overall, conformance, completeness.
- Paired exact sign tests on per-unit mean overall score, graph vs none and graph vs full document, six models,
  Holm across these 12 GSCS tests (the original analysis used 14 tests including 2 on Public5; unit = program here,
  one comment unit per program). Reported for original and masked scores side by side.
- Checks: reference > fixer template (discrimination), weighted kappa between judges on re-rated items.
- Reporting: the masked result is a sensitivity analysis next to the original Table 5, not a replacement; if the
  graph-vs-full-document differences for Gemma/Qwen shrink or reverse, Section 5.2 says so; if not, it says the
  difference is not explained by the author/date labels.

## sha256 (before rating)
- items.jsonl 8459aa199e7d1ef5e360d9ec29da1238d25629332d307bc924c742a47080a82e
- item_map.jsonl 22a4231f364633b64c5e7c9989b23ccb0ad8f3ae26bb36576ffcb5b45ef0a0d4
- items_to_rate.jsonl 77965e173609c6aae69f6950c04113b611449ba6d9c3dfd00a8043f4ed01ba3c
- judge.py 3ce4f634b2a421167ad34265787df300907c7690289f003caa455f8104d04b77
- judges.json c0297d1f442e94580915f3942315aa20578096bc6a2dec8ebc67a5586734a41f
- build_masked.py ff460c13c49392f037ddd84c0a7b8d8188b99dbbb7bff887bb4a9eaf1dbabb2d
- aggregate_mask.py 62c878ffc22db2704ce66644f74b3470971d8fe5817f4a7ef3b7651b922311ce
Pipeline dry-run with the mock judge (random scores): results/_dryrun_* (not results).
