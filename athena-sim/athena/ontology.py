"""Stdlib-only reader for an Athena ontology (node-link JSON, see ontology_schema.md).

Equivalent to graph_loader.get_applicable_rules() + graph_rag.rank_rules() of the project's
pipeline, but without the networkx dependency so it runs on any plain Python 3.9+.
"""
from __future__ import annotations

import hashlib
import json

SEVERITY_RANK = {"MUST": 3, "SHOULD": 2, "MAY": 1}
# same specificity fields as graph_rag.py, plus requiredLabels (used by the custom GSCS pack)
SPECIFICITY_FIELDS = ["prefix", "suffix", "minLength", "maxLength", "forbiddenPatterns",
                      "requiredElements", "requiredLabels"]


def specificity(rule: dict) -> int:
    return sum(1 for f in SPECIFICITY_FIELDS if rule.get(f))


def rank_key(rule: dict):
    return (-SEVERITY_RANK.get(rule.get("severity"), 0), -specificity(rule), rule["id"])


def render_rule(rule: dict, examples: list | None = None) -> str:
    """One rule as prompt text.  Regexes are shown only when short and not flagged hidePatterns."""
    kind = rule.get("identifierKind", "")
    head = f"[{rule.get('severity', '?')}] {rule['id']}" + (f" ({kind})" if kind else "")
    lines = [f"{head}: {rule.get('description', '').strip()}"]
    checks = []
    if rule.get("casing"):
        checks.append(f"casing={rule['casing']}")
    if rule.get("prefix"):
        checks.append(f"prefix={rule['prefix']}")
    if rule.get("suffix"):
        checks.append(f"suffix={rule['suffix']}")
    if rule.get("allowedPrefixes"):
        checks.append("type prefixes: " + ", ".join(rule["allowedPrefixes"]))
    if rule.get("minLength"):
        checks.append(f"min length={rule['minLength']}")
    if rule.get("maxLength"):
        checks.append(f"max length={rule['maxLength']}")
    if rule.get("forbiddenPatterns") and not rule.get("hidePatterns"):
        checks.append("forbidden: " + ", ".join(f"/{p}/" for p in rule["forbiddenPatterns"]))
    if rule.get("requiredLabels"):
        checks.append("must contain: " + "; ".join(rule["requiredLabels"]))
    elif rule.get("requiredElements"):
        checks.append("must contain: " + "; ".join(rule["requiredElements"]))
    if checks:
        lines.append("  checks: " + " | ".join(checks))
    for ex in examples or []:
        tag = "OK " if ex.get("isCompliant") else "BAD"
        note = f" -- {ex['explanation']}" if ex.get("explanation") else ""
        code = str(ex.get("code", "")).replace("\n", " ⏎ ")
        lines.append(f"  {tag}: `{code}`{note}")
    return "\n".join(lines)


class Ontology:
    def __init__(self, path: str):
        with open(path, "rb") as f:
            raw = f.read()
        self.path = path
        self.sha256 = hashlib.sha256(raw).hexdigest()
        d = json.loads(raw.decode("utf-8"))
        self.name = d.get("graph", {}).get("name", "ontology")
        self.nodes = {n["id"]: n for n in d["nodes"]}
        self.languages = [n["id"] for n in d["nodes"] if n["type"] == "Language"]
        self.kinds = [n["id"] for n in d["nodes"] if n["type"] == "IdentifierKind"]
        self._applies: dict[str, dict[str, set]] = {}
        self._examples: dict[str, list[dict]] = {}
        self._defined_in: dict[str, str] = {}
        for e in d["links"]:
            rel, s, t = e["relation"], e["source"], e["target"]
            if rel == "APPLIES_TO":
                a = self._applies.setdefault(s, {"lang": set(), "kind": set()})
                if t in self.languages:
                    a["lang"].add(t)
                else:
                    a["kind"].add(t)
            elif rel == "HAS_EXAMPLE":
                self._examples.setdefault(s, []).append(self.nodes[t])
            elif rel == "DEFINED_IN":
                self._defined_in[s] = t

    # ---- lookups -------------------------------------------------------------
    def rule(self, rid: str) -> dict:
        return {"id": rid, **self.nodes[rid]}

    def standard_name(self, sid: str) -> str:
        return self.nodes.get(sid, {}).get("name", sid)

    def rules_for(self, lang: str, kind: str, types=("NamingRule",), standard_id: str | None = None) -> list[dict]:
        """Ranked rules that APPLIES_TO both `lang` and `kind` (graph-RAG step 1 + ranking)."""
        out = []
        for rid, a in self._applies.items():
            n = self.nodes.get(rid)
            if n is None or n["type"] not in types:
                continue
            if lang in a["lang"] and kind in a["kind"]:
                if standard_id and self._defined_in.get(rid) not in (None, standard_id):
                    continue
                out.append({"id": rid, **n})
        return sorted(out, key=rank_key)

    def rules_of_standard(self, standard_id: str, types=("NamingRule", "CommentRule", "StructureRule")) -> list[dict]:
        out = [{"id": rid, **self.nodes[rid]} for rid, sid in self._defined_in.items()
               if sid == standard_id and self.nodes[rid]["type"] in types]
        return sorted(out, key=lambda r: r["id"])

    def examples(self, rid: str, max_n: int | None = 2) -> list[dict]:
        """Keep a compliant + a non-compliant example first (as graph_rag.py does)."""
        ex = self._examples.get(rid, [])
        good = [e for e in ex if e.get("isCompliant")]
        bad = [e for e in ex if not e.get("isCompliant")]
        mixed = []
        for i in range(max(len(good), len(bad))):
            if i < len(good):
                mixed.append(good[i])
            if i < len(bad):
                mixed.append(bad[i])
        return mixed if max_n is None else mixed[:max_n]
