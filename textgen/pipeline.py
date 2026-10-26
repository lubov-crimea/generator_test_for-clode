"""Whole pipeline: step 1 -> step 2 -> (step 3 -> step 2 with fixes)* -> step 4."""
from __future__ import annotations

from pathlib import Path

from . import store
from .config import Settings
from .llm import LLM
from .step1 import run_step1
from .step2 import run_step2
from .step3 import run_step3
from .step4 import run_step4
from .store import Run


def check_and_fix_loop(run: Run, llm: LLM, settings: Settings) -> bool:
    """Step 3 -> one merged fix set -> step 2 regenerates only the affected blocks -> step 3 again."""
    for it in range(settings.max_fix_iterations + 1):
        passed, fixes = run_step3(run, llm, settings, iteration=it)
        if passed:
            return True
        if it == settings.max_fix_iterations:
            break
        print(f"  -> step 2: regenerating {', '.join(fixes)}")
        run_step2(run, llm, settings, fixes=fixes, iteration=it + 1)
    return False


def run_all(run: Run, llm: LLM, settings: Settings, html_dir: Path | None = None, words: int | None = None,
            force: bool = False, force_final: bool = False) -> bool:
    print("STEP 1: competitor analysis + ТЗ")
    if force or not run.has(store.BRIEF):
        run_step1(run, llm, settings, html_dir=html_dir, words=words, force=force)
    else:
        print("  (already done, reusing 01_brief.json; use --force to redo)")

    print("STEP 2: text generation")
    run_step2(run, llm, settings)

    print("STEP 3: checks (+ fix loop through step 2)")
    ok = check_and_fix_loop(run, llm, settings)
    if not ok:
        print(f"  !! not passed after {settings.max_fix_iterations} fix iterations; see 03_check_iter_*.json")
        if not force_final:
            return False

    print("STEP 4: save txt")
    run_step4(run, force=force_final)
    return ok
