"""Phase 9 re-analysis (see ADDENDUM.md). Run from athena-sim/phase9_stats:  python -B phase9.py  -> results.md, results.json"""
import collections, glob, json, os, sys
import numpy as np

SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SIM)
from athena.evaluate import check_naming_compliance, name_for_check  # noqa: E402
from athena.packs import load_pack  # noqa: E402

B, SEED = 10_000, 20261003
GSCS = {"o3-mini": "runs/test_o3mini_gscs_{t}", "GPT-6 Luna": "runs/test_luna_gscs_{t}",
        "Qwen3.5-9B": "runs/qwen_gscs_{t}", "Gemini 3.1 Flash-Lite": "runs/gemini31fl_gscs_{t}",
        "DeepSeek V4 Flash": "runs/dsv4f_gscs_{t}", "Gemma 4 26B": "runs/gemma4_gscs_{t}"}
P5 = {"GPT-6 Luna": "runs/test_luna_p5_{t}"}
ABL = {"o3-mini": "ablation_noex/runs/abl_o3mini_{t}", "GPT-6 Luna": "ablation_noex/runs/abl_luna_{t}",
       "Gemini 3.1 Flash-Lite": "ablation_noex/runs/abl_gemini31fl_{t}", "Gemma 4 26B (endpoint)": "ablation_noex/runs/abl_gemma4or_{t}"}
FROZEN = {"o3-mini": "frozen/frozen_o3mini_gscs_{t}.json", "GPT-6 Luna": "frozen/frozen_luna_gscs_{t}.json",
          "GPT-6 Luna (Public5)": "frozen/frozen_luna_p5_{t}.json", "Qwen3.5-9B": "frozen/frozen_qwen_gscs_{t}.json",
          "Gemini 3.1 Flash-Lite": "frozen/frozen_gemini31fl_gscs_{t}.json",
          "DeepSeek V4 Flash": "frozen/frozen_dsv4f_gscs_{t}.json", "Gemma 4 26B": "frozen/frozen_gemma4_gscs_{t}.json",
          "ablation o3-mini": "ablation_noex/frozen_abl_o3mini_{t}.json", "ablation Luna": "ablation_noex/frozen_abl_luna_{t}.json",
          "ablation Gemini": "ablation_noex/frozen_abl_gemini31fl_{t}.json",
          "ablation Gemma (endpoint)": "ablation_noex/frozen_abl_gemma4or_{t}.json"}
COND = ["none", "fulldoc", "chunk", "graph", "graph_noex"]


def load_all(rel):
    latest = {}
    with open(os.path.join(SIM, rel, "trials.jsonl"), encoding="utf-8") as f:
        for line in f:
            t = json.loads(line); latest[t["key"]] = t
    return list(latest.values())


def load(rel):
    return [t for t in load_all(rel) if not t.get("error")]


def mean(x):
    x = list(x); return sum(x) / len(x) if x else float("nan")


# ---------------------------------------------------------------- 9.1
def settings():
    rows = []
    for name, pat in FROZEN.items():
        for t in ("rename", "comment"):
            p = os.path.join(SIM, pat.format(t=t))
            if not os.path.exists(p):
                continue
            s = json.load(open(p, encoding="utf-8")).get("settings", {})
            rows.append(dict(run=name, task=t, **{k: s.get(k) for k in
                        ("conditions", "top_k", "chunk_k", "examples", "temperature", "max_tokens", "repeats")}))
    return rows


def retrieval_load():
    rows = []
    for fam, mp in (("GSCS", GSCS), ("Public5", P5), ("Ablation", ABL)):
        for task in ("rename", "comment"):
            for model, rel in mp.items():
                try:
                    tr = load(rel.format(t=task))
                except FileNotFoundError:
                    continue
                for c in COND:
                    T = [t for t in tr if t["condition"] == c]
                    if not T:
                        continue
                    n = [(t.get("retrieval") or {}).get("n_items", 0) for t in T]
                    pt = [t["prompt_tokens"] for t in T if t.get("prompt_tokens")]
                    rows.append(dict(family=fam, task=task, model=model, condition=c, trials=len(T),
                                     items_mean=mean(n), items_min=min(n), items_max=max(n),
                                     prompt_tokens=mean(pt) if pt else None))
    return rows


# ---------------------------------------------------------------- 9.2
def si_table():
    rows = []
    for fam, mp in (("GSCS", GSCS), ("Public5", P5)):
        for model, rel in mp.items():
            allt = load_all(rel.format(t="rename"))
            for c in COND[:4]:
                A = [t for t in allt if t["condition"] == c]
                T = [t for t in A if not t.get("error")]
                if not T:
                    continue
                m = [t["metrics"] for t in T]
                inv = [x for x in m if not x.get("valid_identifier")]
                val = [x for x in m if x.get("valid_identifier")]
                rows.append(dict(family=fam, model=model, condition=c, trials=len(A), errors=len(A) - len(T),
                                 invalid=len(inv), invalid_pct=100 * len(inv) / len(T),
                                 si_before=mean(x["sim_char_before"] for x in m),
                                 si_reported=mean(x["sim_char_after"] for x in m),
                                 si_valid=mean(x["sim_char_after"] for x in val),
                                 invalid_at_1=sum(1 for x in inv if x["sim_char_after"] >= 1.0)))
    return rows


# ---------------------------------------------------------------- 9.3
def must_only():
    pack = load_pack("public5")
    sev = lambda rid: pack.ontology.rule(rid).get("severity")
    tr = load(P5["GPT-6 Luna"].format(t="rename"))
    units = {}
    for t in tr:
        units.setdefault(t["unit_id"], (t["language"], t["kind"]))
    core_sets = {u: pack.core_rules(l, k) for u, (l, k) in units.items()}
    affected = sum(1 for s in core_sets.values() if any(sev(r) != "MUST" for r in s))
    no_must = sum(1 for s in core_sets.values() if s and not any(sev(r) == "MUST" for r in s))
    no_core = sum(1 for s in core_sets.values() if not s)
    rows, mismatch = [], 0
    for c in COND[:4]:
        T = [t for t in tr if t["condition"] == c]
        per_all, per_must = collections.defaultdict(list), collections.defaultdict(list)
        for t in T:
            m = t["metrics"]; core = core_sets[t["unit_id"]]
            must = [r for r in core if sev(r) == "MUST"]
            if m.get("valid_identifier"):
                chk = name_for_check(t["language"], m["suggested"])
                ok_all = all(check_naming_compliance(chk, pack.ontology.rule(r))[0] for r in core) if core else None
                ok_must = all(check_naming_compliance(chk, pack.ontology.rule(r))[0] for r in must) if must else None
            else:
                ok_all = False if core else None
                ok_must = False if must else None
            rec = m.get("core_ok")
            if (rec is None) != (ok_all is None) or (rec is not None and bool(rec) != bool(ok_all)):
                mismatch += 1
            if ok_all is not None:
                per_all[t["unit_id"]].append(1.0 if ok_all else 0.0)
            if ok_must is not None:
                per_must[t["unit_id"]].append(1.0 if ok_must else 0.0)
        ra = mean(mean(v) for v in per_all.values()); rm = mean(mean(v) for v in per_must.values())
        rows.append(dict(condition=c, units_all=len(per_all), rate_all=100 * ra, units_must=len(per_must), rate_must=100 * rm))
    # GSCS check
    g = load_pack("gscs")
    gsev = collections.Counter(n.get("severity") for n in g.ontology.nodes.values() if n.get("type") == "NamingRule")
    return dict(rows=rows, units=len(units), affected_units=affected, no_must_units=no_must, no_core_units=no_core,
                recompute_mismatch=mismatch, gscs_naming_severity=dict(gsev) if gsev else None)


# ---------------------------------------------------------------- 9.4
def repo_of_snippets():
    out = {}
    for p in glob.glob(os.path.join(SIM, "..", "athena-corpus", "benchmark", "snippets", "*", "*.json")):
        d = json.load(open(p, encoding="utf-8"))
        out[d["id"]] = d["provenance"]["repo"]
    for p in glob.glob(os.path.join(SIM, "..", "athena-corpus", "benchmark", "comment_units", "*", "*.json")):
        d = json.load(open(p, encoding="utf-8"))
        out.setdefault(d["snippetId"], d["provenance"]["repo"])
    return out


def cluster_ci(values_by_unit, cluster_of, rng):
    """values_by_unit: unit -> value (mean over repeats, or paired difference). Rate = mean over units."""
    us = sorted(values_by_unit); x = np.array([values_by_unit[u] for u in us])
    bs_u = x[rng.integers(0, len(x), size=(B, len(x)))].mean(axis=1)
    groups = collections.defaultdict(list)
    for u in us:
        groups[cluster_of[u]].append(values_by_unit[u])
    sums = np.array([sum(v) for v in groups.values()]); cnts = np.array([len(v) for v in groups.values()])
    j = rng.integers(0, len(sums), size=(B, len(sums)))
    bs_r = sums[j].sum(axis=1) / cnts[j].sum(axis=1)
    return (float(x.mean()), tuple(np.percentile(bs_u, [2.5, 97.5])), tuple(np.percentile(bs_r, [2.5, 97.5])),
            len(us), len(groups))


def repo_bootstrap(rng):
    repo = repo_of_snippets(); rows = []
    for task, metric in (("rename", "core_ok"), ("comment", "comment_ok")):
        tr = load(P5["GPT-6 Luna"].format(t=task))
        per = {c: collections.defaultdict(list) for c in COND[:4]}; cl = {}
        for t in tr:
            v = (t.get("metrics") or {}).get(metric)
            if v is None and metric == "comment_ok":
                continue
            per[t["condition"]][t["unit_id"]].append(1.0 if v else 0.0)
            cl[t["unit_id"]] = repo[t["snippet_id"]]
        um = {c: {u: mean(v) for u, v in d.items()} for c, d in per.items()}
        for c in COND[:4]:
            r, ciu, cir, nu, nr = cluster_ci(um[c], cl, rng)
            rows.append(dict(task=task, stat=c, value=100 * r, unit_ci=[100 * a for a in ciu],
                             repo_ci=[100 * a for a in cir], units=nu, repos=nr))
        for a, b in (("graph", "none"), ("graph", "chunk"), ("graph", "fulldoc")):
            common = set(um[a]) & set(um[b])
            d = {u: um[a][u] - um[b][u] for u in common}
            r, ciu, cir, nu, nr = cluster_ci(d, cl, rng)
            rows.append(dict(task=task, stat=f"{a} - {b} (pp)", value=100 * r, unit_ci=[100 * x for x in ciu],
                             repo_ci=[100 * x for x in cir], units=nu, repos=nr))
    return rows


def main():
    rng = np.random.default_rng(SEED)
    S, R, SI, M, RB = settings(), retrieval_load(), si_table(), must_only(), repo_bootstrap(rng)
    json.dump(dict(settings=S, retrieval=R, si=SI, must_only=M, repo_bootstrap=RB),
              open(os.path.join(HERE, "results.json"), "w", encoding="utf-8"), indent=1, default=str)
    f1 = lambda v: "-" if v is None else f"{v:.1f}"
    L = ["# Phase 9 results (exploratory; see ADDENDUM.md)", "", "## 9.1a Settings used (frozen configs)", "",
         "| run | task | conditions | top_k | chunk_k | examples | temperature | max_tokens | repeats |", "|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {r['run']} | {r['task']} | {','.join(r['conditions'] or [])} | {r['top_k']} | {r['chunk_k']} | {r['examples']} | "
          f"{r['temperature']} | {r['max_tokens']} | {r['repeats']} |" for r in S]
    L += ["", "## 9.1b Retrieved items per trial and prompt tokens", "",
          "| family | task | model | condition | trials | items mean | min | max | prompt tokens |", "|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {r['family']} | {r['task']} | {r['model']} | {r['condition']} | {r['trials']} | {r['items_mean']:.2f} | "
          f"{r['items_min']} | {r['items_max']} | {f1(r['prompt_tokens']) if r['prompt_tokens'] else '-'} |" for r in R]
    L += ["", "## 9.2 Similarity Index (character) and invalid answers", "",
          "| family | model | condition | trials | provider errors | invalid (%) | SI before | SI reported | SI valid only | invalid at SI=1 |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {r['family']} | {r['model']} | {r['condition']} | {r['trials']} | {r['errors']} | {r['invalid']} ({r['invalid_pct']:.1f}) | "
          f"{r['si_before']:.4f} | {r['si_reported']:.4f} | {r['si_valid']:.4f} | {r['invalid_at_1']} |" for r in SI]
    L += ["", "## 9.3 MUST-only sensitivity (Public5, Luna, rename)", "",
          f"units {M['units']}; core set contains SHOULD/MAY: {M['affected_units']}; core set has no MUST rule: {M['no_must_units']}; "
          f"no core rule: {M['no_core_units']}; recompute mismatches vs recorded core_ok: {M['recompute_mismatch']}; "
          f"GSCS naming-rule severities: {M['gscs_naming_severity']}", "",
          "| condition | units (all core) | core-rule % (recorded definition) | units (MUST only) | MUST-only % |", "|---|---|---|---|---|"]
    L += [f"| {r['condition']} | {r['units_all']} | {r['rate_all']:.1f} | {r['units_must']} | {r['rate_must']:.1f} |" for r in M["rows"]]
    L += ["", "## 9.4 Repository-level cluster bootstrap (Public5, Luna)", "",
          "| task | statistic | value | unit bootstrap 95% | repository bootstrap 95% | units | repos |", "|---|---|---|---|---|---|---|"]
    L += [f"| {r['task']} | {r['stat']} | {r['value']:.1f} | {r['unit_ci'][0]:.1f}–{r['unit_ci'][1]:.1f} | "
          f"{r['repo_ci'][0]:.1f}–{r['repo_ci'][1]:.1f} | {r['units']} | {r['repos']} |" for r in RB]
    open(os.path.join(HERE, "results.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("written results.md, results.json")


if __name__ == "__main__" and not os.environ.get("PHASE9_95"):
    main()


# ---------------------------------------------------------------- 9.5 (appended; see ADDENDUM 9.5)
def gscs_section_hit():
    pack = load_pack("gscs")
    def secs(rid):
        s = pack.ontology.rule(rid).get("sourceSection", "")
        return {x.split(" - ")[0].strip() for x in s.split(";") if x.strip()}
    rows = []
    for model, rel in GSCS.items():
        T = [t for t in load(rel.format(t="rename")) if t["condition"] == "chunk"]
        hit, miss = [], []
        for t in T:
            core = pack.core_rules(t["language"], t["kind"])
            need = set().union(*[secs(r) for r in core]) if core else set()
            got = set((t.get("retrieval") or {}).get("retrieved_ids") or [])
            ok = 1.0 if (t.get("metrics") or {}).get("core_ok") else 0.0
            (hit if need and need <= got else miss).append(ok)
        rows.append(dict(model=model, trials=len(T), hit_pct=100 * len(hit) / len(T),
                         core_hit=100 * mean(hit) if hit else None, core_miss=100 * mean(miss) if miss else None,
                         n_hit=len(hit), n_miss=len(miss)))
    return rows


if __name__ == "__main__" and os.environ.get("PHASE9_95"):
    R = gscs_section_hit()
    L = ["", "## 9.5 GSCS chunk retrieval: section-level hit (exploratory; ADDENDUM 9.5)", "",
         "| model | chunk trials | section hit % | core-rule % when hit (n) | core-rule % when missed (n) |", "|---|---|---|---|---|"]
    f = lambda v: "-" if v is None else f"{v:.1f}"
    L += [f"| {r['model']} | {r['trials']} | {r['hit_pct']:.1f} | {f(r['core_hit'])} ({r['n_hit']}) | {f(r['core_miss'])} ({r['n_miss']}) |" for r in R]
    open(os.path.join(HERE, "results.md"), "a", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))
