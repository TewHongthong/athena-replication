"""Phase 10 (see ADDENDUM.md). Run from athena-sim/phase10_stats: python -B phase10.py -> results.md, results.json"""
import collections, csv, json, math, os
SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = {"o3-mini": "runs/test_o3mini_gscs_{t}", "GPT-6 Luna": "runs/test_luna_gscs_{t}",
        "Qwen3.5-9B": "runs/qwen_gscs_{t}", "Gemini 3.1 Flash-Lite": "runs/gemini31fl_gscs_{t}",
        "DeepSeek V4 Flash": "runs/dsv4f_gscs_{t}", "Gemma 4 26B": "runs/gemma4_gscs_{t}"}
ABL = {"o3-mini": ("ablation_noex/runs/abl_o3mini_{t}", "runs/test_o3mini_gscs_{t}"),
       "GPT-6 Luna": ("ablation_noex/runs/abl_luna_{t}", "runs/test_luna_gscs_{t}"),
       "Gemini 3.1 Flash-Lite": ("ablation_noex/runs/abl_gemini31fl_{t}", "runs/gemini31fl_gscs_{t}"),
       "Gemma 4 26B (endpoint)": ("ablation_noex/runs/abl_gemma4or_{t}", None)}
PM = {"rename": "core_ok", "comment": "comment_ok"}

def load(rel):
    p = os.path.join(SIM, rel, "trials.jsonl"); latest = {}
    for l in open(p, encoding="utf-8"):
        try: t = json.loads(l)
        except ValueError: continue
        latest[t["key"]] = t
    return [t for t in latest.values() if not t.get("error")]

def prog_means(trials, cond, metric):
    unit = collections.defaultdict(list); prog_of = {}
    for t in trials:
        if t["condition"] != cond: continue
        v = (t.get("metrics") or {}).get(metric)
        if v is None and metric == "comment_ok":
            continue
        unit[t["unit_id"]].append(1.0 if v else 0.0); prog_of[t["unit_id"]] = t["snippet_id"]
    um = {u: sum(v) / len(v) for u, v in unit.items()}
    pr = collections.defaultdict(list)
    for u, m in um.items(): pr[prog_of[u]].append(m)
    return {p: sum(v) / len(v) for p, v in pr.items()}, um, prog_of

def sign(a, b):
    ks = sorted(set(a) & set(b)); be = sum(a[k] > b[k] for k in ks); wo = sum(a[k] < b[k] for k in ks); n = be + wo
    p = 1.0 if n == 0 else min(1.0, 2 * sum(math.comb(n, i) for i in range(min(be, wo) + 1)) / 2 ** n)
    return dict(n=len(ks), better=be, worse=wo, ties=len(ks) - n, diff=100 * sum(a[k] - b[k] for k in ks) / len(ks), p=p)

def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); out = [0.0] * len(ps); run = 0.0
    for r, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - r) * ps[i])); out[i] = run
    return out

def main_runs():
    rows = []
    for m, rel in MAIN.items():
        tr = load(rel.format(t="rename"))
        P = {c: prog_means(tr, c, "core_ok")[0] for c in ("none", "fulldoc", "chunk", "graph")}
        U = {c: prog_means(tr, c, "core_ok")[1] for c in ("none", "fulldoc", "chunk", "graph")}
        fam = [("fulldoc", "none"), ("chunk", "none"), ("graph", "none")]
        res = [dict(model=m, a=a, b=b, level="program", **sign(P[a], P[b])) for a, b in fam]
        for r, h in zip(res, holm([r["p"] for r in res])): r["p_holm"] = h
        unit = [dict(model=m, a=a, b=b, level="unit", **sign(U[a], U[b])) for a, b in fam]
        for r, h in zip(unit, holm([r["p"] for r in unit])): r["p_holm"] = h
        expl = [dict(model=m, a=a, b=b, level="program", p_holm=None, **sign(P[a], P[b])) for a, b in (("graph", "chunk"), ("graph", "fulldoc"))]
        explu = [dict(model=m, a=a, b=b, level="unit", p_holm=None, **sign(U[a], U[b])) for a, b in (("graph", "chunk"), ("graph", "fulldoc"))]
        rows += res + expl + unit + explu
    return rows

def ablation():
    rows = []
    for m, (new, orig) in ABL.items():
        for task in ("rename", "comment"):
            nt = load(new.format(t=task)); ot = load(orig.format(t=task)) if orig else None
            src = {}
            for c in ("graph", "graph_noex", "none", "fulldoc", "chunk"):
                if any(t["condition"] == c for t in nt): src[c] = (nt, c)
                elif ot and any(t["condition"] == c for t in ot): src[c] = (ot, c)
            if ot and any(t["condition"] == "graph" for t in ot): src["graph_orig"] = (ot, "graph")
            P = {k: prog_means(tr, c, PM[task])[0] for k, (tr, c) in src.items()}
            pairs = [("graph", "graph_noex"), ("graph_noex", "chunk"), ("graph_noex", "fulldoc"), ("graph_noex", "none")]
            pairs.append(("graph", "graph_orig") if "graph_orig" in P else ("graph", "none"))
            res = [dict(model=m, task=task, a=a, b=b, **sign(P[a], P[b])) for a, b in pairs if a in P and b in P]
            for r, h in zip(res, holm([r["p"] for r in res])): r["p_holm"] = h
            rows += res
    return rows

def comment_units_per_program():
    tr = load(MAIN["o3-mini"].format(t="comment"))
    c = collections.Counter(); seen = set()
    for t in tr:
        if (t["unit_id"]) in seen: continue
        seen.add(t["unit_id"]); c[t["snippet_id"]] += 1
    tr2 = load(MAIN["o3-mini"].format(t="rename")); u = collections.defaultdict(set)
    for t in tr2: u[t["snippet_id"]].add(t["unit_id"])
    return dict(comment=dict(c), rename_units_per_program={k: len(v) for k, v in sorted(u.items())})

def semantic():
    rows = list(csv.DictReader(open(os.path.join(SIM, "semantic_check/results/trial_results.csv"), encoding="utf-8")))
    st = collections.Counter(r["status"] for r in rows)
    na = [r for r in rows if r["status"] == "not_applied"]
    reasons = collections.Counter()
    for r in na:
        s = (r["suggested"] or "").strip()
        reasons["no valid answer" if not s else ("same as injected" if s == r["injected"] else "other")] += 1
    by_model = collections.Counter(r["model"] for r in na)
    ex = [json.loads(l) for l in open(os.path.join(SIM, "semantic_check/results/exec_cache.jsonl"), encoding="utf-8")]
    return dict(trials=len(rows), status=dict(st), not_applied_reasons=dict(reasons), not_applied_by_model=dict(by_model),
                exec_cache_entries=len(ex))

def main():
    M, A, C, S = main_runs(), ablation(), comment_units_per_program(), semantic()
    json.dump(dict(main=M, ablation=A, units=C, semantic=S), open(os.path.join(HERE, "results.json"), "w"), indent=1)
    L = ["# Phase 10 results (exploratory; see ADDENDUM.md)", "", "## 10.1a GSCS rename, main runs", "",
         "| model | comparison | level | n | better/worse/ties | mean diff pp | p | Holm p |", "|---|---|---|---|---|---|---|---|"]
    for r in M:
        L.append(f"| {r['model']} | {r['a']} vs {r['b']} | {r['level']} | {r['n']} | {r['better']}/{r['worse']}/{r['ties']} | {r['diff']:+.1f} | {r['p']:.3g} | {'-' if r['p_holm'] is None else format(r['p_holm'], '.3g')} |")
    L += ["", "## 10.1b Ablation (program level, Holm within model x task)", "",
          "| model | task | comparison | n | better/worse/ties | mean diff pp | p | Holm p |", "|---|---|---|---|---|---|---|---|"]
    for r in A:
        L.append(f"| {r['model']} | {r['task']} | {r['a']} vs {r['b']} | {r['n']} | {r['better']}/{r['worse']}/{r['ties']} | {r['diff']:+.1f} | {r['p']:.3g} | {r['p_holm']:.3g} |")
    L += ["", "## 10.1c Units per program", "", f"comment units per program: {C['comment']}", f"rename units per program: {C['rename_units_per_program']}",
          "", "## 10.2 Behaviour check accounting", "", "```", json.dumps(S, indent=1), "```"]
    open(os.path.join(HERE, "results.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))

if __name__ == "__main__":
    main()
