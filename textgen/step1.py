"""Step 1 - competitor analysis and the ТЗ (brief).

Reads : 00_input.json
Writes: 01_competitors_raw.json, 01_keyword_stats.json, 01_heading_clusters.json, 01_brief.json, 01_brief.md
"""
from __future__ import annotations

import json
from pathlib import Path

from . import brief as B
from . import store
from .analysis import cluster_headings, fact_table_summary, keyword_stats, mine_entities, usable_pages
from .config import ROOT, Settings
from .fetcher import fetch_competitor
from .lang import language_from_geo, language_name
from .llm import LLM
from . import kb as KB
from .prompts import load_step1_prompt
from .sitemap import attach_internal_links, site_pages_for
from .store import Run
from .tiers import describe

MAX_BRIEF_ATTEMPTS = 3
MAX_REVIEW_ROUNDS = 2


def _resolve_language(run: Run, llm: LLM, settings: Settings) -> str:
    job = run.job()
    if job.language:
        return job.language
    code = language_from_geo(job.geo)
    if not code:
        code = llm.text(
            "Answer with one lowercase ISO 639-1 code only (e.g. en, de, pt).",
            f"Main language of online-casino/affiliate content for the GEO: {job.geo}",
            settings.model_analysis,
            max_tokens=10,
        ).strip().lower()[:5]
    data = run.load_json(store.INPUT)
    data["language"] = code
    run.save_json(store.INPUT, data)
    return code


def _compact_clusters(clusters: list[dict]) -> list[dict]:
    return [
        {
            "id": c["id"], "canonical_title": c["canonical_title"], "topic": c["topic"], "frequency": c["frequency"],
            "mandatory": c["mandatory"], "levels": c["levels"], "avg_section_words": c["avg_section_words"],
            "avg_position": c["avg_position"], "examples": [e["text"] for e in c["examples"][:4]],
        }
        for c in clusters
    ]


def _brief_context(run: Run, stats: dict, clusters: list[dict], targets: dict, kb: dict | None = None) -> dict:
    job = run.job()
    raw = usable_pages(run.load_json(store.COMPETITORS_RAW))
    review = job.page_type == "brand-review"
    top_list = job.page_type == "top-list"
    return {
        "geo": job.geo,
        "page_language": language_name(job.language),
        **({} if review else {"page_type": job.page_type}),
        **({"brand": job.brand_name} if job.page_type == "brand-subpage" else {}),
        **({"casinos_in_ranking_order": [{"slug": c["slug"], "name": c["name"]} for c in job.casinos]} if top_list else {}),
        "keywords": job.keywords,
        "facts_to_respect": job.facts,
        # a top list carries the knowledge bases of several casinos: values are shortened here, the code inserts the full ones by path
        "knowledge_base": ({"title": kb["title"], "variables": KB.digest(kb["variables"]) if top_list else kb["variables"]} if kb else None),
        "competitor_h1": [next((h["text"] for h in p["headings"] if h["level"] == 1), "") for p in raw if p.get("ok")],
        "competitor_stats": [
            {
                "url": r["url"], "body_words": r["body_words"],
                "keywords_in_total": r["total"], "keywords_in_h1": r["headings_by_level"]["1"],
                "keywords_in_h2": r["headings_by_level"]["2"],
            }
            for r in stats["competitors"]
        ],
        "targets": {"target_body_words": targets["target_body_words"], "competitor_body_words": targets["competitor_body_words"],
                    "max_body_words": targets["max_body_words"], "keyword_targets": targets["keyword_targets"]},
        "heading_clusters": _compact_clusters(clusters),
        "entity_candidates": [{"entity": e["entity"], "competitors": e["competitors"]} for e in run.load_json(store.ENTITIES)[:60]],
        **({  # the brand fact sheet is built from the knowledge base only
            "fact_table_requirements": {
                "position": "the 2nd or the 3rd block of the page, level 2, formats [\"table\"], `fact_table` rows set",
                "required_row_keys": B.REQUIRED_FACT_ROWS,
                "allowed_row_keys": B.FACT_ROW_KEYS,
                "max_rows": B.FACT_TABLE_MAX_ROWS,
            },
            "competitor_fact_tables": run.load_json(store.FACT_TABLES) if run.has(store.FACT_TABLES) else {"tables": [], "labels": []},
        } if kb and review else {}),
    }


def _generate_brief(ctx: dict, targets: dict, job, settings: Settings, llm: LLM, clusters: list[dict],
                    kb: dict | None = None) -> tuple[dict, list[str]]:
    system = load_step1_prompt("brief", job.page_type)
    user = json.dumps(ctx, ensure_ascii=False, indent=1)
    errors: list[str] = []
    brief: dict = {"blocks": []}
    for attempt in range(1, MAX_BRIEF_ATTEMPTS + 1):
        msg = user
        if errors:
            msg += "\n\nYour previous answer had these problems, fix them all:\n- " + "\n- ".join(errors)
            msg += "\n\nPrevious answer:\n" + json.dumps(brief, ensure_ascii=False)
        brief = B.normalize(llm.json(system, msg, B.BRIEF_SCHEMA, settings.model_analysis, name="brief"), job.keywords, kb)
        errors = B.validate(brief, targets, job.keywords, settings, clusters, kb, job.page_type, job.casinos)
        if not errors:
            return brief, []
    # keyword sums are arithmetic - fix them in code instead of failing the run
    B.rebalance_keywords(brief, targets, job.keywords)
    return brief, B.validate(brief, targets, job.keywords, settings, clusters, kb, job.page_type, job.casinos)


def _review(brief: dict, targets: dict, job, settings: Settings, llm: LLM, clusters: list[dict],
            kb: dict | None = None) -> tuple[dict, list[dict]]:
    all_issues: list[dict] = []
    system = load_step1_prompt("review", job.page_type)
    for _ in range(MAX_REVIEW_ROUNDS):
        user = json.dumps({"targets": targets, "brief": brief}, ensure_ascii=False)
        res = llm.json(system, user, B.REVIEW_SCHEMA, settings.model_check, name="review")
        issues = res.get("issues", [])
        if not issues:
            break
        all_issues += issues
        cand = B.normalize({**brief, "blocks": res["blocks"]}, job.keywords, kb)
        errs = B.validate(cand, targets, job.keywords, settings, clusters, kb, job.page_type, job.casinos)
        if errs:  # the reviewer broke a rule: keep the previous brief (no silent keyword shuffling)
            all_issues.append({"problem": "reviewer output rejected by validation", "fix": "; ".join(errs)})
            break
        brief = cand
    return brief, all_issues


def run_step1(run: Run, llm: LLM, settings: Settings, html_dir: Path | None = None, words: int | None = None, force: bool = False) -> dict:
    job = run.job()
    job.language = _resolve_language(run, llm, settings)
    html_dir = html_dir or (ROOT / "input" / "html")

    # 1.0 knowledge base with the brand information (selected by name in the input, fetched from AffBulk MCP)
    kb = run.knowledge_base()
    print(f"  page type: {job.page_type}")
    if kb and job.page_type == "top-list":
        print(f"  knowledge bases: {', '.join(c['name'] + ' (' + c['knowledge_base'] + ')' for c in job.casinos)}")
    elif kb:
        print(f"  knowledge base: {kb['title']} (id {kb['id']}), {len(kb['variables'])} variables")

    # 1.1 download + parse competitors
    if force or not run.has(store.COMPETITORS_RAW):
        pages = [fetch_competitor(u, html_dir if html_dir.exists() else None) for u in job.competitors]
        run.save_json(store.COMPETITORS_RAW, pages)
    pages = usable_pages(run.load_json(store.COMPETITORS_RAW))
    for p in pages:
        print(f"  {'OK ' if p.get('ok') else 'FAIL'} {p['url']}  words={p['word_count']}  headings={len(p['headings'])}  {p.get('error', '')}")

    # 1.1 keyword occurrences
    stats = keyword_stats(pages, job.keywords)
    run.save_json(store.KEYWORD_STATS, stats)

    # 1.1 entity candidates (names/terms competitors talk about)
    run.save_json(store.ENTITIES, mine_entities(pages, job.keywords))

    # 1.1 brand fact sheets of the competitors (label | value tables): the model picks the rows of our fact table from them
    facts = fact_table_summary(pages)
    run.save_json(store.FACT_TABLES, facts)
    print(f"  competitor fact tables: {len(facts['tables'])}" + ("" if facts["tables"] else " (none found: the required rows are used)"))
    if not kb:
        print("  WARNING: no knowledge base: " + (
            "the brand fact table needs it and is NOT added (add `Knowledge Base - <name>` to the input)" if job.page_type == "brand-review"
            else "the page will carry no brand facts (add `Knowledge Base - <name>` to the input)"))

    # 1.2 heading clusters
    if force or not run.has(store.CLUSTERS):
        run.save_json(store.CLUSTERS, cluster_headings(pages, settings, llm))
    clusters = run.load_json(store.CLUSTERS)
    print(f"  clusters: {len(clusters)} ({sum(c['mandatory'] for c in clusters)} mandatory)")

    # 1.3-1.4 structure + parameters per heading
    targets = B.compute_targets(stats, job.keywords, settings, words)
    run.save_json(store.TIERS, targets["tiers"])
    print("  size groups of the competitors (the base ТЗ is built for 'medium'):\n    " + describe(targets["tiers"]).replace("\n", "\n    "))
    ctx = _brief_context(run, stats, clusters, targets, kb)
    brief, errors = _generate_brief(ctx, targets, job, settings, llm, clusters, kb)
    if errors:
        run.save_json(store.BRIEF, {"targets": targets, "brief": brief, "validation_errors": errors})
        raise RuntimeError("ТЗ did not pass validation:\n- " + "\n- ".join(errors))

    # 1.5 consistency review of the whole ТЗ
    brief, issues = _review(brief, targets, job, settings, llm, clusters, kb)

    # 1.6 room for the content: the facts and connections of a block get the words they need (the competitor-based size stays the
    # minimum, the growth and the limit of the whole text are checked by `validate`)
    budget = B.apply_coverage_budget(brief, targets, settings)
    print(f"  limit of the whole text: {targets['max_body_words']} words ({B._limit_note(targets)})")
    if budget:
        print(f"  coverage budget: {len(budget)} block(s) enlarged, body {targets['base_body_words']} -> {targets['target_body_words']} words")
        for r in budget:
            print(f"    {r['id']} {r['heading'][:40]!r}: needs {r['need']} words ({r['facts']} facts + {r['connections']} connections), {r['from'][0]}-{r['from'][1]} -> {r['to'][0]}-{r['to'][1]}")

    # 1.7 internal links: every internal page of the site is planted in the block where its topic comes up (anchors of at most 3 words)
    pages = site_pages_for(job)
    if pages:
        placed = attach_internal_links(brief, pages, required=job.page_type == "brand-review")
        brief["site_pages"] = pages
        print(f"  internal links: " + ", ".join(f"/{s} -> {placed[s]}" for s in pages if s in placed)
              + ("" if len(placed) == len(pages) else f"  (no block for: {', '.join(s for s in pages if s not in placed)})"))

    result = {
        "geo": job.geo, "language": job.language, "keywords": job.keywords, "targets": targets, "brand": job.brand_name,
        **({"site_pages": pages} if pages else {}),
        "knowledge_base": {"id": kb["id"], "title": kb["title"]} if kb else None,
        **({} if job.page_type == "brand-review" else {
            "page_type": job.page_type, "skipped_clusters": brief.get("skipped_clusters", []),
            **({"casinos": [{"slug": c["slug"], "name": c["name"]} for c in job.casinos]} if job.page_type == "top-list" else {}),
        }),
        "intent_summary": brief.get("intent_summary", ""), "blocks": brief["blocks"], "review_issues": issues,
        "coverage_budget": budget,
    }
    run.save_json(store.BRIEF, result)
    run.save_text(store.BRIEF_MD, B.render_markdown(
        brief, {"geo": job.geo, "language": job.language, "knowledge_base": kb["title"] if kb else None, "page_type": job.page_type}, targets))
    run.mark("step1", "done", blocks=len(brief["blocks"]))
    print(f"  ТЗ: {len(brief['blocks'])} blocks, {sum(b['words'] for b in brief['blocks'])} words -> {store.BRIEF_MD}")
    return result


