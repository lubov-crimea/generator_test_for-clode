"""Page headings.

The brief is always English, headings included. The headings that appear on the page are written in the page language, so step 2
localizes them first (one call for all headings) and saves them in 02_headings.json:

    {"language": "de", "headings": {"b01": {"en": "...", "local": "..."}, ...}}

Every localized heading must contain exactly the tracked keywords the brief planned for it (`heading_keywords`), so the keyword
totals of the whole page stay correct. Step 3 re-checks the localized headings.
"""
from __future__ import annotations

import json

from . import store
from .config import Settings
from .lang import check_language, language_name
from .llm import LLM
from .prompts import load_prompt
from .store import Run
from .textutil import count_keywords

FILE = "02_headings.json"

SCHEMA = {
    "type": "object",
    "properties": {
        "headings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"id": {"type": "string"}, "heading": {"type": "string"}},
                "required": ["id", "heading"],
            },
        }
    },
    "required": ["headings"],
}


def check_heading(local: str, b: dict, keywords: list[str], language: str) -> list[str]:
    """Problems of one localized heading: wrong keyword counts, foreign script / language."""
    problems: list[str] = []
    found = count_keywords(local, keywords)
    for k in keywords:
        need = b["heading_keywords"].get(k, 0)
        if found[k] != need:
            problems.append(f'keyword "{k}" appears {found[k]} time(s) in the heading but must appear exactly {need}')
    if not language.startswith("en"):
        bad = check_language(local, language, keywords)
        if bad:
            problems.append(f"the heading is not in {language_name(language)} ({bad[0]['reason']})")
    return problems


def load(run: Run, brief: dict) -> dict[str, str]:
    """id -> page heading. English pages use the brief headings unchanged; other languages need 02_headings.json."""
    if brief["language"].startswith("en"):
        return {b["id"]: b["heading"] for b in brief["blocks"]}
    if not run.has(FILE):
        raise RuntimeError(f"{FILE} is missing: the page headings must be localized first (run step 2).")
    data = run.load_json(FILE)["headings"]
    missing = [b["id"] for b in brief["blocks"] if b["id"] not in data]
    if missing:
        raise RuntimeError(f"{FILE} has no heading for {', '.join(missing)}: run step 2.")
    return {b["id"]: data[b["id"]]["local"] for b in brief["blocks"]}


def localize(run: Run, brief: dict, llm: LLM, settings: Settings, only: list[str] | None = None,
             problems: dict[str, list[str]] | None = None, max_attempts: int = 3) -> dict[str, str]:
    """Create or repair the page headings. `only` = ids to (re)do, `problems` = id -> fix instructions from step 3."""
    language = brief["language"]
    if language.startswith("en"):
        return load(run, brief)
    keywords = brief["keywords"]
    saved = run.load_json(FILE) if run.has(FILE) else {"language": language, "headings": {}}
    heads: dict[str, dict] = saved["headings"]
    by_id = {b["id"]: b for b in brief["blocks"]}
    todo = list(only) if only else [i for i in by_id if i not in heads or heads[i]["en"] != by_id[i]["heading"]]
    feedback = {i: list((problems or {}).get(i, [])) for i in todo}

    for attempt in range(1, max_attempts + 1):
        if not todo:
            break
        items = [
            {
                "id": i, "level": by_id[i]["level"], "english_heading": by_id[i]["heading"],
                "keywords_the_heading_must_contain": {k: n for k, n in by_id[i]["heading_keywords"].items() if n},
                **({"current_heading": heads[i]["local"]} if i in heads else {}),
                **({"problems_to_fix": feedback[i]} if feedback.get(i) else {}),
            }
            for i in todo
        ]
        user = (
            f"Page language: {language_name(language)} ({language}). GEO: {brief['geo']}.\n"
            f"All tracked keywords: {', '.join(keywords)}\n\nHeadings to localize:\n" + json.dumps(items, ensure_ascii=False, indent=1)
        )
        res = llm.json(load_prompt("step2_headings"), user, SCHEMA, settings.model_generation, name="headings")
        answers = {h["id"]: h["heading"].strip() for h in res["headings"] if h["id"] in by_id}
        still = []
        for i in todo:
            local = answers.get(i, "")
            errs = check_heading(local, by_id[i], keywords, language) if local else ["no heading returned"]
            if errs:
                feedback[i] = errs
                still.append(i)
            else:
                heads[i] = {"en": by_id[i]["heading"], "local": local}
        run.save_json(FILE, {"language": language, "headings": heads})
        todo = still
    if todo:
        raise RuntimeError("Could not localize headings: " + "; ".join(f"{i}: {feedback[i]}" for i in todo))
    return load(run, brief)
