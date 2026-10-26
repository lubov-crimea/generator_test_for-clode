"""Size groups of the competitors (textgen/tiers.py) and what they do to the targets and the variants."""
import pytest

from textgen.brief import compute_targets, normalize, validate
from textgen.config import Settings
from textgen.tiers import allocate, build_tiers, describe, split_groups


@pytest.fixture
def settings():
    return Settings.load()


def test_natural_breaks_cut_at_the_two_largest_gaps():
    assert split_groups([1116, 1473, 1836, 1957, 3355]) == [[1116, 1473], [1836, 1957], [3355]]  # the example of the operator
    assert split_groups([238, 385, 524, 844, 1754]) == [[238, 385, 524], [844], [1754]]  # Login
    assert split_groups([1, 2]) == [[1], [2]] and split_groups([5]) == [[5]] and split_groups([7, 7, 7]) == [[7], [7], [7]]


def test_tiers_mean_limit_and_multiplier(settings):
    t = build_tiers([1754, 238, 385, 844, 524], settings)["tiers"]
    assert (t["small"]["mean"], t["small"]["limit"]) == (382, 459)  # the limit uses the exact mean: 382.33 x 1.2
    assert (t["medium"]["target"], t["medium"]["limit"]) == (844, 1013)
    assert (t["large"]["target"], t["large"]["limit"]) == (1754, 1754)  # no extra for the large group
    assert t["large"]["outlier"] and not t["medium"].get("outlier")


def test_few_competitors_give_fewer_groups(settings):
    one = build_tiers([900], settings)
    assert list(one["tiers"]) == ["medium"] and one["tiers"]["medium"]["limit"] == 1080
    two = build_tiers([1000, 3000], settings)["tiers"]
    assert two["small"]["target"] == 1000 and two["large"]["target"] == 3000 and two["large"]["limit"] == 3000
    assert two["medium"]["target"] == 2000 and two["medium"]["synthetic"]  # the middle of the two
    given = build_tiers([1000, 3000], settings, words_override=500)
    assert list(given["tiers"]) == ["medium"] and given["tiers"]["medium"]["target"] == 500 and given["tiers"]["medium"]["limit"] == 600
    assert build_tiers([0, 800, 0], settings)["tiers"]["medium"]["target"] == 800  # an empty page is no competitor


def test_allocation_of_the_texts(settings):
    login = build_tiers([238, 385, 524, 844, 1754], settings)
    assert allocate(8, login, settings) == {"small": 3, "medium": 4, "large": 1}  # the Login split
    assert allocate(10, login, settings) == {"small": 4, "medium": 5, "large": 1}
    assert allocate(11, login, settings)["large"] == 2  # one outlier text per 10 texts
    assert allocate(1, login, settings) == {"small": 0, "medium": 1, "large": 0}
    assert allocate(2, login, settings) == {"small": 0, "medium": 1, "large": 1}  # fewer texts: one large text, the optimum first
    assert allocate(3, login, settings) == {"small": 1, "medium": 1, "large": 1}
    wide = build_tiers([100, 110, 500, 520, 530, 900, 950], settings)  # a large group of two competitors is shared by competitors
    assert wide["tiers"]["large"]["competitors"] == [900, 950] and not wide["tiers"]["large"]["outlier"]
    assert allocate(7, wide, settings)["large"] == 2  # 7 texts x 2 of 7 competitors
    assert allocate(5, build_tiers([800], settings), settings) == {"medium": 5}


def test_describe_lists_the_groups(settings):
    text = describe(build_tiers([238, 385, 524, 844, 1754], settings))
    assert "small  238/385/524 -> mean 382, limit 459" in text and "large  1754 -> mean 1754, limit 1754 (x1.0) (single outlier)" in text


def test_compute_targets_follow_the_group(settings):
    stats = {"aggregate": {"median_total": {"k": 2}}, "competitors": [{"body_words": w} for w in (238, 385, 524, 844, 1754)]}
    medium = compute_targets(stats, ["k"], settings)
    assert (medium["tier"], medium["target_body_words"], medium["max_body_words"]) == ("medium", 844, 1013)
    small = compute_targets(stats, ["k"], settings, tier="small")
    assert (small["target_body_words"], small["max_body_words"]) == (382, 459)
    large = compute_targets(stats, ["k"], settings, tier="large")
    assert (large["target_body_words"], large["max_body_words"]) == (1754, 1754)
    assert compute_targets(stats, ["k"], settings, words_override=700)["max_body_words"] == 840


def test_variants_take_the_limit_and_the_defaults_of_their_group(settings, monkeypatch):
    from textgen import variants as V

    monkeypatch.setattr(V, "INTRINSIC", {})
    tiers = build_tiers([238, 385, 524, 844, 1754], settings)
    ents = [{"name": f"E{i}", "priority": 10 - i} for i in range(6)]
    conns = [{"subject": f"S{i}", "relation": "r", "object": "o", "priority": 9 - i} for i in range(3)]
    base = {"page_type": "brand-subpage", "skipped_clusters": [], "targets": {"tier": "medium", "tiers": tiers},
            "blocks": [{**_mk(1, "Login", 60), "id": "b01", "entities": ents, "entity_connections": conns, "covers_clusters": [], "kb_refs": [], "listed_entities": []},
                       {**_mk(2, "Steps", 60), "id": "b02", "covers_clusters": [], "kb_refs": [], "listed_entities": []}]}

    def spec(tier, words):
        return {"id": "v1", "name": "n", "tier": tier, "intent_summary": "x", "blocks": [
            {"from": ["b01"], "level": 1, "heading": "Login", "words": words, "kw": {"a": 1}},
            {"from": ["b02"], "level": 2, "heading": "Steps", "words": words}]}

    cl = []
    brief, targets, errs = V.build_variant(base, spec("small", 200), None, ["a"], settings, cl)
    assert errs == [] and (targets["tier"], targets["max_body_words"], targets["competitor_body_words"]) == ("small", 459, 382)
    assert len(brief["blocks"][0]["entities"]) == 3 and len(brief["blocks"][0]["entity_connections"]) == 1  # the small text cuts them to the minimum
    brief, targets, errs = V.build_variant(base, spec("large", 200), None, ["a"], settings, cl)
    assert targets["max_body_words"] == 1754 and len(brief["blocks"][0]["entities"]) == 6 and len(brief["blocks"][0]["entity_connections"]) == 3
    _, _, errs = V.build_variant(base, spec("small", 260), None, ["a"], settings, cl)  # 2 x 260 x 1.12 = 582 words of maxima > 459
    assert any("limit is 459" in e and 'size group "small"' in e for e in errs)
    _, _, errs = V.build_variant(base, spec("medium", 260), None, ["a"], settings, cl)
    assert not any("limit is" in e for e in errs)  # the same text fits the medium group (1013)
    with pytest.raises(ValueError, match='no size group "huge"'):
        V.build_variant(base, spec("huge", 100), None, ["a"], settings, cl)


def _mk(level, heading, mid):
    return {"id": "x", "level": level, "heading": heading, "source": "mandatory", "words_min": round(mid * 0.88), "words_max": round(mid * 1.12),
            "keywords": {}, "summary": "s", "copywriter_notes": "n", "formats": ["paragraph"],
            "entities": [{"name": "Online Casino", "priority": 10}],
            "entity_connections": [{"subject": "Licence", "relation": "regulates", "object": "Online Casino", "priority": 8}]}


def test_the_large_text_may_be_shorter_than_its_target_but_not_longer(settings):
    brief = {"blocks": [_mk(1, "T", 100), _mk(2, "Part", 100)]}
    normalize(brief, ["a"])
    base = {"target_body_words": 1000, "competitor_body_words": 1000, "max_body_words": 1000, "keyword_targets": {"a": 0}}
    assert any("sum of block words is 200" in e for e in validate(brief, {**base, "tier": "medium"}, ["a"], settings))  # too short for a medium text
    assert not any("sum of block words" in e for e in validate(brief, {**base, "tier": "large"}, ["a"], settings))  # fine for the large one
    big = {"blocks": [_mk(1, "T", 600), _mk(2, "Part", 600)]}
    normalize(big, ["a"])
    assert any("sum of block words is 1200" in e for e in validate(big, {**base, "tier": "large"}, ["a"], settings))  # but never over the target
