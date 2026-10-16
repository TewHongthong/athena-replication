"""Original vs masked rubric scores on GSCS (see ADDENDUM.md):  python aggregate_mask.py [--judges muse haiku]"""
import argparse, json, math, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ORIG = os.path.join(os.path.dirname(HERE), "judge_rubric")
sys.path.insert(0, ORIG)
from aggregate import qwk, sign_p, holm  # same helpers as the original analysis
CRIT = ["accuracy", "completeness", "clarity", "conformance"]
CONDS = ["none", "fulldoc", "chunk", "graph"]
MODELS = ["o3-mini", "GPT-6 Luna", "Qwen3.5-9B", "Gemini 3.1 Flash-Lite", "DeepSeek V4 Flash", "Gemma 4 26B"]


def load(path):
    d = {}
    if os.path.exists(path):
        for l in open(path, encoding="utf-8"):
            r = json.loads(l)
            if r.get("ok"): d[r["item"]] = r["scores"]
    return d


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--judges", nargs="+", default=["muse", "haiku"])
    ap.add_argument("--orig-judges", nargs="+", default=None); a = ap.parse_args()
    oj = a.orig_judges or a.judges
    J0 = {k: load(os.path.join(ORIG, "results", f"judgments_{k}.jsonl")) for k in oj}
    J1 = {k: load(os.path.join(HERE, "results", f"judgments_{k}.jsonl")) for k in a.judges}
    rows = [json.loads(l) for l in open(os.path.join(HERE, "item_map.jsonl"), encoding="utf-8")]
    rerate = {json.loads(l)["id"] for l in open(os.path.join(HERE, "items_to_rate.jsonl"), encoding="utf-8")}

    def sc(J, keys, item):
        rs = [J[k][item] for k in keys if item in J[k]]
        if not rs: return None
        s = {c: sum(r[c] for r in rs) / len(rs) for c in CRIT}; s["overall"] = sum(s[c] for c in CRIT) / 4
        return s

    ONE = {c: 1.0 for c in CRIT + ["overall"]}
    per = {"original": defaultdict(list), "masked": defaultdict(list)}; unit = {"original": defaultdict(list), "masked": defaultdict(list)}
    missing = 0
    for r in rows:
        if r["item"] is None:
            s0 = s1 = ONE
        else:
            s0 = sc(J0, oj, r["orig_item"])
            s1 = sc(J1, a.judges, r["item"]) if r["item"] in rerate else s0
            if s0 is None or s1 is None: missing += 1; continue
        for mode, s in (("original", s0), ("masked", s1)):
            per[mode][(r["source"], r["condition"])].append(s)
            unit[mode][(r["source"], r["condition"], r["unit"])].append(s["overall"])
    rated = {k: sum(1 for i in rerate if i in J1[k]) for k in a.judges}
    L = ["# Rubric sensitivity: non-inferable label values masked (GSCS; exploratory, see ADDENDUM.md)", "",
         f"Re-rated items: {len(rerate)}; rated so far: {rated}; rows missing a score: {missing}", ""]
    if len(a.judges) >= 2:
        k1, k2 = a.judges[:2]; both = [i for i in rerate if i in J1[k1] and i in J1[k2]]
        x = [round(sum(J1[k1][i].values()) / 4) for i in both]; y = [round(sum(J1[k2][i].values()) / 4) for i in both]
        L += [f"Judge agreement on re-rated items (overall, quadratic-weighted kappa): {qwk(x, y):.2f} (n = {len(both)})", ""]
    m = lambda v, c: sum(s[c] for s in v) / len(v) if v else float("nan")
    ref = m(per["masked"][("reference", "reference")], "overall"); flo = m(per["masked"][("linter autofix", "graph")], "overall")
    L += [f"Discrimination check (masked): reference {ref:.2f} vs rule-based fixer template {flo:.2f} -> "
          + ("PASS" if ref > flo else "FAIL"), "",
          "| Source | Condition | n | overall original | overall masked | diff | conformance orig -> masked | completeness orig -> masked |",
          "|---|---|---|---|---|---|---|---|"]
    for src in MODELS + ["linter autofix", "reference"]:
        for cond in (CONDS if src != "reference" else ["reference"]):
            v0, v1 = per["original"][(src, cond)], per["masked"][(src, cond)]
            if not v0: continue
            note = " (not re-rated)" if cond == "chunk" else ""
            L.append(f"| {src} | {cond}{note} | {len(v0)} | {m(v0,'overall'):.2f} | {m(v1,'overall'):.2f} | {m(v1,'overall')-m(v0,'overall'):+.2f} | "
                     f"{m(v0,'conformance'):.2f} -> {m(v1,'conformance'):.2f} | {m(v0,'completeness'):.2f} -> {m(v1,'completeness'):.2f} |")
    L.append("")
    for mode in ("original", "masked"):
        tests = []
        for src in MODELS:
            units = sorted({u for (s, c, u) in unit[mode] if s == src})
            for other in ("none", "fulldoc"):
                b = w = 0; diffs = []
                for u in units:
                    g = unit[mode].get((src, "graph", u)); o = unit[mode].get((src, other, u))
                    if not g or not o: continue
                    d = sum(g) / len(g) - sum(o) / len(o); diffs.append(d); b += d > 0; w += d < 0
                tests.append([src, other, sum(diffs) / max(1, len(diffs)), b, w, sign_p(b, w)])
        adj = holm([t[5] for t in tests])
        L += [f"## Paired sign tests, {mode} scores (per-unit mean overall; Holm across these 12 GSCS tests)", "",
              "| Model | graph vs | mean diff | units better | units worse | p | Holm p |", "|---|---|---|---|---|---|---|"]
        L += [f"| {t[0]} | {t[1]} | {t[2]:+.2f} | {t[3]} | {t[4]} | {t[5]:.3g} | {h:.3g} |" for t, h in zip(tests, adj)] + [""]
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    open(os.path.join(HERE, "results", "mask_summary.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
