"""Regression check for p5_extra (run from p5_extra/:  python -B regression_check_p5.py). No LLM is called.

The harness here is the ablation_noex copy (llm.py with env-gated options ATHENA_OMIT_TEMP / ATHENA_EXTRA_BODY /
ATHENA_LOG_PROVIDER). For Public5 renaming it must reproduce the frozen GPT-6 Luna test run exactly:
1. the sampled test units (--per-language 20 --seed 42 --split test) equal the 100 units of that run;
2. the prompts of all four conditions equal the logged prompts character for character.
"""
import argparse, collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from athena.packs import load_pack
from athena.retrieval import Retriever
from athena.runner import get_units, make_prompt

CORPUS = os.path.normpath(os.path.join(HERE, "..", "..", "athena-corpus"))
LUNA = os.path.join(HERE, "..", "runs", "test_luna_p5_rename", "trials.jsonl")
pack = load_pack("public5", CORPUS)
ret = Retriever(pack, chunk_k=3, top_k=None, n_examples=2)
args = argparse.Namespace(task="rename", split="test", per_language=20, seed=42, limit=0, languages=None)
units = {u.unit_id: u for u in get_units(pack, args)}
trials = [json.loads(l) for l in open(LUNA, encoding="utf-8")]
run_units = {t["unit_id"] for t in trials}
lines = [f"sampled units {len(units)}, Luna run units {len(run_units)}, identical: {set(units) == run_units}"]
c = collections.Counter()
for t in trials:
    p, _ = make_prompt(pack, ret, "rename", units[t["unit_id"]], t["condition"])
    c[(t["condition"], p == t["prompt"])] += 1
lines.append("prompts: " + ", ".join(f"{k[0]} {'same' if k[1] else 'DIFF'} {v}" for k, v in sorted(c.items())))
ok = set(units) == run_units and not any(not k[1] for k in c)
lines.append("REGRESSION " + ("PASS" if ok else "FAIL"))
print("\n".join(lines))
open(os.path.join(HERE, "regression_check_p5.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
