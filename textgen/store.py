"""A run is a folder in runs/<slug>/. Every step writes its result there and the next step reads it back."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from .config import RUNS_DIR
from .inputs import Job

INPUT = "00_input.json"
KNOWLEDGE_BASE = "00_knowledge_base.json"  # fetched from AffBulk through MCP (see textgen/kb.py)
KNOWLEDGE_BASES_DIR = "00_kb"  # top list: one knowledge base per casino, <casino slug>.json
COMPETITORS_RAW = "01_competitors_raw.json"
KEYWORD_STATS = "01_keyword_stats.json"
CLUSTERS = "01_heading_clusters.json"
ENTITIES = "01_entity_candidates.json"
TIERS = "01_tiers.json"  # size groups of the competitors: mean and limit of the small / medium / large text (textgen/tiers.py)
FACT_TABLES = "01_fact_tables.json"  # brand fact sheets of the competitors (label | value tables)
BRIEF = "01_brief.json"
BRIEF_MD = "01_brief.md"
BLOCKS = "02_blocks.json"
TEXT_DRAFT = "02_text_draft.md"
FINAL_TXT = "04_final.txt"
FINAL_JSON = "04_final.json"
STATE = "state.json"


class Run:
    def __init__(self, path: Path):
        self.path = path
        self.path.mkdir(parents=True, exist_ok=True)

    @classmethod
    def create(cls, slug: str, job: Job) -> "Run":
        run = cls(RUNS_DIR / slug)
        run.save_json(INPUT, job.to_dict())
        return run

    @classmethod
    def open(cls, name_or_path: str) -> "Run":
        p = Path(name_or_path)
        if not p.exists():
            p = RUNS_DIR / name_or_path
        if not (p / INPUT).exists():
            raise FileNotFoundError(f"Run not found: {name_or_path}")
        return cls(p)

    # --- files ---
    def has(self, name: str) -> bool:
        return (self.path / name).exists()

    def save_json(self, name: str, data: Any) -> Path:
        p = self.path / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return p

    def load_json(self, name: str) -> Any:
        return json.loads((self.path / name).read_text(encoding="utf-8"))

    def save_text(self, name: str, text: str) -> Path:
        p = self.path / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def load_text(self, name: str) -> str:
        return (self.path / name).read_text(encoding="utf-8")

    def job(self) -> Job:
        return Job(**self.load_json(INPUT))

    def knowledge_base(self) -> dict | None:
        """The brand knowledge base chosen in the input (None when the input names none).

        The file is saved from AffBulk MCP (knowledge_bases_find); a missing or mismatching file is an error, never a silent fallback.
        """
        from . import kb as KB

        job = self.job()
        if job.page_type == "top-list":
            return self._casino_knowledge_bases(job)
        name = job.knowledge_base
        if not name:
            return None
        if not self.has(KNOWLEDGE_BASE):
            raise RuntimeError(
                f'Input names the knowledge base "{name}" but {self.path / KNOWLEDGE_BASE} does not exist. '
                "Find it in AffBulk (MCP knowledge_bases_find, filter title) and save the result there."
            )
        kb = KB.load(self.load_json(KNOWLEDGE_BASE))
        if kb["title"] != name:
            raise RuntimeError(f'{KNOWLEDGE_BASE} holds "{kb["title"]}", but the input asks for "{name}".')
        return kb

    def _casino_knowledge_bases(self, job: Job) -> dict:
        """Top list: one knowledge base per casino, saved from AffBulk as runs/<run>/00_kb/<casino slug>.json (same format as
        00_knowledge_base.json) and merged into one (see `kb.merge`)."""
        from . import kb as KB

        missing = [c for c in job.casinos if not self.has(f"{KNOWLEDGE_BASES_DIR}/{c['slug']}.json")]
        if missing:
            raise RuntimeError(
                "Knowledge bases of the casinos are missing. Find each in AffBulk (MCP knowledge_bases_find, filter title) and save the result there:\n"
                + "\n".join(f'  "{c["knowledge_base"]}" ({c["name"]}) -> {self.path / KNOWLEDGE_BASES_DIR / (c["slug"] + ".json")}' for c in missing)
            )
        parts: dict[str, dict] = {}
        for c in job.casinos:
            name = f"{KNOWLEDGE_BASES_DIR}/{c['slug']}.json"
            kb = KB.load(self.load_json(name))
            if kb["title"] != c["knowledge_base"]:
                raise RuntimeError(f'{name} holds "{kb["title"]}", but the input asks for "{c["knowledge_base"]}".')
            parts[c["slug"]] = kb
        return KB.merge(parts, "top-list: " + ", ".join(c["name"] for c in job.casinos))

    # --- progress log ---
    def mark(self, step: str, status: str, **extra: Any) -> None:
        state = self.load_json(STATE) if self.has(STATE) else {}
        state[step] = {"status": status, "at": datetime.now().isoformat(timespec="seconds"), **extra}
        self.save_json(STATE, state)

