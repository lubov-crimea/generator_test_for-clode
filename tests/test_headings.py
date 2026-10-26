"""Brief language (always English) and localization of the page headings."""
import pytest

from textgen import headings as H
from textgen import store
from textgen.brief import normalize, validate
from textgen.config import Settings
from textgen.inputs import Job
from textgen.store import Run
from tests.test_units import mk

KW = ["Incaspin", "Incaspin casino"]


@pytest.fixture
def settings():
    return Settings.load()


def test_heading_keywords_default_to_the_english_heading_and_can_be_declared():
    brief = {"blocks": [mk(1, "Incaspin Casino review", 90, 110, source="h1"), mk(2, "Bonuses", 90, 110, heading_keywords={"Incaspin": 1})]}
    normalize(brief, KW)
    assert brief["blocks"][0]["heading_keywords"] == {"Incaspin": 0, "Incaspin casino": 1}
    assert brief["blocks"][1]["heading_keywords"] == {"Incaspin": 1, "Incaspin casino": 0}


def test_brief_must_be_english(settings):
    targets = {"target_body_words": 200, "keyword_targets": {"Incaspin": 0, "Incaspin casino": 1}}
    ok = {"intent_summary": "A review page for German players.", "blocks": [
        mk(1, "Incaspin Casino review", 90, 110, source="h1", summary="Short introduction to the casino and the page.",
           copywriter_notes="Open with one clear sentence about the casino and name the licence exactly as given.")]}
    normalize(ok, KW)
    assert not [e for e in validate(ok, {**targets, "keyword_targets": {"Incaspin": 0, "Incaspin casino": 1}}, KW, settings) if "English" in e]

    bad = {"intent_summary": "Markenbezogene Seite über das Online-Casino für Spieler aus Deutschland und Österreich.", "blocks": [
        mk(1, "Willkommensbonus im Incaspin Casino", 90, 110, source="h1",
           summary="Kurze Einleitung: was das Online-Casino ist und welche Bereiche es gibt, für Spieler aus Deutschland.",
           copywriter_notes="Beginne mit einem klaren Satz zur zentralen Entität und nenne die Bereiche laut der Information über die Marke.")]}
    normalize(bad, KW)
    errs = validate(bad, targets, KW, settings)
    assert any("intent_summary must be in English" in e for e in errs)
    # a short German heading WITHOUT diacritics cannot be detected reliably (see test below for the diacritics rule); the LLM review covers it
    assert any("summary must be in English" in e for e in errs)
    assert any("copywriter_notes must be in English" in e for e in errs)


def test_heading_with_diacritics_is_rejected(settings):
    brief = {"blocks": [mk(1, "Bonusbedingungen auf einen Blick: Gültigkeit", 90, 110, source="h1")]}
    normalize(brief, KW)
    assert any("must be in English" in e for e in validate(brief, {"target_body_words": 100, "keyword_targets": {"Incaspin": 0, "Incaspin casino": 0}}, KW, settings))


def test_check_heading_counts_and_language():
    b = normalize({"blocks": [mk(2, "Welcome bonus at Incaspin Casino", 90, 110)]}, KW)["blocks"][0]
    assert H.check_heading("Willkommensbonus im Incaspin Casino", b, KW, "de") == []
    assert any("must appear exactly 1" in p for p in H.check_heading("Willkommensbonus im Casino", b, KW, "de"))
    assert any('"Incaspin" appears 1' in p and "exactly 0" in p for p in H.check_heading("Incaspin Casino und Incaspin", b, KW, "de"))
    assert H.check_heading("Приветственный бонус в Incaspin Casino", b, KW, "de")  # foreign script
    assert H.check_heading("Anything goes here", b, ["x"], "en") == []


class FakeLocalizer:
    """Returns a wrong heading first (keyword missing), then the repaired one."""

    def __init__(self):
        self.calls = []

    def json(self, system, user, schema, model, name="result", max_tokens=0):
        import json as _j

        assert name == "headings"
        items = _j.loads(user[user.index("["):])
        self.calls.append([i["id"] for i in items])
        out = []
        for i in items:
            need = i["keywords_the_heading_must_contain"]
            if len(self.calls) == 1 and need:
                out.append({"id": i["id"], "heading": "Willkommensbonus"})  # keyword missing
            else:
                out.append({"id": i["id"], "heading": "Willkommensbonus im Incaspin Casino" if need else "Bonusbedingungen"})
        return {"headings": out}


def _run(tmp_path, monkeypatch, language):
    monkeypatch.setattr(store, "RUNS_DIR", tmp_path / "runs")
    return Run.create("t", Job(geo="DE", keywords=KW, competitors=["https://x.de"], language=language))


def test_localize_retries_until_keywords_are_right(tmp_path, monkeypatch, settings):
    run = _run(tmp_path, monkeypatch, "de")
    brief = normalize({"language": "de", "geo": "DE", "keywords": KW, "blocks": [
        mk(1, "Welcome bonus at Incaspin Casino", 90, 110, source="h1"), mk(2, "Bonus terms", 90, 110)]}, KW)
    llm = FakeLocalizer()
    heads = H.localize(run, brief, llm, settings)
    assert heads == {"b01": "Willkommensbonus im Incaspin Casino", "b02": "Bonusbedingungen"}
    assert len(llm.calls) == 2 and llm.calls[1] == ["b01"]  # only the failed heading is asked again
    saved = run.load_json(H.FILE)["headings"]
    assert saved["b01"] == {"en": "Welcome bonus at Incaspin Casino", "local": "Willkommensbonus im Incaspin Casino"}
    assert H.load(run, brief) == heads


def test_english_pages_need_no_localization(tmp_path, monkeypatch, settings):
    run = _run(tmp_path, monkeypatch, "en")
    brief = normalize({"language": "en", "geo": "AU", "keywords": KW, "blocks": [mk(1, "Incaspin Casino review", 90, 110, source="h1")]}, KW)
    assert H.localize(run, brief, None, settings) == {"b01": "Incaspin Casino review"}


def test_load_requires_localization_for_other_languages(tmp_path, monkeypatch):
    run = _run(tmp_path, monkeypatch, "de")
    brief = normalize({"language": "de", "geo": "DE", "keywords": KW, "blocks": [mk(1, "Incaspin Casino review", 90, 110, source="h1")]}, KW)
    with pytest.raises(RuntimeError, match="localized first"):
        H.load(run, brief)


def test_assemble_uses_localized_headings():
    from textgen.step2 import assemble

    blocks = normalize({"blocks": [mk(1, "Title", 90, 110, source="h1"), mk(2, "Bonuses", 90, 110)]}, KW)["blocks"]
    text = assemble(blocks, {"b01": {"text": "A"}, "b02": {"text": "B"}}, {"b01": "Titel", "b02": "Boni"})
    assert text.startswith("# Titel\n\nA\n\n## Boni\n\nB")
    assert assemble(blocks, {"b01": {"text": "A"}, "b02": {"text": "B"}}).startswith("# Title")
