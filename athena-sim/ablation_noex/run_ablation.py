#!/usr/bin/env python3
"""Ablation graph_noex (revision plan Phase 3.1; see ADDENDUM.md). Run from this folder in PowerShell:

  $env:OPENAI_API_KEY = "<your hosted API key>"
  python run_ablation.py --dry-run          # show the plan, write nothing
  python run_ablation.py --budget 4         # real run (asks "Start? [y/N]")

For every model: 1-unit smoke test on the DEV split (stops if the API call fails), then freeze, then the TEST split once
(3 repeats). Safe to run again: finished sets are skipped, an interrupted set resumes under the same run id.
Log: runs/run_ablation.log.  Nothing outside this folder is touched.
"""
import argparse, datetime, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
LOG = os.path.join(RUNS, "run_ablation.log")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "")
REPEATS = 3
HOSTED = "graph,graph_noex"
ALL5 = "none,fulldoc,chunk,graph,graph_noex"
GEMMA_EXTRA = os.environ.get("ATHENA_GEMMA_EXTRA_BODY") or json.dumps(
    {"reasoning": {"effort": "none"}})

MODELS = {   # settings identical to the original test runs of each hosted model
    "o3mini": dict(backend="openai:openai/o3-mini", price_in=1.1, price_out=4.4, max_tokens=8192, env={},
                   note="o3-mini via a hosted OpenAI-compatible API, reasoning model (no temperature), max_tokens 8192"),
    "luna": dict(backend="openai:openai/gpt-6-luna", price_in=0.1, price_out=0.5, max_tokens=8192, env={},
                 note="GPT-6 Luna via a hosted OpenAI-compatible API, temperature 0.2, max_tokens 8192"),
    "gemini31fl": dict(backend="openai:google/gemini-3.1-flash-lite", price_in=0.25, price_out=1.5, max_tokens=8192,
                       env={"ATHENA_OMIT_TEMP": "1"},
                       note="Gemini 3.1 Flash-Lite via a hosted OpenAI-compatible API, temperature omitted (ATHENA_OMIT_TEMP=1), max_tokens 8192"),
    "gemma4or": dict(backend="openai:google/gemma-4-26b-a4b-it", price_in=0.042, price_out=0.22, max_tokens=2048,
                     env={"ATHENA_EXTRA_BODY": GEMMA_EXTRA},
                     note="Gemma 4 26B A4B via a hosted OpenAI-compatible API (not the local 4-bit run), temperature 0.2, max_tokens 2048, extra body " + GEMMA_EXTRA),
}
# (model, task, conditions, estimated USD) -- order = priority
PLAN = [
    ("o3mini", "rename", HOSTED, 2.2), ("o3mini", "comment", HOSTED, 0.3),
    ("luna", "rename", HOSTED, 0.15), ("luna", "comment", HOSTED, 0.03),
    ("gemini31fl", "rename", HOSTED, 0.35), ("gemini31fl", "comment", HOSTED, 0.06),
    ("gemma4or", "rename", ALL5, 0.25), ("gemma4or", "comment", ALL5, 0.05),
]


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def emit(msg, dry=False):
    line = "[%s] %s" % (now(), msg)
    print(line, flush=True)
    if not dry:
        os.makedirs(RUNS, exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def trials(run_id):
    p = os.path.join(RUNS, run_id, "trials.jsonl")
    if not os.path.exists(p):
        return []
    out = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def run_cost(run_id):
    return sum(float(t.get("cost_usd") or 0) for t in trials(run_id))


def is_done(frozen_path, run_id):
    p = frozen_path + ".ledger.jsonl"
    done = False
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("run_id") == run_id and e.get("event") == "end":
                    done = e.get("status") == "complete" and not e.get("trials_error")
    return done


def call(cmd, env_extra, dry):
    emit("$ " + " ".join("%s=%s" % kv for kv in env_extra.items()) + " " + subprocess.list2cmdline(cmd), dry)
    if dry:
        return 0
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1",
               ATHENA_LOG_PROVIDER="1", **env_extra)
    p = subprocess.Popen(cmd, cwd=HERE, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", errors="replace")
    with open(LOG, "a", encoding="utf-8") as lf:
        for line in p.stdout:
            line = line.rstrip("\n")
            print(line, flush=True)
            lf.write("    " + line + "\n")
    return p.wait()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--budget", type=float, default=4.0, help="stop starting new sets when spent + estimate > budget (USD)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--only", help="run one set, e.g. luna_rename")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()

    entries = []
    for model, task, conds, est in PLAN:
        sid = "%s_%s" % (model, task)
        entries.append(dict(id=sid, model=model, task=task, conds=conds, est=est, run_id="abl_" + sid,
                            frozen=os.path.join(HERE, "frozen_abl_%s.json" % sid), **MODELS[model]))
    if a.only:
        entries = [e for e in entries if e["id"] == a.only] or sys.exit("unknown set " + a.only)
    if not a.dry_run and not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY is not set in this window (put your hosted API key in it first).")

    spent = sum(run_cost(e["run_id"]) for e in entries)
    print("\nAblation graph_noex (%s)   budget $%.2f   already spent $%.4f\n" % (BASE_URL, a.budget, spent))
    print("%-20s %-40s %-36s %-7s %s" % ("set", "backend", "conditions", "est.$", "state"))
    for e in entries:
        state = "DONE" if is_done(e["frozen"], e["run_id"]) else ("resume" if os.path.isdir(os.path.join(RUNS, e["run_id"])) else "new")
        print("%-20s %-40s %-36s %-7.2f %s" % (e["id"], e["backend"], e["conds"], e["est"], state))
    print()
    if not a.dry_run and not a.yes and input("Start? [y/N] ").strip().lower() != "y":
        sys.exit("cancelled")

    smoked, skipped = set(), []
    try:
        for e in entries:
            rid, fz = e["run_id"], e["frozen"]
            if is_done(fz, rid):
                emit("SKIP %s: already complete" % e["id"], a.dry_run)
                continue
            remaining = max(e["est"] - run_cost(rid), 0.0)
            if spent + remaining > a.budget:
                emit("SKIP %s: spent $%.2f + est. $%.2f > budget $%.2f" % (e["id"], spent, remaining, a.budget), a.dry_run)
                skipped.append(e["id"])
                continue
            base = ["--pack", "gscs", "--backend", e["backend"], "--per-language", "0", "--max-tokens", str(e["max_tokens"]),
                    "--base-url", BASE_URL]
            if e["model"] not in smoked and not os.path.exists(fz):          # smoke once per model, before its freeze
                srid = "smoke_" + e["model"]
                rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "run"] + base +
                          ["--task", "rename", "--conditions", e["conds"], "--split", "dev", "--limit", "1", "--repeats", "1",
                           "--run-id", srid, "--max-errors", "2"], e["env"], a.dry_run)
                errs = [t for t in trials(srid) if t.get("error")]
                if not a.dry_run and (rc or errs):
                    emit("STOP: smoke test for %s failed (rc=%s, %d API errors). First error: %s\n"
                         "Send this message to Claude; nothing was frozen or run on the test split."
                         % (e["model"], rc, len(errs), (errs[0]["error"] if errs else "-")[:400]))
                    sys.exit(1)
                if not a.dry_run:
                    served = sorted({t.get("model") for t in trials(srid)})
                    emit("smoke OK for %s; served by: %s" % (e["model"], ", ".join(map(str, served))))
                smoked.add(e["model"])
            common = base + ["--task", e["task"], "--conditions", e["conds"], "--repeats", str(REPEATS)]
            if not os.path.exists(fz):
                rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "freeze"] + common +
                          ["--out-file", fz, "--note", "ablation graph_noex (ADDENDUM.md): " + e["note"]], e["env"], a.dry_run)
                if rc:
                    sys.exit("freeze failed for %s (rc=%s)" % (e["id"], rc))
            emit("START %s (run id %s)" % (e["id"], rid), a.dry_run)
            rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "run"] + common +
                      ["--split", "test", "--workers", str(a.workers), "--max-errors", "10",
                       "--price-in", str(e["price_in"]), "--price-out", str(e["price_out"]),
                       "--frozen", fz, "--run-id", rid], e["env"], a.dry_run)
            spent = sum(run_cost(x["run_id"]) for x in entries)
            emit("END %s rc=%s   this set $%.4f   total spent $%.4f" % (e["id"], rc, run_cost(rid), spent), a.dry_run)
            if rc:
                emit("FAILED %s - fix, then run this script again to resume" % e["id"], a.dry_run)
                sys.exit(1)
    except KeyboardInterrupt:
        emit("INTERRUPTED - progress is saved; run this script again to resume", a.dry_run)
        sys.exit(130)
    emit("SUMMARY total spent $%.4f of budget $%.2f; skipped: %s" % (spent, a.budget, ", ".join(skipped) or "none"), a.dry_run)


if __name__ == "__main__":
    main()
