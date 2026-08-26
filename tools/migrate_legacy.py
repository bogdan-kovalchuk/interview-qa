"""M4 migration: convert the 392 predecessor cards into `content/` questions.

Reads the frozen input under `meta/migration/legacy/` (via `migration.legacy_reader`),
applies the hand-made classification tables in `migration.overrides`, and writes
one Ukrainian + one English Markdown file per question, plus the id-registry
and vocabulary.yml updates. Nothing here reads or writes anything outside
`content/`, `meta/id-registry.csv` and `meta/vocabulary.yml`.

Run from the repository root:

    python tools/migrate_legacy.py [--dry-run]

Idempotent: re-running after the files already exist re-derives the same
content deterministically (same IDs, same slugs) and will simply overwrite -
it does not append to the registry a second time for an id already present.

This script is kept as the record of how the migration was done
(AGENTS.md/PLAN.md step 4); it is not part of the regular `iqa` pipeline and
is not expected to run again after the migration is merged.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import sys
from datetime import date
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from migration import legacy_reader
from migration.htmlconv import back_to_short_answer_md, html_fragment_to_plain
from migration.overrides import (
    TOPIC_FILE_SECTION,
    SECTION_OVERRIDE,
    EXISTING_PREFIXES,
    NEW_PREFIXES,
    NEW_SECTION_LABELS,
    TYPE_OVERRIDE,
    CODING_EXPORT_FALSE,
    UK_SHORT_ANSWER_OVERRIDE,
    SHORT_ANSWER_TRIM_OVERRIDE,
    SHORT_ANSWER_BOUNDARY_FIX,
)
from migration.sourcemeta import build_source_meta
import json

from iqa.model import Question, SECTION_SEQUENCES, QuestionType, Level, SectionName

MIGRATION_DATE = date(2026, 9, 4)

TRACK_PREFIX = {
    "python": "py",
    "cpp": "cpp",
    "cs": "cs",
    "systems": "sys",
    "databases": "db",
    "engineering": "eng",
    "system-design": "sd",
    "behavioral": "bhv",
    "embedded": "emb",
    "data-science": "ds",
    "machine-learning": "ml",
    "data-engineering": "de",
    "backend": "be",
    "devops": "ops",
    "qa-automation": "qa",
}

OLD_TYPE_DEFAULT = {
    "Mechanism": "mechanism",
    "Contrast": "comparison",
    "Trap": "pitfall",
    "Scenario": "practical",
    # Code has no default: every Code card must appear in TYPE_OVERRIDE.
}

OLD_LEVEL = {"Middle": "middle", "Senior": "senior", "Junior": "junior"}

EN_TITLES = json.loads((ROOT / "tools" / "migration" / "en_titles.json").read_text(encoding="utf-8"))

STOPWORDS = {
    "a", "an", "the", "of", "in", "on", "to", "for", "with", "and", "or", "but",
    "not", "that", "this", "these", "those", "as", "at", "by", "from", "into",
    "than", "then", "so", "if", "can", "could", "should", "would", "will",
    "shall", "must", "may", "might", "it", "its", "their", "your", "you", "we",
    "i", "he", "she", "they", "them", "his", "her", "our", "us", "between",
    "about", "because", "while", "after", "before", "under", "over", "without",
    "within", "through", "what", "how", "why", "when", "which", "who", "whom",
    "does", "do", "did", "is", "are", "was", "were", "be", "being", "been",
    "one", "two", "s", "t", "d", "m", "re", "ve", "ll", "each", "every",
}


def slugify_title(en_title: str) -> str:
    words = re.findall(r"[a-z0-9]+", en_title.lower())
    significant = [w for w in words if w not in STOPWORDS and len(w) > 1]
    if len(significant) < 3:
        significant = [w for w in words if len(w) > 1]
    slug_words = significant[:7]
    slug = "-".join(slug_words)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "question"


TAG_STOP = {
    "self", "cls", "none", "true", "false", "def", "class", "import", "from",
    "return", "if", "else", "elif", "for", "while", "try", "except", "finally",
    "raise", "with", "as", "async", "await", "yield", "lambda", "pass",
}


def extract_tags(front_html: str, limit: int = 5) -> list[str]:
    terms = re.findall(r"<code>(.*?)</code>", front_html)
    tags: list[str] = []
    seen: set[str] = set()
    for term in terms:
        cleaned = re.sub(r"<[^>]+>", "", term)
        cleaned = cleaned.strip("_").lower()
        cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned)
        cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")
        if not cleaned or cleaned in TAG_STOP or cleaned.isdigit() or len(cleaned) < 2:
            continue
        if cleaned in seen:
            continue
        seen.add(cleaned)
        tags.append(cleaned)
        if len(tags) >= limit:
            break
    return tags


VERSION_TAG = {"Py3_14": "3.14", "Py3_15_preview": "3.15 (preview)"}


def build_applies_to(tags: dict[str, list[str]]) -> tuple[dict, ...]:
    gil = tags.get("gil", [None])[0]
    runtime = tags.get("runtime", [None])[0]
    version_tag = tags.get("version", [None])[0]
    version = VERSION_TAG.get(version_tag) if version_tag else None

    if gil == "Enabled":
        return ({"product": "CPython with GIL", "version": version},)
    if gil == "FreeThreaded":
        return ({"product": "CPython free-threaded build", "version": version},)
    if runtime == "CPython":
        return ({"product": "CPython", "version": version},)
    return ()


def build_execution(card: dict, short_answer_md: str) -> dict | None:
    check = card.get("code_check")
    if not check:
        return None
    if "```" not in short_answer_md:
        return None
    if check.get("status") != "verified":
        return None
    version = re.sub(r"^Python\s+", "", check["python_version"].strip())
    return {
        "language": "python",
        "standard": None,
        "toolchain": {"name": "cpython", "version": version},
        "flags": [],
    }


def resolve_source_url_meta(url: str, registry: dict[str, dict]) -> dict:
    if url not in registry:
        registry[url] = build_source_meta(url)
    return registry[url]


def build_sources(card: dict, url_registry: dict[str, dict]) -> list[dict]:
    sources: list[dict] = []
    used_ids: set[str] = set()

    def add(url: str, kind: str) -> str:
        meta = resolve_source_url_meta(url, url_registry)
        source_id = meta["source_id"]
        suffix = 2
        base_id = source_id
        while source_id in used_ids:
            source_id = f"{base_id}-{suffix}"
            suffix += 1
        used_ids.add(source_id)
        sources.append(
            {
                "source_id": source_id,
                "title": meta["title"],
                "url": url,
                "accessed": MIGRATION_DATE.isoformat(),
                "kind": kind,
                "version": meta["version"],
                "uk_applicability": meta["uk_applicability"],
                "en_applicability": meta["en_applicability"],
            }
        )
        return source_id

    official_ids = [add(url, "official") for url in card["official_refs"]]
    if card["community_ref"]:
        add(card["community_ref"], "community")
    return sources, official_ids


CITATION_STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "to", "for", "with", "and", "or",
    "not", "is", "are", "was", "were", "does", "do", "did", "how", "what",
    "why", "when", "which", "than", "that", "this", "into", "from",
    "python", "value", "object", "method", "function", "code",
}


def best_citation_source(card: dict, sources: list[dict], official_ids: list[str]) -> tuple[str | None, bool]:
    """Pick the official source whose URL best matches this card's own claim.

    front-sources.csv gives one official_refs LIST per legacy topic file, not
    one per card (verified: 22 of 23 topic files share one identical set
    across every card in that file). Falling back to "always cite refs[0]"
    would occasionally cite a page that has nothing to do with the specific
    claim (seen on 20_practical_coding, whose shared set is generic
    tutorial/reference/threading/time.monotonic pages). This scores every
    candidate by keyword overlap between the English title and the URL's own
    path/fragment words, and returns (best_source_id, matched) - `matched`
    is False when no candidate shares a single significant word with the
    title, which is reported rather than silently citing refs[0] anyway.
    """
    title_words = {
        w for w in re.findall(r"[a-z0-9]+", card["en_title"].lower())
        if w not in CITATION_STOPWORDS and len(w) > 2
    }
    by_id = {s["source_id"]: s for s in sources}
    best_id, best_score = None, -1
    for source_id in official_ids:
        url = by_id[source_id]["url"]
        parsed = urlparse(url)
        path_words = set(re.findall(r"[a-z0-9]+", (parsed.path + " " + parsed.fragment).lower()))
        score = len(title_words & path_words)
        if score > best_score:
            best_score, best_id = score, source_id
    return best_id, best_score > 0


def resolve_short_answer(cid: str, back_html: str) -> str:
    if cid in UK_SHORT_ANSWER_OVERRIDE:
        return UK_SHORT_ANSWER_OVERRIDE[cid]
    if cid in SHORT_ANSWER_BOUNDARY_FIX:
        return SHORT_ANSWER_BOUNDARY_FIX[cid]
    if cid in SHORT_ANSWER_TRIM_OVERRIDE:
        return SHORT_ANSWER_TRIM_OVERRIDE[cid]
    md, _ = back_to_short_answer_md(back_html)
    return md


def attach_citation(short_answer_md: str, source_id: str | None) -> str:
    """Insert `[^source_id]` right after the bold lead sentence's closing `**`.

    A naive `^\\*\\*(.*?)\\*\\*` stops at the *first* "**" it sees. That is
    wrong whenever the bold lead itself quotes code containing a literal
    "**" - the power operator (`` `-3 ** 2` ``) or a `**kwargs`/`**unpack`
    spread - which happened on 4 of the 392 migrated cards and corrupted the
    citation placement (caught independently by `tools/verify_build.py`'s
    "raw citation token leaked into HTML" check). Inline code spans are
    masked out before the search so only a real markdown "**" delimiter is
    seen; the mask is scoped to the text before the first blank line (or
    fenced code block), since the bold lead is always there.
    """
    if source_id is None:
        return short_answer_md
    boundary = len(short_answer_md)
    for marker in ("\n\n", "\n```", "```"):
        pos = short_answer_md.find(marker)
        if pos != -1:
            boundary = min(boundary, pos)
    head, tail = short_answer_md[:boundary], short_answer_md[boundary:]

    placeholders: list[str] = []

    def _mask(m: re.Match[str]) -> str:
        placeholders.append(m.group(0))
        return f"\x00CODE{len(placeholders) - 1}\x00"

    masked_head = re.sub(r"`[^`\n]*`", _mask, head)
    match = re.match(r"^\*\*(.*?)\*\*", masked_head, re.DOTALL)
    if not match:
        return short_answer_md
    token = f"[^{source_id}]"
    insert_at = match.end()
    masked_head = masked_head[:insert_at] + token + masked_head[insert_at:]

    def _unmask(m: re.Match[str]) -> str:
        return placeholders[int(m.group(1))]

    head = re.sub(r"\x00CODE(\d+)\x00", _unmask, masked_head)
    return head + tail


def plain_description(text: str, limit: int = 220) -> str:
    text = text.replace("`", "")
    text = re.sub(r'<span class="warn">|</span>', "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        cut = text.rfind(" ", 0, limit)
        text = text[: cut if cut > 0 else limit].rstrip(",;: ") + "..."
    return text


def section_body(question_type: str, level: str, uk_short_answer: str | None) -> list[tuple[str, str]]:
    """[(heading, content)] in contract order for this type/level, English headings."""
    qtype = QuestionType(question_type)
    qlevel = Level(level)
    sections = []
    for name in SECTION_SEQUENCES[qtype]:
        if name is SectionName.EVALUATION_GUIDE and qlevel is Level.JUNIOR:
            continue
        if name is SectionName.FOLLOW_UP:
            continue  # never present: only allowed for junior, and we have none
        if name is SectionName.SOURCES:
            content = "<!-- generated from frontmatter -->"
        elif name is SectionName.SHORT_ANSWER and uk_short_answer is not None:
            content = uk_short_answer
        else:
            content = "TODO"
        sections.append((name.value, content))
    return sections


def render_markdown(frontmatter_yaml: str, sections: list[tuple[str, str]]) -> str:
    body_parts = [f"## {heading}\n\n{content}\n" for heading, content in sections]
    return frontmatter_yaml + "\n" + "\n".join(body_parts)


def yaml_str(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_frontmatter(
    *,
    qid: str,
    title: str,
    description: str,
    track: str,
    section: str,
    level: str,
    qtype: str,
    tags: list[str],
    execution: dict | None,
    applies_to: tuple[dict, ...],
    anki_export: bool,
    sources: list[dict],
    lang: str,
    other_lang: str,
) -> str:
    lines = ["---"]
    lines.append(f"id: {qid}")
    lines.append(f"title: {yaml_str(title)}")
    lines.append(f"description: {yaml_str(description)}")
    lines.append(f"track: {track}")
    lines.append(f"section: {section}")
    lines.append(f"level: {level}")
    lines.append(f"type: {qtype}")
    if tags:
        lines.append("tags: [" + ", ".join(tags) + "]")
    else:
        lines.append("tags: []")
    lines.append("status: published")
    lines.append(f"updated: {MIGRATION_DATE.isoformat()}")
    lines.append("content_revision: 1")
    lines.append("reconciled_with:")
    lines.append(f"  {other_lang}: 1")
    if execution is not None:
        lines.append("execution:")
        lines.append(f"  language: {execution['language']}")
        lines.append("  standard: null")
        lines.append("  toolchain:")
        lines.append(f"    name: {execution['toolchain']['name']}")
        lines.append(f"    version: {yaml_str(execution['toolchain']['version'])}")
        lines.append("  flags: []")
    if applies_to:
        lines.append("applies_to:")
        for item in applies_to:
            lines.append(f"  - product: {yaml_str(item['product'])}")
            version = item["version"]
            lines.append(f"    version: {yaml_str(version) if version is not None else 'null'}")
    lines.append("anki:")
    lines.append(f"  export: {'true' if anki_export else 'false'}")
    lines.append("sources:")
    for source in sources:
        applicability = source["uk_applicability"] if lang == "uk" else source["en_applicability"]
        lines.append(f"  - source_id: {source['source_id']}")
        lines.append(f"    title: {yaml_str(source['title'])}")
        lines.append(f"    url: {source['url']}")
        lines.append(f"    accessed: {source['accessed']}")
        lines.append(f"    kind: {source['kind']}")
        version = source["version"]
        lines.append(f"    version: {yaml_str(version) if version is not None else 'null'}")
        lines.append(f"    applicability: {yaml_str(applicability)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cards = legacy_reader.load_all()
    print(f"checkpoint 1: loaded {len(cards)} legacy cards (expected 392)")

    # ---- classify + assign (track, section) --------------------------------
    rejected = []
    for card in cards:
        cid = card["legacy_card_id"]
        old_type = card["tags"]["type"][0]
        new_type = TYPE_OVERRIDE.get(cid) or OLD_TYPE_DEFAULT.get(old_type)
        if new_type is None:
            rejected.append((cid, f"no type mapping for old type {old_type}"))
            continue
        card["new_type"] = new_type
        card["new_level"] = OLD_LEVEL[card["tags"]["level"][0]]
        card["export"] = cid not in CODING_EXPORT_FALSE
        if cid in SECTION_OVERRIDE:
            card["track"], card["section"] = SECTION_OVERRIDE[cid]
        else:
            card["track"], card["section"] = TOPIC_FILE_SECTION[card["topic_file"]]

    if rejected:
        print(f"checkpoint 1: REJECTED {len(rejected)} cards:")
        for cid, reason in rejected:
            print(f"  {cid}: {reason}")
    accepted = [c for c in cards if c["legacy_card_id"] not in {r[0] for r in rejected}]
    print(f"checkpoint 1: {len(accepted)} accepted, {len(rejected)} rejected, "
          f"{len(accepted) + len(rejected)} accounted for (expected 392)")

    # ---- id issuance ---------------------------------------------------------
    registry_path = ROOT / "meta" / "id-registry.csv"
    with registry_path.open(encoding="utf-8", newline="") as handle:
        existing_registry = list(csv.DictReader(handle))
    existing_ids = {row["id"] for row in existing_registry}

    section_prefixes = dict(EXISTING_PREFIXES)
    section_prefixes.update(NEW_PREFIXES)

    counters: dict[str, int] = {}
    for row in existing_registry:
        # e.g. cs-cmplx-0001 -> counter key "cs/cmplx"
        parts = row["id"].split("-")
        num = int(parts[-1])
        key = "-".join(parts[:-1])
        counters[key] = max(counters.get(key, 0), num)

    new_registry_rows = []
    for card in sorted(accepted, key=lambda c: (c["topic_file"], c["order_in_file"])):
        track = card["track"]
        section = card["section"]
        section_path = f"{track}/{section}"
        prefix = section_prefixes.get(section_path)
        if prefix is None:
            raise SystemExit(f"no section prefix registered for {section_path}")
        track_prefix = TRACK_PREFIX[track]
        counter_key = f"{track_prefix}-{prefix}"
        counters[counter_key] = counters.get(counter_key, 0) + 1
        qid = f"{track_prefix}-{prefix}-{counters[counter_key]:04d}"
        if qid in existing_ids:
            raise SystemExit(f"id collision: {qid} already in registry")
        existing_ids.add(qid)
        card["id"] = qid

    print(f"checkpoint 2: issued {len(accepted)} new ids "
          f"({len(existing_registry)} pre-existing pilot ids untouched)")

    # ---- slugs (unique within track/section) ---------------------------------
    used_slugs: dict[str, set[str]] = {}
    url_registry: dict[str, dict] = {}
    for card in accepted:
        cid = card["legacy_card_id"]
        en_title = EN_TITLES[cid]
        slug = slugify_title(en_title)
        path_key = f"{card['track']}/{card['section']}"
        bucket = used_slugs.setdefault(path_key, set())
        base_slug = slug
        n = 2
        while slug in bucket:
            slug = f"{base_slug}-{n}"
            n += 1
        bucket.add(slug)
        card["slug"] = slug
        card["en_title"] = en_title

        uk_title = html_fragment_to_plain(card["front_html"])
        card["uk_title"] = uk_title

        short_answer_md = resolve_short_answer(cid, card["back_html"])
        sources, official_ids = build_sources(card, url_registry)
        card["weak_citation"] = False
        if card["new_type"] != "coding":
            best_id, matched = best_citation_source(card, sources, official_ids)
            short_answer_md = attach_citation(short_answer_md, best_id)
            card["weak_citation"] = not matched
        card["short_answer_md"] = short_answer_md
        card["sources"] = sources
        card["execution"] = build_execution(card, short_answer_md)
        card["applies_to"] = build_applies_to(card["tags"])
        card["tags_list"] = extract_tags(card["front_html"])

        # description = the bold lead claim of the (final, possibly overridden
        # or citation-tagged) Short answer - the same "key sentence" idea the
        # nine pilots use, read back from whatever text actually ships instead
        # of re-deriving it from the untouched legacy Back a second time.
        bold_lead_match = re.match(r"^\*\*(.*?)\*\*", short_answer_md, re.DOTALL)
        uk_key = bold_lead_match.group(1) if bold_lead_match else short_answer_md
        uk_key = re.sub(r"\[\^[a-z0-9-]+\]", "", uk_key)
        card["uk_description"] = plain_description(uk_key)
        # English description reuses the English title (QUESTIONS.md SS9: the
        # English file is a stub - inventing a second, independent English
        # sentence to summarise an answer that is not written in English
        # would be inventing English prose, which this step must not do).
        card["en_description"] = en_title

    # ---- write content files ---------------------------------------------
    content_root = ROOT / "content"
    written = 0
    export_false_report = []
    for card in accepted:
        cid = card["legacy_card_id"]
        qid = card["id"]
        track, section, slug = card["track"], card["section"], card["slug"]
        rel_path = Path(track) / section / f"{slug}.md"

        for lang, other in (("uk", "en"), ("en", "uk")):
            title = card["uk_title"] if lang == "uk" else card["en_title"]
            description = card["uk_description"] if lang == "uk" else card["en_description"]
            sections = section_body(
                card["new_type"], card["new_level"],
                card["short_answer_md"] if lang == "uk" else None,
            )
            frontmatter = build_frontmatter(
                qid=qid,
                title=title,
                description=description,
                track=track,
                section=section,
                level=card["new_level"],
                qtype=card["new_type"],
                tags=card["tags_list"],
                execution=card["execution"],
                applies_to=card["applies_to"],
                anki_export=card["export"],
                sources=card["sources"],
                lang=lang,
                other_lang=other,
            )
            text = render_markdown(frontmatter, sections)
            path = content_root / lang / rel_path
            if not args.dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8", newline="\n")
            written += 1

        if not card["export"]:
            export_false_report.append((qid, cid, card["en_title"]))

        new_registry_rows.append(
            {
                "id": qid,
                "created": MIGRATION_DATE.isoformat(),
                "status": "published",
                "current_path": rel_path.as_posix(),
            }
        )

    print(f"checkpoint 3: wrote {written} files ({written // 2} questions x 2 languages)")
    print(f"  anki.export=false: {len(export_false_report)} questions")
    for qid, cid, title in export_false_report:
        print(f"    {qid} ({cid}): {title}")

    if not args.dry_run:
        with registry_path.open("a", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            for row in new_registry_rows:
                writer.writerow([row["id"], row["created"], row["status"], row["current_path"]])
        print(f"checkpoint 2: appended {len(new_registry_rows)} rows to {registry_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
