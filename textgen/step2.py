"""Step 2 - text generation, one call per heading (block), using the user's system prompt.

Reads : 01_brief.json (+ 03 fixes when re-generating)
Writes: 02_blocks.json (current text of every block), 02_text_draft.md (assembled text), 02_history/*.json
"""
from __future__ import annotations

import re

from . import store
from .config import Settings
from .lang import language_name
from .llm import LLM
from .prompts import load_writer_prompt
from .store import Run
from .textutil import HEADING_RE
from . import headings as H
from . import kb as KB
from .brief import FACT_TABLE_VALUE_MAX_WORDS, block_cap, brand_info_hazards, home_link_note, visual_elements
from .sitemap import internal_link_note
from .checks import brand_free_max
from .textutil import is_brand_keyword
from .paraphrase import Cards, load_bank, slot_of
from .protected import Mask, protected_phrases
from .shingles import taken_phrases
from .siblings import sibling_corpus

HEADING_TAG = "[heading]"  # prefix of step-3 fix instructions that concern the page heading, not the body
FENCE_RE = re.compile(r"^```[a-zA-Z]*\n|\n```\s*$")

_CARDS: Cards | None = None  # fact cards of the run being written (paraphrase.py); None = the knowledge base reaches the writer verbatim
_TAKEN: list[str] = []  # word sequences that sibling texts already use (shingles.taken_phrases)


def prepare_cards(run: Run, brief: dict, settings: Settings) -> None:
    """Sets the fact cards (a bank of paraphrases exists for the knowledge base) and the phrases taken by sibling texts for this run."""
    global _CARDS, _TAKEN
    _CARDS, _TAKEN = None, []
    kb = run.knowledge_base()
    if not kb:
        return
    mask = Mask.for_kb(kb, brief.get("brand", ""))
    bank = load_bank(kb["title"])
    if bank["items"] or settings.require_bank:
        _CARDS = Cards(kb, mask, bank, slot_of(brief), seed=run.path.name, require=settings.require_bank)
    sib = sibling_corpus(run.path)
    if sib:
        _TAKEN = taken_phrases(sib, settings.shingle_n, mask=mask)


def _taken_section(n: int = 9) -> str:
    if not _TAKEN:
        return ""
    return (
        "## TAKEN PHRASES\n"
        f"Sibling pages of this brand already use the word sequences below (lower-case, punctuation removed). A technical duplicate is any run of {n} "
        "or more words that another page shares, so none of these sequences may appear in your text, not even lightly edited. Names, figures, "
        "periods and other exact facts stay as given, but the words around them must be your own:\n"
        + "\n".join(f"- {p}" for p in _TAKEN[:40])
    )


def clean_output(text: str, heading: str) -> str:
    text = FENCE_RE.sub("", text.strip()).strip()
    lines = text.splitlines()
    if lines and HEADING_RE.match(lines[0]) and re.sub(r"^#+\s*", "", lines[0]).strip().lower() == heading.strip().lower():
        lines = lines[1:]  # the model repeated the heading we add ourselves
    return "\n".join(lines).strip()


def assemble(brief_blocks: list[dict], blocks: dict[str, dict], headings: dict[str, str] | None = None) -> str:
    """Page text. `headings` = localized page headings (id -> heading); the brief's English headings are the fallback."""
    parts = []
    for b in brief_blocks:
        parts.append("#" * b["level"] + " " + (headings or {}).get(b["id"], b["heading"]))
        parts.append(blocks[b["id"]]["text"] if b["id"] in blocks else "")
    return "\n\n".join(parts).strip() + "\n"


def _h(b: dict, headings: dict[str, str] | None) -> str:
    return (headings or {}).get(b["id"], b["heading"])


def _outline(brief_blocks: list[dict], headings: dict[str, str] | None = None) -> str:
    """The structure of the page: every block with its heading, word range and summary, so that a block knows what comes before and after."""
    return "\n".join(
        f'{b["id"]} {"  " * (b["level"] - 1)}H{b["level"]} {_h(b, headings)} ({b["words_min"]}-{b["words_max"]} words): {b["summary"]}'
        for b in brief_blocks
    )


SECTION_MARK_RE = re.compile(r"^={3}\s*(b\d+)\s*={3}\s*$", re.MULTILINE)


def sections(brief_blocks: list[dict]) -> list[list[dict]]:
    """Units of generation: the H1 block alone, every H2 together with all its deeper blocks (H3...), written in one call."""
    groups: list[list[dict]] = []
    for b in brief_blocks:
        if b["level"] <= 2 or not groups:
            groups.append([b])
        else:
            groups[-1].append(b)
    return groups


def parse_section(raw: str, ids: list[str]) -> dict[str, str]:
    """Split the answer of a section call at the `=== bNN ===` markers. Only the expected ids are returned."""
    parts = SECTION_MARK_RE.split(raw)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2) if parts[i] in ids and parts[i + 1].strip()}


def _context(brief: dict) -> str:
    facts = "\n".join(f"- {f}" for f in brief.get("facts", []))
    if brief.get("knowledge_base"):
        how = "as a fact card" if _CARDS else "verbatim"
        facts = (facts + "\n" if facts else "") + (
            f'- The brand facts for each block are given in its BLOCK BRIEF under "Brand Information" '
            f'({how} from the AffBulk knowledge base "{brief["knowledge_base"]["title"]}"). Use only those facts for brand-specific claims.'
        )
    facts = facts or (
        "None provided. State NO brand-specific facts (numbers, amounts, licences, providers, payment methods, dates). "
        "Use safe general wording, or the 'not specified' cell value in tables."
    )
    page_type = brief.get("page_type", "brand-review")
    if page_type == "top-list":
        brand = "Brand: none. This page ranks several casinos (see below); no brand name is tracked, so every keyword count of the block brief is exact\n"
    else:
        brand = (f'Brand: {brief["brand"]} (this name and its spellings are tracked keywords: the block brief gives the exact count; '
                 "where it says 0 the brand name is free to use)\n")
    kind = {
        "brand-subpage": "Page type: focused page of the brand about ONE topic (not the general review of the brand)\n",
        "top-list": "Page type: top list, a ranking page of several casinos\n",
    }.get(page_type, "")
    casinos = ""
    if page_type == "top-list":
        casinos = ("Casinos on this page, in page order (this order is the ranking; the Brand Information paths of a casino start with its slug, "
                   "use the casino name exactly as listed):\n"
                   + "\n".join(f'{n}. {c["name"]} (slug `{c["slug"]}`)' for n, c in enumerate(brief.get("casinos", []), 1)) + "\n")
    return (
        "## CONTEXT\n"
        + brand
        + f'Country / GEO: {brief["geo"]}\n'
        f'Language: {language_name(brief["language"])} ({brief["language"]}). Write ONLY in this language.\n'
        f'Page intent: {brief.get("intent_summary", "")}\n'
        + kind
        + f'All tracked keywords: {", ".join(brief["keywords"])}\n'
        + casinos
        + f"Information about the brand to use:\n{facts}"
    )


def _brand_info(b: dict, brand: str = "") -> str:
    """Verbatim knowledge-base facts selected by the ТЗ for this block."""
    if not b.get("brand_info"):
        return "\nBrand Information: none for this block. State no brand-specific facts here; use safe general wording."
    if _CARDS:
        items = "\n".join(f"- {i['path']}: {_CARDS.render_value(i['path'], i['value'])}{_CARDS.keep_line(i['value'])}" for i in b["brand_info"])
        out = ("\nBrand Information (fact card from the knowledge base; the ONLY source of brand-specific facts for this block). Names, figures, "
               "periods and short values are exact: keep them as written. Every sentence is given in an alternative wording: state it in your "
               f"own words, never copy a sentence of this card, and write list items in your own order and phrasing:\n{items}")
    else:
        items = "\n".join(f"- {i['path']}: {KB.render_value(i['value'])}" for i in b["brand_info"])
        out = f"\nBrand Information (verbatim from the knowledge base; the ONLY source of brand-specific facts for this block):\n{items}"
    hazards = {k: n for k, n in brand_info_hazards(b, list(b["keywords"])).items()
               if b["keywords"].get(k, 0) or not is_brand_keyword(k, brand)}  # the brand name is free where the block allows 0
    if hazards:
        allowed = {k: n for k, n in b["keywords"].items() if n}
        out += (
            "\nCounting warning: the facts above contain tracked keywords "
            + ", ".join(f'"{k}" (x{n})' for k, n in hazards.items())
            + ". Names, domains, e-mail addresses and sentences copied from them count as keyword occurrences (for example "
            "'incaspin.com', 'Incaspin Originals', 'support@incaspin.com'). Do not copy such wording unless it is exactly one of the "
            f"permitted uses of this block ({allowed or 'none'}); otherwise paraphrase ('the website', 'your account', 'the casino's own games')."
        )
    return out


def _fact_table(b: dict) -> str:
    """The brand fact sheet: which rows, in which order, and the verbatim values each row is built from."""
    if not b.get("fact_table"):
        return ""
    rows = []
    render = (lambda p, v: _CARDS.render_value(p, v)) if _CARDS else (lambda p, v: KB.render_value(v))
    hdr = " | ".join(_CARDS.header_pair()) if _CARDS else "Parameter | Details"
    for n, r in enumerate(b["fact_table"], 1):
        vals = " | ".join(f"{v['path']} = {render(v['path'], v['value'])}" for v in r.get("values", [])) or "NO VALUE (write the 'not specified' cell value)"
        rows.append(f'{n}. {r["label"]} [{r["key"]}]: {vals}')
    return (
        "\n\nFact Table (this block is the brand fact sheet of the page; the Brand Information above is its source):\n"
        f"Output ONE Markdown table with exactly two columns: a header row in the output language (for example '{hdr}'), "
        "the separator row, then exactly the rows listed below, in this order, one table row per line, no row added, merged or dropped. "
        "Left cell: the row label translated into the output language. Right cell: a SHORT fact built only from that row's values: "
        f"a figure, a name or a comma-separated list, at most {FACT_TABLE_VALUE_MAX_WORDS} words, no full sentences, no explanations, no conditions. "
        "Keep figures, names and e-mail addresses exactly as given. Choose the most important items when a row has many: "
        "licence = authority, licence number, jurisdiction; welcome bonus = maximum amount and number of free spins; "
        "cashback = percentage and its base; payment methods and currencies = names only; languages = the languages; support = the e-mail "
        "(add the 24/7 availability only if it is part of the row's values). No text before or after the table.\n"
        + "\n".join(rows)
    )


def _spec(b: dict, brief: dict, settings: Settings, headings: dict[str, str] | None = None, together: bool = False) -> str:
    lo, hi = b["words_min"], b["words_max"]
    cap = block_cap(b, settings)
    brand = brief.get("brand", "")
    free_max = brand_free_max(lo, settings)
    kw_lines = "\n".join(
        f'- "{k}": exactly {n} time(s)' if n else
        (f'- "{k}": 0 here, but the brand name may appear when the text reads naturally: at most {free_max} time(s) in this block '
         f'(one per {settings.brand_free_words} words)' if is_brand_keyword(k, brand) else f'- "{k}": 0 (do not use)')
        for k, n in b["keywords"].items()
    )
    ents = "\n".join(f'- {e["name"]} [{e["priority"]}]' for e in b["entities"])
    conns = "\n".join(f'- {c["subject"]} → {c["relation"]} → {c["object"]} [{c["priority"]}]' for c in b["entity_connections"])
    idx = brief["blocks"].index(next(x for x in brief["blocks"] if x["id"] == b["id"]))
    subs = []
    for c in brief["blocks"][idx + 1:]:
        if c["level"] <= b["level"]:
            break
        subs.append(f'{c["id"]} H{c["level"]} "{_h(c, headings)}"')
    parent = next((x for x in reversed(brief["blocks"][:idx]) if x["level"] < b["level"]), None)
    place = f'under H{parent["level"]} "{_h(parent, headings)}"' if parent else "page title"
    visual = visual_elements(b, brief["blocks"])
    return (
        "## BLOCK BRIEF\n"
        f'Block: {b["id"]}, H{b["level"]} "{b["heading"]}" ({place})\n'
        + (f'Page heading (output language): "{_h(b, headings)}"\n' if _h(b, headings) != b["heading"] else "")
        + "Write ONLY the body text under this heading. Do not output the heading itself.\n"
        + ((f'Sub-sections written in the same answer (lead into them, but do NOT cover their facts here): {"; ".join(subs)}\n' if together
            else f'Sub-sections written separately (do NOT cover their topics here): {"; ".join(subs)}\n') if subs else "")
        + f'Word Count: {lo}-{hi} words (body only, heading excluded). If the facts, the entities and a natural style need more room, '
        f'go over {hi}, but never beyond {cap} words.\n'
        f'Format: {" + ".join(b["formats"])}. Visual Elements: {visual}\n'
        f'Keywords (case-insensitive, whole words, longest match first; use each EXACTLY this many times; '
        f'a grammatical form of the keyword (case ending, plural) counts as the keyword):\n{kw_lines}\n'
        f'Entities to cover [priority 1-10]:\n{ents}\n'
        f'Entity Connections to state explicitly [priority]:\n{conns}\n'
        f'Summary: {b["summary"]}\n'
        f'Copywriter Notes: {b["copywriter_notes"]}'
        + (f"\n{home_link_note(brief)}" if b["level"] == 1 and home_link_note(brief) else "")
        + (f"\n{internal_link_note(b)}" if b.get("internal_links") else "")
        + _brand_info(b, brand)
        + _fact_table(b)
    )


def build_user_message(b: dict, brief: dict, blocks: dict[str, dict], settings: Settings, fixes: list[str] | None = None,
                       headings: dict[str, str] | None = None) -> str:
    parts = [_context(brief), f'## PAGE STRUCTURE FOR CONTEXT\n{_outline(brief["blocks"], headings)}']
    written = [
        f'{"#" * x["level"]} {_h(x, headings)}\n{blocks[x["id"]]["text"]}'
        for x in brief["blocks"] if x["id"] != b["id"] and x["id"] in blocks and blocks[x["id"]]["text"]
    ]
    if written:
        parts.append("## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)\n\n" + "\n\n".join(written))
    if _taken_section(settings.shingle_n):
        parts.append(_taken_section(settings.shingle_n))
    parts.append(_spec(b, brief, settings, headings))
    if fixes:
        cur = blocks.get(b["id"], {}).get("text", "")
        parts.append(
            "## FIX MODE\nThis block was already written but FAILED the checks. Rewrite it so that ALL problems below are solved, "
            "keep everything that is already fine, and still respect every requirement of the block brief. "
            "Follow the numbers in the problem list literally (if a keyword appears 3 times and must appear 1, remove exactly two). "
            "After the fix re-check every other hard constraint: shortening can remove a required keyword or entity. "
            "Do not mention the fixes in the text.\n\n"
            f"CURRENT TEXT:\n{cur}\n\nPROBLEMS TO FIX:\n" + "\n".join(f"- {f}" for f in fixes)
        )
    return "\n\n---\n\n".join(parts)


def build_section_message(group: list[dict], brief: dict, blocks: dict[str, dict], settings: Settings,
                          headings: dict[str, str] | None = None) -> str:
    """One call for an H2 together with its sub-sections: shared context, one BLOCK BRIEF per block, the answer split by markers."""
    ids = [b["id"] for b in group]
    parts = [_context(brief), f'## PAGE STRUCTURE FOR CONTEXT\n{_outline(brief["blocks"], headings)}']
    written = [
        f'{"#" * x["level"]} {_h(x, headings)}\n{blocks[x["id"]]["text"]}'
        for x in brief["blocks"] if x["id"] not in ids and x["id"] in blocks and blocks[x["id"]]["text"]
    ]
    if written:
        parts.append("## ALREADY WRITTEN BLOCKS (keep facts, numbers and tone consistent; do not repeat their content)\n\n" + "\n\n".join(written))
    if _taken_section(settings.shingle_n):
        parts.append(_taken_section(settings.shingle_n))
    parts.append(
        f"## SECTION\nWrite the blocks {', '.join(ids)} in ONE answer, in this order. They are one continuous section of the page: "
        "the sub-sections continue the parent, so the text must flow from block to block without repeating itself. "
        "Start the body of every block with a marker line `=== bNN ===` (the block id, exactly in this form, alone on its line) and write "
        "nothing outside the bodies. Every block keeps its own word range, keyword counts, format and facts."
    )
    parts += [_spec(b, brief, settings, headings, together=True) for b in group]
    return "\n\n---\n\n".join(parts)


def _generate(group: list[dict], brief: dict, blocks: dict[str, dict], settings: Settings, llm: LLM, system: str,
              headings: dict[str, str], fixes: dict[str, list[str]] | None = None) -> dict[str, str]:
    """Texts of one unit of generation. A single block (or a fix) is one call; a section of several blocks is one call too, and a block
    that the answer lost is written on its own."""
    if len(group) == 1:
        b = group[0]
        msg = build_user_message(b, brief, blocks, settings, fixes.get(b["id"]) if fixes else None, headings)
        raw = llm.text(system, msg, settings.model_generation, max_tokens=max(1024, block_cap(b, settings) * 6))
        return {b["id"]: clean_output(raw, headings[b["id"]])}
    msg = build_section_message(group, brief, blocks, settings, headings)
    raw = llm.text(system, msg, settings.model_generation, max_tokens=max(2048, sum(block_cap(b, settings) for b in group) * 6))
    parsed = parse_section(raw, [b["id"] for b in group])
    out = {i: clean_output(t, headings[i]) for i, t in parsed.items()}
    for b in group:
        if not out.get(b["id"]):
            known = {**blocks, **{i: {"text": t} for i, t in out.items()}}
            out.update(_generate([b], brief, known, settings, llm, system, headings))
    return out


def _snapshot(run: Run, state: dict, tag: str) -> None:
    run.save_json(f"02_history/{tag}.json", state)


def run_step2(run: Run, llm: LLM, settings: Settings, fixes: dict[str, list[str]] | None = None, iteration: int = 0) -> dict:
    brief = run.load_json(store.BRIEF)
    brief["facts"] = run.job().facts
    brief["brand"] = run.job().brand_name
    prepare_cards(run, brief, settings)
    system = load_writer_prompt(brief.get("page_type", "brand-review"))
    state = run.load_json(store.BLOCKS) if run.has(store.BLOCKS) else {"iteration": 0, "complete": False, "blocks": {}}
    blocks: dict[str, dict] = state["blocks"]
    by_id = {b["id"]: b for b in brief["blocks"]}

    # headings: the brief is English, the page headings are localized first (and repaired when step 3 reports problems)
    heading_fixes = {i: [f[len(HEADING_TAG):].strip() for f in fx if f.startswith(HEADING_TAG)] for i, fx in (fixes or {}).items()}
    heading_fixes = {i: fx for i, fx in heading_fixes.items() if fx}
    headings = H.localize(run, brief, llm, settings, only=list(heading_fixes) or None, problems=heading_fixes)
    if fixes:
        fixes = {i: [f for f in fx if not f.startswith(HEADING_TAG)] for i, fx in fixes.items()}
        fixes = {i: fx for i, fx in fixes.items() if fx}

    if fixes:
        todo = [b for b in brief["blocks"] if b["id"] in fixes]
    else:
        todo = [b for b in brief["blocks"] if b["id"] not in blocks]  # resume: skip what is already generated
    state["iteration"] = iteration

    if fixes:  # a fix rewrites one block at a time
        units = [[b] for b in todo]
    else:  # first pass: an H2 with its sub-sections is written in one call
        todo_ids = {b["id"] for b in todo}
        units = [g for g in ([b for b in grp if b["id"] in todo_ids] for grp in sections(brief["blocks"])) if g]

    for unit in units:
        texts = _generate(unit, brief, blocks, settings, llm, system, headings, fixes)
        for b in unit:
            prev = blocks.get(b["id"], {"version": 0, "history": []})
            blocks[b["id"]] = {
                "id": b["id"], "level": b["level"], "heading": headings[b["id"]], "text": texts[b["id"]],
                "version": prev["version"] + 1,
                "history": prev["history"] + ([{"iteration": iteration, "fixes": fixes[b["id"]]}] if fixes else []),
            }
            print(f"  {b['id']} {headings[b['id']][:50]!r}  v{blocks[b['id']]['version']}" + (" (section)" if len(unit) > 1 else ""))
        state["complete"] = all(i in blocks for i in by_id)
        run.save_json(store.BLOCKS, state)  # save after every unit so a crash loses nothing

    state["complete"] = all(i in blocks for i in by_id)
    run.save_json(store.BLOCKS, state)
    _snapshot(run, state, f"iter_{iteration:02d}")
    run.save_text(store.TEXT_DRAFT, assemble(brief["blocks"], blocks, headings))
    run.mark("step2", "done", iteration=iteration, regenerated=len(todo))
    return state

