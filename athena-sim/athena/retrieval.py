"""The four ways Athena Sim can give the LLM a coding standard (RQ3 conditions).

  none     the standard is only *named*; the LLM must rely on what it already knows
  fulldoc  the whole standard is pasted into the prompt (how Cursor/Copilot rule files are used)
  chunk    plain RAG, the design the original Athena pilot started from: the standard is cut into
           chunks and the top-k chunks most similar to the code are retrieved (lexical TF-IDF here,
           because the embedding model used in the pilot is unknown and no network is needed)
  graph    ontology-guided Graph RAG: only the rules that APPLIES_TO this language + identifier kind,
           ranked by severity/specificity, with few-shot examples (the journal paper's method)
  graph_noex  ablation (2026-10-02, see ablation_noex/ADDENDUM.md): exactly the graph block without the
           few-shot examples, to separate the effect of rule selection from that of the examples
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field

from .ontology import render_rule

CONDITIONS = ("none", "fulldoc", "chunk", "graph", "graph_noex")

_STOP = set("""a an and are as at be by for from has have if in into is it its of on or that the this to
use used uses using with should shall must may can not no all any each when than then else also only
name names named code""".split())


def words(text: str) -> list:
    """Split identifiers (snake/camel) and prose into lower-case word tokens."""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    toks = re.findall(r"[A-Za-z][A-Za-z0-9]+", text.replace("_", " "))
    return [t.lower() for t in toks if t.lower() not in _STOP and len(t) > 1]


class ChunkIndex:
    """Tiny TF-IDF cosine index over (chunk_id, text) pairs."""

    def __init__(self, chunks: list):
        self.chunks = chunks
        self.tf = [Counter(words(t)) for _, t in chunks]
        n = len(chunks)
        df = Counter()
        for c in self.tf:
            df.update(c.keys())
        self.idf = {w: math.log((n + 1) / (d + 1)) + 1.0 for w, d in df.items()}
        self.norm = [math.sqrt(sum((v * self.idf[w]) ** 2 for w, v in c.items())) or 1.0 for c in self.tf]

    def top(self, query_tokens: list, k: int) -> list:
        q = Counter(query_tokens)
        qn = math.sqrt(sum((v * self.idf.get(w, 1.0)) ** 2 for w, v in q.items())) or 1.0
        scored = []
        for i, c in enumerate(self.tf):
            dot = sum(v * self.idf.get(w, 1.0) * c[w] * self.idf.get(w, 1.0) for w, v in q.items() if w in c)
            scored.append((dot / (qn * self.norm[i]), i))
        scored.sort(key=lambda x: (-x[0], x[1]))
        return [i for s, i in scored[:k] if s > 0]


@dataclass
class Context:
    text: str
    meta: dict = field(default_factory=dict)


class Retriever:
    def __init__(self, pack, chunk_k: int = 3, top_k: int | None = None, n_examples: int = 2):
        self.pack, self.chunk_k, self.top_k, self.n_examples = pack, chunk_k, top_k, n_examples
        self._idx: dict = {}

    def _chunk_index(self, sid):
        if sid not in self._idx:
            self._idx[sid] = ChunkIndex(self.pack.chunks(sid))
        return self._idx[sid]

    def context(self, condition: str, *, task: str, standard_id: str, language: str, kind: str,
                name: str, code: str) -> Context:
        pack, onto = self.pack, self.pack.ontology
        sname = pack.standard_name(standard_id)
        if condition == "none":
            return Context(f"The team follows: {sname}.\nThe text of the standard is NOT provided - "
                           f"apply it from your own knowledge of it.", {"n_items": 0})
        if condition == "fulldoc":
            text = pack.fulltext(standard_id)
            return Context(f"{sname} - complete text:\n{text}", {"n_items": 1, "chars": len(text)})
        if condition == "chunk":
            idx = self._chunk_index(standard_id)
            q = words(f"{language} {kind} {kind} {kind} {name} {name}") + words(code)
            hits = idx.top(q, self.chunk_k)
            ids = [idx.chunks[i][0] for i in hits]
            body = "\n\n".join(idx.chunks[i][1] for i in hits) or "(no matching passage found)"
            return Context(f"{sname} - the {len(hits)} passage(s) most similar to the code:\n{body}",
                           {"n_items": len(hits), "retrieved_ids": ids})
        if condition in ("graph", "graph_noex"):
            n_ex = 0 if condition == "graph_noex" else self.n_examples
            types = ("NamingRule",) if task == "rename" else ("CommentRule", "StructureRule")
            rules = onto.rules_for(language, kind, types=types, standard_id=standard_id)
            if self.top_k:
                rules = rules[: self.top_k]
            if not rules:
                return Context(f"{sname}: the ontology holds no specific rule for a {kind} in {language}; "
                               f"apply the general conventions of the standard.", {"n_items": 0, "retrieved_ids": []})
            body = "\n\n".join(render_rule(r, onto.examples(r["id"], n_ex) if n_ex else None)
                               for r in rules)
            return Context(f"{sname} - rules retrieved for a {kind} in {language} (most important first):\n{body}",
                           {"n_items": len(rules), "retrieved_ids": [r["id"] for r in rules]})
        raise ValueError(f"unknown condition {condition!r}; choose from {CONDITIONS}")
