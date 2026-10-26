"""GEO -> language and language checks for generated text."""
from __future__ import annotations

import re

from langdetect import DetectorFactory, detect_langs
from langdetect.lang_detect_exception import LangDetectException

from .textutil import count_words, remove_keywords, text_segments

DetectorFactory.seed = 0

GEO_LANG = {
    "australia": "en", "new zealand": "en", "united kingdom": "en", "uk": "en", "ireland": "en", "canada": "en",
    "united states": "en", "usa": "en", "us": "en", "south africa": "en", "india": "en", "nigeria": "en",
    "kenya": "en", "ghana": "en", "philippines": "en", "singapore": "en", "malaysia": "en",
    "germany": "de", "austria": "de", "switzerland": "de",
    "france": "fr", "belgium": "fr", "spain": "es", "mexico": "es", "argentina": "es", "chile": "es",
    "colombia": "es", "peru": "es", "portugal": "pt", "brazil": "pt", "italy": "it", "netherlands": "nl",
    "poland": "pl", "czech republic": "cs", "czechia": "cs", "slovakia": "sk", "hungary": "hu",
    "romania": "ro", "bulgaria": "bg", "greece": "el", "turkey": "tr", "sweden": "sv", "norway": "no",
    "denmark": "da", "finland": "fi", "japan": "ja", "south korea": "ko", "korea": "ko", "china": "zh-cn",
    "vietnam": "vi", "thailand": "th", "indonesia": "id", "ukraine": "uk", "russia": "ru", "kazakhstan": "ru",
    "egypt": "ar", "saudi arabia": "ar", "uae": "ar", "croatia": "hr", "serbia": "sr", "slovenia": "sl",
    # Russian names
    "австралия": "en", "новая зеландия": "en", "великобритания": "en", "канада": "en", "сша": "en",
    "индия": "en", "германия": "de", "франция": "fr", "испания": "es", "португалия": "pt", "бразилия": "pt",
    "италия": "it", "польша": "pl", "турция": "tr", "япония": "ja", "россия": "ru", "украина": "uk",
}

LANG_NAMES = {
    "en": "English", "de": "German", "fr": "French", "es": "Spanish", "pt": "Portuguese", "it": "Italian",
    "nl": "Dutch", "pl": "Polish", "cs": "Czech", "sk": "Slovak", "hu": "Hungarian", "ro": "Romanian",
    "bg": "Bulgarian", "el": "Greek", "tr": "Turkish", "sv": "Swedish", "no": "Norwegian", "da": "Danish",
    "fi": "Finnish", "ja": "Japanese", "ko": "Korean", "zh-cn": "Chinese", "vi": "Vietnamese", "th": "Thai",
    "id": "Indonesian", "ms": "Malay", "uk": "Ukrainian", "ru": "Russian", "ar": "Arabic", "hr": "Croatian", "sr": "Serbian",
    "sl": "Slovenian", "hi": "Hindi",
}

SCRIPTS = {
    "cyrillic": r"[Ѐ-ӿ]",
    "cjk": r"[一-鿿぀-ヿ]",
    "hangul": r"[가-힯ᄀ-ᇿ]",
    "arabic": r"[؀-ۿ]",
    "hebrew": r"[֐-׿]",
    "thai": r"[฀-๿]",
    "devanagari": r"[ऀ-ॿ]",
    "greek": r"[Ͱ-Ͽ]",
}
ALLOWED_SCRIPTS = {
    "ru": {"cyrillic"}, "uk": {"cyrillic"}, "bg": {"cyrillic"}, "sr": {"cyrillic"},
    "ja": {"cjk"}, "zh-cn": {"cjk"}, "ko": {"hangul", "cjk"}, "ar": {"arabic"}, "he": {"hebrew"},
    "th": {"thai"}, "hi": {"devanagari"}, "el": {"greek"},
}


def language_from_geo(geo: str) -> str | None:
    return GEO_LANG.get(geo.strip().lower())


def language_name(code: str) -> str:
    return LANG_NAMES.get(code, code)


def _same_lang(detected: str, target: str) -> bool:
    family = {"id", "ms"}  # langdetect has no Malay profile and reads Malay as Indonesian
    return detected == target or detected.split("-")[0] == target.split("-")[0] or ({detected, target} <= family)


def check_language(text: str, target: str, keywords: list[str]) -> list[dict]:
    """Return a list of {segment, detected, reason} for fragments not in the target language."""
    problems: list[dict] = []
    allowed = ALLOWED_SCRIPTS.get(target, set())
    for seg in text_segments(text):
        clean = remove_keywords(seg, keywords)
        if re.fullmatch(r"[A-Z0-9][A-Z0-9 ,/()+.&'-]*", clean.strip()):
            continue  # a row of codes (EUR, USD, USDT ...) has no language
        foreign = [name for name, rx in SCRIPTS.items() if name not in allowed and re.search(rx, clean)]
        if foreign:
            problems.append({"segment": seg[:160], "detected": "/".join(foreign), "reason": "foreign script"})
            continue
        if count_words(clean) < 6:
            continue  # too short for reliable detection
        try:
            top = detect_langs(clean)[0]
        except LangDetectException:
            continue
        if not _same_lang(top.lang, target) and top.prob >= 0.85:
            problems.append({"segment": seg[:160], "detected": top.lang, "reason": f"detected {top.lang} ({top.prob:.2f})"})
    return problems
