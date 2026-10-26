from __future__ import annotations

from .config import PROMPTS_DIR, STUB_MARKER

REVIEW = "brand-review"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text(encoding="utf-8").strip()


def load_step1_prompt(kind: str, page_type: str = REVIEW) -> str:
    """Prompt of the ТЗ model: `kind` = "brief" or "review". The brand-review prompts are `step1_brief.md` / `step1_review.md`,
    the other page types have a prompt of their own (`step1_brief_top-list.md`, ...)."""
    return load_prompt(f"step1_{kind}" if page_type == REVIEW else f"step1_{kind}_{page_type}")


def load_writer_prompt(page_type: str = REVIEW) -> str:
    """The user's own system prompt for text generation (step 2). Refuses to run with the stub.
    Page types other than brand-review add their page-type rules (`writer_<page type>.md`) at the end."""
    text = load_prompt("system_prompt")
    if STUB_MARKER in text:
        raise RuntimeError(
            "prompts/system_prompt.md still contains the stub. Paste your real system prompt there "
            f"(and delete the line with {STUB_MARKER})."
        )
    return text if page_type == REVIEW else text + "\n\n" + load_prompt(f"writer_{page_type}")


def load_consistency_prompt(page_type: str = REVIEW) -> str:
    """Prompt of the step 3 consistency check; the other page types add their rules (`step3_consistency_<page type>.md`)."""
    text = load_prompt("step3_consistency")
    return text if page_type == REVIEW else text + "\n\n" + load_prompt(f"step3_consistency_{page_type}")
