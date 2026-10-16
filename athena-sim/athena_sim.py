#!/usr/bin/env python3
"""Athena Sim - headless experiment harness standing in for the Athena VS Code extension.

  python athena_sim.py packs                                   what data is available
  python athena_sim.py run --pack gscs --backend mock:oracle   dry run with a stand-in (no API key)
  python athena_sim.py run --pack gscs --backend openai:o3-mini --conditions none,fulldoc,chunk,graph   (split dev)
  python athena_sim.py freeze <same options> --out-file frozen.json         after tuning on dev
  python athena_sim.py run <same options> --split test --frozen frozen.json   the one test run (see HYPOTHESES.md)
  python athena_sim.py report runs/<run-id> [runs/<other-run-id> ...]
  python athena_sim.py prompts --pack gscs --export prompts.jsonl   prompts to paste into Cursor / Copilot
  python athena_sim.py show --pack gscs --condition graph      print one prompt (what the LLM would see)

Standard library only (Python 3.9+).  See README.md.
"""
from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from athena.packs import load_pack  # noqa: E402
from athena.retrieval import CONDITIONS, Retriever  # noqa: E402
from athena.runner import execute, export_prompts, freeze_cmd, get_units, make_prompt  # noqa: E402
from athena.report import write_reports  # noqa: E402


def add_common(p):
    p.add_argument("--pack", default="gscs", choices=["public5", "gscs"], help="which coding standard + data (default gscs)")
    p.add_argument("--corpus", default=None, help="path to athena-corpus (public5 pack; default ../athena-corpus or $ATHENA_CORPUS)")
    p.add_argument("--task", default="rename", choices=["rename", "comment"])
    p.add_argument("--conditions", default=",".join(CONDITIONS), help="comma list of: " + ", ".join(CONDITIONS))
    p.add_argument("--languages", default=None, help="comma list, e.g. python,java (default: all in the pack)")
    p.add_argument("--per-language", type=int, default=10, help="units sampled per language, 0 = all (default 10)")
    p.add_argument("--limit", type=int, default=0, help="cap total units after sampling (quick tests)")
    p.add_argument("--seed", type=int, default=42, help="sampling seed")
    p.add_argument("--split", default="dev", choices=["dev", "test", "all"],
                   help="dev = tune here (default); test = final numbers, needs --frozen for real models; all = mock only")
    p.add_argument("--top-k", type=int, default=None, help="graph: max rules in the prompt (default: all retrieved)")
    p.add_argument("--chunk-k", type=int, default=3, help="chunk: passages retrieved (default 3)")
    p.add_argument("--examples", type=int, default=2, help="graph: few-shot examples per rule (0 = none, default 2)")


def add_run_args(p):
    """Options that change the numbers (kept identical for `run` and `freeze`)."""
    p.add_argument("--backend", required=True, help="openai:<model> | gemini:<model> | mock:oracle|echo|autofix | replay:<file>")
    p.add_argument("--repeats", type=int, default=1, help="repeat every trial N times (LLMs are non-deterministic)")
    p.add_argument("--temperature", type=float, default=0.2, help="ignored by reasoning models such as o3-mini")
    p.add_argument("--max-tokens", type=int, default=None, help="completion budget (reasoning models: includes hidden reasoning)")
    p.add_argument("--reasoning-effort", default=None, choices=["low", "medium", "high"], help="o1/o3/o4/gpt-5 only")
    p.add_argument("--base-url", default=None, help="OpenAI-compatible endpoint (default $OPENAI_BASE_URL or api.openai.com)")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="athena_sim", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run an experiment")
    add_common(r)
    add_run_args(r)
    r.add_argument("--frozen", default=None, help="frozen setup file (required for --split test with a real model)")
    r.add_argument("--allow-rerun", action="store_true", help="run the test split again under the same freeze (logged)")
    r.add_argument("--timeout", type=float, default=180.0)
    r.add_argument("--retries", type=int, default=5, help="retries per call on 429/5xx/network errors")
    r.add_argument("--workers", type=int, default=1, help="parallel calls (mind rate limits; local servers usually 1)")
    r.add_argument("--max-errors", type=int, default=20, help="abort after N consecutive failed calls")
    r.add_argument("--price-in", type=float, default=None, help="USD per 1M prompt tokens (optional, for the cost column)")
    r.add_argument("--price-out", type=float, default=None, help="USD per 1M completion tokens")
    r.add_argument("--no-store-prompt", action="store_true", help="do not save full prompts in trials.jsonl")
    r.add_argument("--run-id", default=None, help="name of the run folder; reuse to resume")
    r.add_argument("--out", default=os.path.join(HERE, "runs"), help="output folder (default ./runs)")
    r.add_argument("--progress", type=int, default=10, help="print progress every N trials")

    fz = sub.add_parser("freeze", help="fingerprint the setup for the test split (do this after tuning on dev)")
    add_common(fz)
    add_run_args(fz)
    fz.add_argument("--out-file", required=True, help="e.g. frozen_gscs_rename.json")
    fz.add_argument("--note", default="", help="free text, e.g. what was tuned on dev")

    rp = sub.add_parser("report", help="(re)build trials.csv and summary.md from run folders")
    rp.add_argument("runs", nargs="+")
    rp.add_argument("--out", default=None, help="folder for the combined report (default: first run folder)")
    rp.add_argument("--baseline", default=None, help="baseline condition for paired comparisons (default none)")

    pr = sub.add_parser("prompts", help="export prompts for manual tools (Cursor / Copilot / chat UI)")
    add_common(pr)
    pr.add_argument("--export", required=True, help="output .jsonl")

    sh = sub.add_parser("show", help="print the prompt for one sampled unit")
    add_common(sh)
    sh.add_argument("--condition", default="graph", choices=CONDITIONS)
    sh.add_argument("--index", type=int, default=0, help="which sampled unit to show")

    pk = sub.add_parser("packs", help="list packs and unit counts")
    pk.add_argument("--corpus", default=None)

    a = ap.parse_args(argv)
    if a.cmd == "run":
        return execute(a)
    if a.cmd == "freeze":
        return freeze_cmd(a)
    if a.cmd == "report":
        md = write_reports(a.runs, a.out, a.baseline)
        print(md)
        return 0
    if a.cmd == "prompts":
        return export_prompts(a)
    if a.cmd == "show":
        pack = load_pack(a.pack, a.corpus)
        units = get_units(pack, a)
        if a.index >= len(units):
            print("no such unit", file=sys.stderr)
            return 2
        u = units[a.index]
        prompt, ctx = make_prompt(pack, Retriever(pack, a.chunk_k, a.top_k, a.examples), a.task, u, a.condition)
        print(f"# unit {u.unit_id} ({u.language}, {u.kind}); retrieval meta: {ctx.meta}\n")
        print(prompt)
        return 0
    if a.cmd == "packs":
        for name in ("gscs", "public5"):
            try:
                pack = load_pack(name, a.corpus)
            except FileNotFoundError as e:
                print(f"{name}: not available ({e})")
                continue
            ru, cu = pack.rename_units(), pack.comment_units()
            langs = sorted({u.language for u in ru})
            sp = lambda us: "dev=%d test=%d" % (sum(u.split == "dev" for u in us), sum(u.split == "test" for u in us))  # noqa: E731
            print(f"{name}: {pack.title}\n  standards: {', '.join(pack.standard_ids())}\n  rename units: {len(ru)} "
                  f"({', '.join(f'{l}={sum(1 for u in ru if u.language == l)}' for l in langs)}); {sp(ru)}"
                  f"\n  comment units: {len(cu)}; {sp(cu)}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
