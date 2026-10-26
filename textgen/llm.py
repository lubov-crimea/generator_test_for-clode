"""Thin wrapper around the Anthropic API. Structured output goes through a forced tool call."""
from __future__ import annotations

import os
from typing import Any, Protocol


class LLM(Protocol):
    def text(self, system: str, user: str, model: str, max_tokens: int = 4096) -> str: ...

    def json(self, system: str, user: str, schema: dict, model: str, name: str = "result", max_tokens: int = 16000) -> Any: ...


class NeedsAnswer(RuntimeError):
    """Raised by ManualLLM when an answer file is missing."""


class ManualLLM:
    """No API: every request is written to <run>/llm/<name>.request.md and the answer is read from <run>/llm/<name>.json
    (or .txt for plain text). Lets an operator (or Claude Code itself) play the model while the pipeline stays unchanged."""

    def __init__(self, llm_dir) -> None:
        from pathlib import Path

        self.dir = Path(llm_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.n = 0
        self.seen: dict[str, int] = {}

    def _ask(self, name: str, system: str, user: str, ext: str):
        self.n += 1
        self.seen[name] = self.seen.get(name, 0) + 1
        if self.seen[name] > 1:  # repeated call of the same kind: brief.json, brief_2.json, ...
            name = f"{name}_{self.seen[name]}"
        ans = self.dir / f"{name}.{ext}"
        if ans.exists():
            return ans.read_text(encoding="utf-8-sig")
        (self.dir / f"{name}.request.md").write_text(f"# SYSTEM\n\n{system}\n\n# USER\n\n{user}\n", encoding="utf-8")
        raise NeedsAnswer(f"Answer needed: {ans} (request: {self.dir / (name + '.request.md')})")

    def text(self, system: str, user: str, model: str, max_tokens: int = 4096) -> str:
        return self._ask(f"text_{self.n + 1:03d}", system, user, "txt").strip()

    def json(self, system: str, user: str, schema: dict, model: str, name: str = "result", max_tokens: int = 16000) -> Any:
        import json

        return json.loads(self._ask(name, system, user, "json"))


class AnthropicLLM:
    def __init__(self) -> None:
        import anthropic

        if not os.getenv("ANTHROPIC_API_KEY"):
            raise RuntimeError("ANTHROPIC_API_KEY is not set. Put it into .env (see .env.example).")
        self.client = anthropic.Anthropic(max_retries=4)

    def text(self, system: str, user: str, model: str, max_tokens: int = 4096) -> str:
        resp = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(b.text for b in resp.content if b.type == "text").strip()

    def json(self, system: str, user: str, schema: dict, model: str, name: str = "result", max_tokens: int = 16000) -> Any:
        resp = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            tools=[{"name": name, "description": "Return the result in this exact structure.", "input_schema": schema}],
            tool_choice={"type": "tool", "name": name},
        )
        for block in resp.content:
            if block.type == "tool_use":
                return block.input
        raise RuntimeError(f"Model returned no tool call (stop_reason={resp.stop_reason})")

