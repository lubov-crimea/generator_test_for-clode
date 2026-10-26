"""Settings: paths, models, tolerances. Values come from env / .env."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
RUNS_DIR = ROOT / "runs"
OUTPUT_DIR = ROOT / "output"

STUB_MARKER = "TEXTGEN_STUB_PROMPT"


def load_dotenv(path: Path | None = None) -> None:
    path = path or ROOT / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


@dataclass
class Settings:
    model_analysis: str
    model_generation: str
    model_check: str
    words_tolerance: float  # allowed deviation of block length from the ТЗ, e.g. 0.15 = ±15%
    total_words_tolerance: float
    min_words_slack: int  # absolute slack so tiny blocks are not too strict
    max_fix_iterations: int
    mandatory_ratio: float  # heading cluster is mandatory if it appears in >= this share of competitors
    max_keyword_density: float  # max keyword occurrences per word for the whole text (0.04 = 4%)
    words_overflow: float = 0.10  # while writing, a block may exceed its words_max by this share (the cap of the block)
    range_width: float = 0.12  # the words range of a block is the computed middle +-this share
    max_growth: float = 0.20  # the ТЗ may enlarge a block over its competitor-based range by this share (both bounds); with the overflow ~+30%
    page_limit: float = 0.20  # the whole text stays within the mean of its size group plus this share (`max_body_words` of the ТЗ)
    page_limit_large: float = 0.0  # the large group (the longest competitors) gets no extra: its limit is the group mean
    large_per_texts: int = 10  # a single outlier competitor (the large group) is imitated by one text per this many texts
    words_per_connection: int = 15  # words that one entity connection (a chain subject -> relation -> object) of a block gets
    fact_text_factor: float = 1.2  # words of text per word of a knowledge-base value that a paragraph needs to state it (1.0 in a list or a table)
    fact_min_words: int = 3  # a short scalar fact (a figure, a name) still needs this many words
    fact_max_words: int = 30  # one knowledge-base item never gets more (a long value is shortened or shown in a list or a table: 40)
    brand_free_words: int = 50  # where the ТЗ allows the brand name 0 times it may still appear once per this many words
    shingle_n: int = 9  # technical duplicate = this many words in a row shared with a sibling text (shingles.py)
    paraphrase_slots: int = 12  # paraphrases of every sentence of the knowledge base in the bank: one per variant (paraphrase.py)
    require_bank: bool = False  # True: a sentence of the knowledge base without a bank entry stops step 2 (no verbatim sentence reaches the writer)

    @classmethod
    def load(cls) -> "Settings":
        load_dotenv()
        default = "claude-sonnet-5-5"
        return cls(
            model_analysis=os.getenv("TEXTGEN_MODEL_ANALYSIS", default),
            model_generation=os.getenv("TEXTGEN_MODEL_GENERATION", default),
            model_check=os.getenv("TEXTGEN_MODEL_CHECK", default),
            words_tolerance=float(os.getenv("TEXTGEN_WORDS_TOLERANCE", "0.15")),
            total_words_tolerance=float(os.getenv("TEXTGEN_TOTAL_WORDS_TOLERANCE", "0.10")),
            min_words_slack=int(os.getenv("TEXTGEN_MIN_WORDS_SLACK", "12")),
            max_fix_iterations=int(os.getenv("TEXTGEN_MAX_FIX_ITERATIONS", "4")),
            mandatory_ratio=float(os.getenv("TEXTGEN_MANDATORY_RATIO", "0.5")),
            max_keyword_density=float(os.getenv("TEXTGEN_MAX_KEYWORD_DENSITY", "0.04")),
            words_overflow=float(os.getenv("TEXTGEN_WORDS_OVERFLOW", "0.10")),
            range_width=float(os.getenv("TEXTGEN_RANGE_WIDTH", "0.12")),
            max_growth=float(os.getenv("TEXTGEN_MAX_GROWTH", "0.20")),
            page_limit=float(os.getenv("TEXTGEN_PAGE_LIMIT", "0.20")),
            page_limit_large=float(os.getenv("TEXTGEN_PAGE_LIMIT_LARGE", "0.0")),
            large_per_texts=int(os.getenv("TEXTGEN_LARGE_PER_TEXTS", "10")),
            words_per_connection=int(os.getenv("TEXTGEN_WORDS_PER_CONNECTION", "15")),
            fact_text_factor=float(os.getenv("TEXTGEN_FACT_TEXT_FACTOR", "1.2")),
            fact_min_words=int(os.getenv("TEXTGEN_FACT_MIN_WORDS", "3")),
            fact_max_words=int(os.getenv("TEXTGEN_FACT_MAX_WORDS", "30")),
            brand_free_words=int(os.getenv("TEXTGEN_BRAND_FREE_WORDS", "50")),
            shingle_n=int(os.getenv("TEXTGEN_SHINGLE_N", "9")),
            paraphrase_slots=int(os.getenv("TEXTGEN_PARAPHRASE_SLOTS", "12")),
            require_bank=os.getenv("TEXTGEN_REQUIRE_BANK", "0") == "1",
        )
