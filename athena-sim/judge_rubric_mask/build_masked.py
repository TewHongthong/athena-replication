"""Sensitivity items for the rubric judges (see ADDENDUM.md): every GSCS comment (generated, rule-based fixer,
developer reference) with the values of the four labels the code cannot reveal replaced by one fixed token.
Reads ../judge_rubric/items.jsonl + item_map.jsonl; writes items.jsonl, item_map.jsonl, mask_report.md here."""
import hashlib, json, os, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ORIG = os.path.join(os.path.dirname(HERE), "judge_rubric")
TOKEN = "[not inferable from code]"
LABEL = r"(?:created\s*by|creat(?:e|ed|ion)\s*date|revised\s*by|revis(?:ed|ion)\s*date)"
STOP = r"(?:\*/|\"\"\"|'''|" + LABEL + r"\s*:)"
PAT = re.compile(r"(?i)(" + LABEL + r")(\s*:)((?:(?!" + STOP + r").)*)")


def mask(comment):
    n = 0
    def rep(m):
        nonlocal n; n += 1
        tail = m.group(3)
        trail = " " if tail.endswith(" ") and tail.strip() else ""
        return f"{m.group(1)}{m.group(2)} {TOKEN}{trail}"
    return PAT.sub(rep, comment), n


def main():
    items = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(ORIG, "items.jsonl"), encoding="utf-8")}
    rows = [json.loads(l) for l in open(os.path.join(ORIG, "item_map.jsonl"), encoding="utf-8")]
    rows = [r for r in rows if r["pack"] == "gscs"]
    new, mp, stats, changed, examples = {}, [], Counter(), 0, []
    for r in rows:
        if r["item"] is None:
            mp.append(dict(r, orig_item=None, item=None)); continue
        it = items[r["item"]]
        mc, n = mask(it["comment"])
        stats[n] += 1
        if mc != it["comment"]:
            changed += 1
            if len(examples) < 4 and r["source"] in ("Gemma 4 26B", "Qwen3.5-9B", "reference"):
                examples.append((r["source"], r["condition"], it["comment"], mc))
        iid = hashlib.sha256(f"gscs|{r['unit']}|{mc}".encode()).hexdigest()[:16]
        if iid not in new:
            new[iid] = dict(it, id=iid, comment=mc)
        mp.append(dict(r, orig_item=r["item"], item=iid))
    order = sorted(new); random.Random(20261003).shuffle(order)
    with open(os.path.join(HERE, "items.jsonl"), "w", encoding="utf-8") as f:
        for i in order: f.write(json.dumps(new[i], ensure_ascii=False) + "\n")
    with open(os.path.join(HERE, "item_map.jsonl"), "w", encoding="utf-8") as f:
        for r in mp: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    orig_ids = {r["orig_item"] for r in mp if r["orig_item"]}
    L = ["# Masking report", "", f"GSCS map rows: {len(mp)} (no comment: {sum(r['item'] is None for r in mp)})",
         f"original unique GSCS items: {len(orig_ids)} -> masked unique items: {len(new)}",
         f"rows whose comment changed: {changed}", f"labels masked per comment: {dict(sorted(stats.items()))}", ""]
    for src, cond, a, b in examples:
        L += [f"## {src} / {cond}", "", "before:", "```", a, "```", "after:", "```", b, "```", ""]
    open(os.path.join(HERE, "mask_report.md"), "w", encoding="utf-8").write("\n".join(L))
    print("\n".join(L[:7]))


if __name__ == "__main__":
    main()


# ---- scope of re-rating (appended; see ADDENDUM.md) ----
SCOPE = {"none", "fulldoc", "graph", "reference"}   # the conditions the paper tests (graph vs none, graph vs fulldoc) + ceiling


def write_scope():
    """items_to_rate.jsonl = masked items whose text differs from the original item and that occur in SCOPE or come
    from the rule-based fixer (floor). Every other row keeps its original rating (identical judge input)."""
    rows = [json.loads(l) for l in open(os.path.join(HERE, "item_map.jsonl"), encoding="utf-8")]
    orig = {json.loads(l)["id"]: json.loads(l)["comment"] for l in open(os.path.join(ORIG, "items.jsonl"), encoding="utf-8")}
    new = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(HERE, "items.jsonl"), encoding="utf-8")}
    ids = []
    for r in rows:
        if r["item"] and new[r["item"]]["comment"] != orig[r["orig_item"]] and (r["condition"] in SCOPE or r["source"] == "linter autofix"):
            if r["item"] not in ids: ids.append(r["item"])
    order = [i for i in (json.loads(l)["id"] for l in open(os.path.join(HERE, "items.jsonl"), encoding="utf-8")) if i in set(ids)]
    with open(os.path.join(HERE, "items_to_rate.jsonl"), "w", encoding="utf-8") as f:
        for i in order: f.write(json.dumps(new[i], ensure_ascii=False) + "\n")
    print("items to rate:", len(order))


if __name__ == "__main__":
    write_scope()
