"""Step 3 - checks of the generated text.

Reads : 01_brief.json, 02_blocks.json
Writes: 03_check_iter_NN.json (all findings) and 03_fixes_iter_NN.json (ONE merged fix set per block, fed back into step 2)
"""
from __future__ import annotations

import json

from . import headings as H
from . import store
from .checks import check_block, check_shingles
from .config import Settings
from .protected import Mask, protected_phrases
from .siblings import sibling_corpus
from .llm import LLM
from .prompts import load_consistency_prompt
from .step2 import HEADING_TAG
from .store import Run
from .textutil import count_keywords, count_words

CONSISTENCY_SCHEMA = {
    "type": "object",
    "properties": {
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"block_id": {"type": "string"}, "problem": {"type": "string"}, "fix": {"type": "string"}},
                "required": ["block_id", "problem", "fix"],
            },
        },
        "missing_data": {  # footnotes: points that cannot be fixed because the ТЗ has no data; no rewrite is requested
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"block_id": {"type": "string"}, "note": {"type": "string"}},
                "required": ["block_id", "note"],
            },
        },
    },
    "required": ["issues"],
}


def consistency_issues(brief: dict, blocks: dict[str, dict], settings: Settings, llm: LLM,
                       headings: dict[str, str] | None = None) -> tuple[list[dict], list[dict]]:
    """Returns (issues to fix, missing-data footnotes). Footnotes never trigger a rewrite."""
    page_type = brief.get("page_type", "brand-review")
    payload = {
        "page": {
            "brand": brief.get("brand", ""), "geo": brief.get("geo", ""), "language": brief.get("language", ""),
            "keywords": brief.get("keywords", []), "facts": brief.get("facts", []),
            **({} if page_type == "brand-review" else {"page_type": page_type}),
            **({"casinos_in_page_order": brief.get("casinos", [])} if page_type == "top-list" else {}),
        },
        "blocks": [
            {"id": b["id"], "level": b["level"], "heading": (headings or {}).get(b["id"], b["heading"]), "summary": b["summary"], "copywriter_notes": b["copywriter_notes"], "brand_info": {i["path"]: i["value"] for i in b.get("brand_info", [])}, "entities": [e["name"] for e in b["entities"]], "entity_connections": [f"{c['subject']} -> {c['relation']} -> {c['object']}" for c in b["entity_connections"]], "text": blocks[b["id"]]["text"]}
            for b in brief["blocks"]
        ]
    }
    res = llm.json(load_consistency_prompt(page_type), json.dumps(payload, ensure_ascii=False), CONSISTENCY_SCHEMA, settings.model_check, name="consistency")
    valid = {b["id"] for b in brief["blocks"]}
    return (
        [i for i in res["issues"] if i["block_id"] in valid],
        [m for m in res.get("missing_data", []) if m["block_id"] in valid],
    )


def run_step3(run: Run, llm: LLM, settings: Settings, iteration: int = 0) -> tuple[bool, dict[str, list[str]]]:
    brief = run.load_json(store.BRIEF)
    brief["facts"] = run.job().facts  # same context as step 2 (facts are not stored in 01_brief.json)
    brief["brand"] = run.job().brand_name
    blocks = run.load_json(store.BLOCKS)["blocks"]
    keywords, language = brief["keywords"], brief["language"]
    headings = H.load(run, brief)  # localized page headings (the brief itself is English)

    per_block: dict[str, list[dict]] = {}
    for b in brief["blocks"]:
        per_block[b["id"]] = check_block(b, blocks[b["id"]]["text"], keywords, language, settings, brief["brand"])
        for prob in H.check_heading(headings[b["id"]], b, keywords, language):  # heading problems are repaired in step 2 separately
            per_block[b["id"]].append({"check": "heading", "problem": prob,
                                       "fix": f'{HEADING_TAG} The page heading "{headings[b["id"]]}": {prob}.'})

    # technical duplicates: runs of `shingle_n` words shared with the sibling texts of the brand (names and figures of the knowledge base are exempt)
    sib = sibling_corpus(run.path)
    if sib:
        kb = run.knowledge_base()
        mask = Mask.for_kb(kb, brief["brand"]) if kb else None
        for b in brief["blocks"]:
            per_block[b["id"]] += check_shingles(b["id"], headings[b["id"]] + "\n\n" + blocks[b["id"]]["text"], run.path, settings, mask, sib)

    llm_issues, missing_data = consistency_issues(brief, blocks, settings, llm, headings)
    for i in llm_issues:
        per_block[i["block_id"]].append({"check": "consistency", "problem": i["problem"], "fix": i["fix"]})

    # the limit of the whole text (competitor median + 20%, `max_body_words` of the ТЗ): when the text is over it, the blocks that
    # went over their own maximum are shortened to it (the sum of the maxima is within the limit, so this is enough)
    limit = brief["targets"].get("max_body_words")
    counts = {b["id"]: count_words(blocks[b["id"]]["text"]) for b in brief["blocks"]}
    total_words = sum(counts.values())
    if limit and total_words > limit:
        over = [b for b in brief["blocks"] if counts[b["id"]] > b["words_max"]] or [b for b in brief["blocks"] if counts[b["id"]] > b["words"]]
        for b in sorted(over, key=lambda b: b["words_max"] - counts[b["id"]]):
            per_block[b["id"]].append({
                "check": "page_limit",
                "problem": f"the text has {total_words} words, the limit of the whole text is {limit}; this block has {counts[b['id']]} (maximum {b['words_max']})",
                "fix": f"The whole text is over its limit ({total_words} words, at most {limit}). Shorten this block to at most {b['words_max']} words "
                       f"(aim for about {b['words']}) by cutting the least important details.",
            })

    fixes = {bid: [p["fix"] for p in probs] for bid, probs in per_block.items() if probs}

    # document-level numbers for the report (informational: blocks are what gets fixed)
    all_text = "\n".join(blocks[b["id"]]["text"] for b in brief["blocks"])
    heads = "\n".join(headings.values())
    body_kw, head_kw = count_keywords(all_text, keywords), count_keywords(heads, keywords)
    summary = {
        "body_words": count_words(all_text),
        "max_body_words": limit,
        "target_body_words": brief["targets"]["target_body_words"],
        "keywords_total": {k: body_kw[k] + head_kw[k] for k in keywords},
        "keyword_targets": brief["targets"]["keyword_targets"],
    }
    passed = not fixes
    report = {"iteration": iteration, "passed": passed, "summary": summary, "blocks": per_block, "missing_data": missing_data}
    run.save_json(f"03_check_iter_{iteration:02d}.json", report)
    run.save_json(f"03_fixes_iter_{iteration:02d}.json", fixes)
    run.mark("step3", "passed" if passed else "needs_fixes", iteration=iteration, blocks_to_fix=len(fixes))

    by_check: dict[str, int] = {}
    for probs in per_block.values():
        for p in probs:
            by_check[p["check"]] = by_check.get(p["check"], 0) + 1
    print(f"  check #{iteration}: {'PASSED' if passed else f'{len(fixes)} block(s) to fix'} {by_check or ''}  words {summary['body_words']}/{summary['target_body_words']}" + (f" (limit {limit})" if limit else ""))
    return passed, fixes

