"""`python -m textgen bank list|merge|status <run>`: the paraphrase bank of the knowledge base of a run (paraphrase.py).

list   writes request files data/paraphrase_banks/<kb>.requests/chunk_NN.json (sentences without a complete entry) for the writers
       (one chunk = one agent); the answer of a chunk is chunk_NN.answer.json: {"<key>": ["<wording 1>", ... "<wording 12>"]}
merge  validates every answer file, stores the valid entries in the bank and writes retry_NN.json for the keys that failed (with the errors)
status counts complete entries
"""
from __future__ import annotations

import json
from pathlib import Path

from .config import Settings
from .paraphrase import BANK_DIR, load_bank, must_keep, save_bank, sentences_of, validate_item
from .protected import Mask, protected_phrases
from .store import Run

RULES = (
    "For EVERY sentence write {slots} alternative wordings (English). Each wording states exactly the same fact: keep every figure, amount, "
    "period, percentage and every name listed in keep_figures / keep_names exactly as written. Do not add a figure, a condition or a claim; do not "
    "drop one. The wordings must differ in construction (subject, order of the clauses, voice, sentence type), not by swapping single words: "
    "no run of {n} words in a row may be shared with the original or with another wording of the same sentence. About the same length as the "
    "original (0.6x to 1.6x). Neutral editorial third person, no em dashes, no semicolons, no second person."
)


def _setup(run: Run, settings: Settings):
    kb = run.knowledge_base()
    if not kb:
        raise RuntimeError("the run has no knowledge base")
    mask = Mask.for_kb(kb, run.job().brand_name)
    return kb, mask, load_bank(kb["title"])


def _complete(bank: dict, key: str, slots: int) -> bool:
    return len(bank["items"].get(key, {}).get("paraphrases", [])) == slots


def run_bank(action: str, run: Run, settings: Settings, chunk: int = 25, file: str | None = None) -> None:
    kb, mask, bank = _setup(run, settings)
    slots, n = settings.paraphrase_slots, settings.shingle_n
    sents = sentences_of(kb)
    todo = [k for k in sents if not _complete(bank, k, slots)]
    req_dir = BANK_DIR / f"{kb['title']}.requests"
    if action == "check":  # validate one answer file (no merge): the writer of a chunk runs this until it prints OK
        answers = json.loads(Path(file).read_text(encoding="utf-8-sig"))
        bad = 0
        for key, paras in answers.items():
            if key not in sents:
                print(f"unknown key {key}")
                bad += 1
                continue
            errs = validate_item(sents[key], paras, mask, slots, n)
            if errs:
                bad += 1
                print(f"{key} {sents[key][:60]!r}:")
                for e in errs[:6]:
                    print(f"    {e}")
        missing = [k for k in json.loads(Path(file).with_name(Path(file).name.replace(".answer", "")).read_text(encoding="utf-8"))["items"] if k["key"] not in answers] if Path(file).name.endswith(".answer.json") else []
        for k in missing:
            print(f"missing key {k['key']}")
        print("OK: every sentence has valid wordings" if not bad and not missing else f"{bad} sentence(s) with problems, {len(missing)} missing")
        return
    if action == "status":
        print(f"{kb['title']}: {len(sents)} sentences, {len(sents) - len(todo)} complete, {len(todo)} missing; bank {BANK_DIR / (kb['title'] + '.json')}")
        return
    if action == "list":
        req_dir.mkdir(parents=True, exist_ok=True)
        for i in range(0, len(todo), chunk):
            items = []
            for k in todo[i:i + chunk]:
                figs, names = must_keep(sents[k], mask)
                items.append({"key": k, "text": sents[k], "keep_figures": figs, "keep_names": names})
            p = req_dir / f"chunk_{i // chunk + 1:02d}.json"
            p.write_text(json.dumps({"rules": RULES.format(slots=slots, n=n), "slots": slots, "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"request: {p}  ->  answer: {p.with_suffix('.answer.json')}")
        print(f"{len(todo)} sentences in {(len(todo) + chunk - 1) // chunk} request file(s)")
        return
    # merge
    bad_total = 0
    retry: dict[str, dict] = {}
    for f in sorted(req_dir.glob("*.answer.json")) if req_dir.exists() else []:
        answers = json.loads(f.read_text(encoding="utf-8-sig"))
        for key, paras in answers.items():
            if key not in sents:
                print(f"{f.name}: unknown key {key}")
                continue
            errs = validate_item(sents[key], paras, mask, slots, n)
            if errs:
                bad_total += 1
                retry[key] = {"key": key, "text": sents[key], "errors": errs[:6], "keep_figures": must_keep(sents[key], mask)[0], "keep_names": must_keep(sents[key], mask)[1]}
            else:
                bank["items"][key] = {"text": sents[key], "paraphrases": paras}
    bank["slots"] = slots
    save_bank(bank)
    left = [k for k in sents if not _complete(bank, k, slots)]
    print(f"merged; bank has {len(sents) - len(left)} of {len(sents)} sentences complete; {bad_total} answer(s) failed validation")
    if retry:
        p = req_dir / "retry.json"
        p.write_text(json.dumps({"rules": RULES.format(slots=slots, n=n), "slots": slots, "items": list(retry.values())}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"retry request with the errors: {p}  ->  answer: {p.with_suffix('.answer.json')}")
        for v in list(retry.values())[:8]:
            print("  ", v["key"], v["errors"][:2])
