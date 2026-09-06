"""Bind every remaining Embedded Interview Lab record to a question ID.

Why this exists as its own pass, before a single file is written: the first
embedded import kept no record of which source record became which question,
so a re-run could not tell an already-imported record from a new one, and the
only way to answer "what is left" was to re-derive it by hand. Binding first
turns that into data.

`bind` allocates an ID per source record, reserves it in `meta/id-registry.csv`
and writes `meta/import/lab-source-map.csv`, keyed by the SHA-1 of the raw
Front. It is idempotent: a record already in the map keeps its ID, and no
number is ever issued twice, even if the pass is interrupted midway.

`status` shows how much of the bound set is written.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import pathlib
import re
import sys
from datetime import date
from difflib import SequenceMatcher

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from iqa import validate
from migration import labconv

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_DIR = (
    pathlib.Path.home() / "Documents/Projects/learning/Embeddedinterviewlab/01_C_Cpp_Foundations"
)
MAP_PATH = ROOT / "meta/import/lab-source-map.csv"
WORKLIST_PATH = ROOT / "meta/import/lab-worklist.csv"
REGISTRY_PATH = ROOT / "meta/id-registry.csv"
# `state` is the write status and `duplicate_review` the bind-time verdict. They were
# one column until a regeneration overwrote `review-duplicate` with `written` and the
# flag vanished: one column cannot carry two facts that change on different passes.
MAP_COLUMNS = [
    "source_file",
    "line",
    "front_sha1",
    "question_id",
    "section",
    "state",
    "duplicate_review",
]
REGISTRY_COLUMNS = ["id", "created", "status", "current_path"]

# Source file -> (target section, section prefix). Both come from
# meta/taxonomy.md and meta/vocabulary.yml, where they were reserved when the
# import started; nothing new is invented here. Files 01 and 02 are absent on
# purpose - they are already in content/ as emb-dtypes-* and emb-cppfound-*.
LAB_SECTIONS = {
    "03": ("structs-unions-and-bitfields", "structs"),
    "04": ("volatile-and-const", "volconst"),
    "05": ("function-pointers-and-callbacks", "fnptr"),
    "06": ("inline-and-macros", "macros"),
    "07": ("memory-alignment-and-endianness", "align"),
    "08": ("common-code-patterns", "patterns"),
    "09": ("cpp-classes-and-oop", "cppoop"),
    "10": ("raii-and-smart-pointers", "raii"),
    "11": ("templates-and-constexpr", "tmplcx"),
    "12": ("cpp-embedded-constraints-and-stl", "cppstl"),
}

# A pair this similar is not dropped automatically: collapsing "semantic
# duplicates" by score alone loses questions that only look alike. The record
# is bound like any other and flagged, so the decision stays with a reader.
DUPLICATE_THRESHOLD = 0.80

# The source's own CardType tag, which is the only classification it carries.
# `Trap` mapped onto `pitfall` exactly in the file-02 import; the split between
# `concept` and `mechanism` was a judgement call there and stays one here, so a
# later pass may reclassify a few. Everything lands `level: junior`, as file 02
# did - and junior is the level that must *not* carry an `Evaluation guide`.
CARD_TYPES = {"Conceptual": "concept", "Code": "mechanism", "Trap": "pitfall"}

SOURCE_LAB: dict[str, object] = {
    "source_id": "embeddedinterviewlab",
    "title": "Embedded Interview Lab",
    "url": "https://embeddedinterviewlab.com/",
    "kind": "community",
    "version": None,
    "applicability": {
        "en": "Source question and answer; answer not independently verified.",
        "uk": "Походження питання і відповіді; відповідь незалежно не перевірена.",
    },
}

# One authoritative source per section, because `sources` with only
# `kind: community` does not satisfy the claim gate. Both ids already exist in
# content/ with these exact fields - reusing them keeps one source_id meaning
# one document across the whole repository.
_ISO_C: dict[str, object] = {
    "source_id": "iso-c-n1570",
    "title": "ISO/IEC 9899:201x Committee Draft N1570",
    "url": "https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf",
    "kind": "spec",
    "version": "N1570",
    "applicability": {
        "en": "Authoritative section-level reference for the C language rules involved; "
        "specific devices and toolchains can differ.",
        "uk": "Авторитетне джерело рівня секції для згаданих правил мови C; "
        "конкретні пристрої й тулчейни можуть відрізнятися.",
    },
}
_ISO_CPP: dict[str, object] = {
    "source_id": "iso-cpp-n4861",
    "title": "C++ International Standard working draft N4861",
    "url": "https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf",
    "kind": "spec",
    "version": "N4861",
    "applicability": {
        "en": "Authoritative section-level reference for the C++ language rules involved; "
        "freestanding and vendor toolchains can differ.",
        "uk": "Авторитетне джерело рівня секції для згаданих правил мови C++; "
        "freestanding і вендорські тулчейни можуть відрізнятися.",
    },
}
SECTION_SOURCES = {
    "structs-unions-and-bitfields": _ISO_C,
    "volatile-and-const": _ISO_C,
    "function-pointers-and-callbacks": _ISO_C,
    "inline-and-macros": _ISO_C,
    "memory-alignment-and-endianness": _ISO_C,
    "common-code-patterns": _ISO_C,
    "cpp-classes-and-oop": _ISO_CPP,
    "raii-and-smart-pointers": _ISO_CPP,
    "templates-and-constexpr": _ISO_CPP,
    "cpp-embedded-constraints-and-stl": _ISO_CPP,
}

WORD_RE = re.compile(r"[\w'а-яіїєґ]+")


def _normalise(text: str) -> str:
    return " ".join(WORD_RE.findall(re.sub(r"<[^>]+>", " ", text).lower()))


def read_records() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for path in sorted(SOURCE_DIR.glob("*_anki_cards.txt")):
        number = path.name[:2]
        if number not in LAB_SECTIONS:
            continue
        section, prefix = LAB_SECTIONS[number]
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("#") or not line.strip():
                continue
            front = line.split("\t")[0]
            records.append(
                {
                    "source_file": path.name,
                    "line": str(line_number),
                    "front_sha1": hashlib.sha1(front.encode("utf-8")).hexdigest(),
                    "front": front,
                    "section": section,
                    "prefix": prefix,
                }
            )
    return records


def _load_map() -> dict[str, dict[str, str]]:
    if not MAP_PATH.exists():
        return {}
    with MAP_PATH.open(encoding="utf-8", newline="") as handle:
        return {row["front_sha1"]: row for row in csv.DictReader(handle)}


def _highest_issued(prefix: str, registry_ids: set[str]) -> int:
    pattern = re.compile(rf"^emb-{re.escape(prefix)}-(\d{{4}})$")
    numbers = [int(match.group(1)) for qid in registry_ids if (match := pattern.match(qid))]
    return max(numbers, default=0)


def _existing_titles() -> list[str]:
    titles = []
    for path in (ROOT / "content/uk/embedded").rglob("*.md"):
        match = re.search(r'^title:\s*"(.*)"\s*$', path.read_text(encoding="utf-8"), re.M)
        if match:
            titles.append(_normalise(match.group(1)))
    return titles


def bind(apply: bool) -> int:
    records = read_records()
    known_map = _load_map()
    with REGISTRY_PATH.open(encoding="utf-8", newline="") as handle:
        registry_ids = {row["id"] for row in csv.DictReader(handle)}

    counters = {
        prefix: _highest_issued(prefix, registry_ids) for _, prefix in LAB_SECTIONS.values()
    }
    candidates = [(title, "content") for title in _existing_titles()]

    rows: list[dict[str, str]] = []
    reserved: list[dict[str, str]] = []
    flagged: list[tuple[str, str, float]] = []
    for record in records:
        known = known_map.get(record["front_sha1"])
        if known is not None:
            rows.append({column: known[column] for column in MAP_COLUMNS})
            continue

        prefix = record["prefix"]
        counters[prefix] += 1
        qid = f"emb-{prefix}-{counters[prefix]:04d}"
        if qid in registry_ids:
            raise SystemExit(f"refusing to reissue `{qid}`: it is already in the registry")
        registry_ids.add(qid)

        title = _normalise(record["front"])
        score, _origin = max(
            ((SequenceMatcher(None, title, other).ratio(), tag) for other, tag in candidates),
            default=(0.0, ""),
        )
        duplicate = "yes" if score >= DUPLICATE_THRESHOLD else "no"
        if duplicate == "yes":
            flagged.append((qid, f"{record['source_file']}:{record['line']}", score))
        candidates.append((title, "batch"))

        rows.append(
            {
                "source_file": record["source_file"],
                "line": record["line"],
                "front_sha1": record["front_sha1"],
                "question_id": qid,
                "section": record["section"],
                "state": "bound",
                "duplicate_review": duplicate,
            }
        )
        reserved.append(
            {
                "id": qid,
                "created": date.today().isoformat(),
                "status": "reserved",
                "current_path": "",
            }
        )

    print(
        f"source records: {len(records)}   "
        f"already bound: {len(records) - len(reserved)}   new: {len(reserved)}"
    )
    for number, (section, prefix) in sorted(LAB_SECTIONS.items()):
        count = sum(1 for row in rows if row["section"] == section)
        print(f"  {number}  {section:36s} emb-{prefix}-0001..{counters[prefix]:04d}  ({count})")
    print(f"\nflagged for duplicate review: {len(flagged)}")
    for qid, where, score in flagged:
        print(f"  {qid}  {where}  similarity {score:.2f}")

    if not apply:
        print("\ndry run; pass --apply to write the map and reserve the IDs")
        return 0

    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MAP_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MAP_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with REGISTRY_PATH.open("a", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=REGISTRY_COLUMNS, lineterminator="\n").writerows(reserved)
    print(f"\nwrote {MAP_PATH.relative_to(ROOT).as_posix()} and reserved {len(reserved)} IDs")
    return 0


def _record_index() -> dict[str, tuple[str, str, str]]:
    """`front_sha1` -> (Front, Back, tags) for every remaining source record."""
    index: dict[str, tuple[str, str, str]] = {}
    for path in sorted(SOURCE_DIR.glob("*_anki_cards.txt")):
        if path.name[:2] not in LAB_SECTIONS:
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or not line.strip():
                continue
            columns = line.split("\t")
            front, back = columns[0], columns[1]
            tags = columns[2] if len(columns) > 2 else ""
            index[hashlib.sha1(front.encode("utf-8")).hexdigest()] = (front, back, tags)
    return index


def _short_answer_problems(text: str) -> list[str]:
    """Every hard `short-answer-limits` failure this text would raise.

    The gate functions are imported from the validator rather than restated,
    so a candidate is judged by the same code CI will judge it by. A record
    that fails is written as `TODO` and listed in the worklist - the import
    never lands a file that turns the build red.
    """
    problems = []
    sentences = validate._sentence_count(text)
    if not 2 <= sentences <= 5:
        problems.append(f"sentences={sentences}")
    if len(validate.CODE_BLOCK_RE.findall(text)) > 1:
        problems.append("more than one code block")
    outside = validate._without_code(text)
    if re.search(r"(?m)^\s{2,}(?:[-+*]|\d+[.)])\s+", outside):
        problems.append("nested list")
    if re.search(r"(?m)^#{1,6}[ \t]+", outside):
        problems.append("heading")
    outside_any = validate._without_any_code(text)
    if validate.MARKDOWN_LINK_RE.search(outside_any) or validate.READY_URL_RE.search(outside_any):
        problems.append("ready URL")
    if re.search(
        r"\A\s*\*\*(?:(?!\*\*).)*<span[ \t]+class=[\"']warn[\"']", outside, re.IGNORECASE | re.DOTALL
    ):
        problems.append("warn nested in key")
    return problems


def _description(short_answer: str, fallback: str) -> str:
    """A one-sentence Ukrainian summary, taken from the answer's own lead.

    `description` is required and has no fallback downstream - the question
    card in a list and `og:description` both read it - so it is derived here
    rather than left for a later pass to forget.
    """
    text = validate.CITATION_RE.sub("", validate._without_code(short_answer)).strip()
    text = re.sub(r"</?span[^>]*>", "", text)
    text = re.sub(r"[*`]", "", text)
    text = " ".join(text.split())
    if not text:
        return fallback
    match = re.search(r"^(.{20,240}?[.!?])(?:\s|$)", text)
    sentence = match.group(1) if match else text[:240].rstrip()
    return sentence


def _frontmatter(
    *,
    qid: str,
    title: str,
    description: str,
    section: str,
    question_type: str,
    language: str,
    other: str,
    sources: list[dict[str, object]],
) -> str:
    lines = [
        "---",
        f"id: {qid}",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "track: embedded",
        f"section: {section}",
        "level: junior",
        f"type: {question_type}",
        "tags: []",
        "status: published",
        f"updated: {date.today().isoformat()}",
        "content_revision: 1",
        "reconciled_with:",
        f"  {other}: 1",
        "anki:",
        "  export: true",
        "sources:",
    ]
    for source in sources:
        lines.append(f"  - source_id: {source['source_id']}")
        lines.append(f"    title: {json.dumps(source['title'], ensure_ascii=False)}")
        lines.append(f"    url: {source['url']}")
        lines.append(f"    accessed: {date.today().isoformat()}")
        lines.append(f"    kind: {source['kind']}")
        version = source["version"]
        lines.append(f"    version: {'null' if version is None else json.dumps(version)}")
        lines.append(
            f"    applicability: {json.dumps(source['applicability'][language], ensure_ascii=False)}"
        )
    lines.append("---")
    return "\n".join(lines)


def _body(question_type: str, short_answer: str) -> str:
    sections = ["Short answer", "Detailed explanation"]
    if question_type == "pitfall":
        sections += ["Symptom", "Why it happens", "How to avoid"]
    parts = []
    for heading in sections:
        content = short_answer if heading == "Short answer" else "TODO"
        parts.append(f"## {heading}\n\n{content}\n")
    parts.append("## Sources\n\n<!-- generated from frontmatter -->\n")
    return "\n".join(parts)


def _section_titles(section: str, language: str, exclude: set[str]) -> dict[str, str]:
    """Titles already written in a section, by question id, minus `exclude`."""
    found: dict[str, str] = {}
    directory = ROOT / "content" / language / "embedded" / section
    for path in directory.glob("*.md") if directory.is_dir() else ():
        text = path.read_text(encoding="utf-8")
        qid = re.search(r"^id:\s*(\S+)", text, re.M)
        title = re.search(r'^title:\s*"(.*)"\s*$', text, re.M)
        if qid and title and qid.group(1) not in exclude:
            found[qid.group(1)] = title.group(1)
    return found


def _check_titles_are_distinct(
    rows: list[dict[str, str]],
    records: dict[str, tuple[str, str, str]],
    names: dict[str, dict[str, str]],
    section: str,
) -> None:
    """Refuse to write two questions that would carry the same title.

    Moving the code out of the question - the owner's decision, and the reason
    the earlier import's titles render as escaped HTML on the site - leaves
    several source records with the same bare phrase: three cards asking "what
    compiles here?" differ only in the snippet. Identical titles are legal
    frontmatter but useless in a section index, so they stop the batch here
    and are fixed with a `uk_title` override in the names file rather than
    discovered later by reading the site.
    """
    collisions: list[str] = []
    for language in ("uk", "en"):
        titles: dict[str, list[str]] = collections.defaultdict(list)
        for qid, title in _section_titles(
            section, language, {row["question_id"] for row in rows}
        ).items():
            titles[title].append(qid)
        for row in rows:
            qid = row["question_id"]
            if language == "uk":
                title = names[qid].get("uk_title") or labconv.split_front(
                    records[row["front_sha1"]][0]
                )[0]
            else:
                title = names[qid]["en_title"]
            titles[title].append(qid)
        for title, ids in sorted(titles.items()):
            if len(ids) > 1:
                collisions.append(f"  {language}: {title!r} -> {', '.join(sorted(ids))}")
    if collisions:
        raise SystemExit(
            "these questions would share a title inside one section; give the Ukrainian one a\n"
            '`uk_title` override, or a more specific `en_title`, in the names file:\n'
            + "\n".join(collisions)
        )


def generate(number: str, names_path: pathlib.Path, apply: bool) -> int:
    if number not in LAB_SECTIONS:
        raise SystemExit(f"unknown lab file `{number}`; expected one of {sorted(LAB_SECTIONS)}")
    section, _prefix = LAB_SECTIONS[number]
    names = json.loads(names_path.read_text(encoding="utf-8"))
    rows = [row for row in _load_map().values() if row["source_file"].startswith(number)]
    records = _record_index()

    missing = [row["question_id"] for row in rows if row["question_id"] not in names]
    if missing:
        raise SystemExit(f"{len(missing)} question(s) have no slug/en_title: {missing[:5]}")
    _check_titles_are_distinct(rows, records, names, section)

    written: list[tuple[str, str]] = []
    worklist: list[dict[str, str]] = []
    for row in rows:
        qid = row["question_id"]
        front, back, tags = records[row["front_sha1"]]
        question_type = CARD_TYPES.get(tags.split()[0] if tags.split() else "", "concept")

        title = names[qid].get("uk_title") or labconv.split_front(front)[0]
        _title, code, lang = labconv.split_front(front)
        answer, _lang = labconv.back_to_short_answer(back)
        if code is not None:
            answer = f"```{lang}\n{code}\n```\n\n{answer}"
        answer = f"{answer}[^embeddedinterviewlab]"

        # A duplicate flag set at bind time would otherwise be overwritten by
        # `written` and lost. It belongs in the worklist anyway: one list of
        # everything a person still has to look at, not two.
        if row["duplicate_review"] == "yes":
            worklist.append(
                {
                    "question_id": qid,
                    "source": f"{row['source_file']}:{row['line']}",
                    "reason": "possible duplicate of an existing question",
                }
            )

        problems = _short_answer_problems(answer)
        if problems:
            worklist.append(
                {
                    "question_id": qid,
                    "source": f"{row['source_file']}:{row['line']}",
                    "reason": "; ".join(problems),
                }
            )
            uk_answer = "TODO"
            description = names[qid]["en_title"]
        else:
            uk_answer = answer
            description = _description(answer, names[qid]["en_title"])

        slug = names[qid]["slug"]
        relative = f"embedded/{section}/{slug}.md"
        sources = [SOURCE_LAB, SECTION_SOURCES[section]]
        files = {
            "uk": _frontmatter(
                qid=qid,
                title=title,
                description=description,
                section=section,
                question_type=question_type,
                language="uk",
                other="en",
                sources=sources,
            )
            + "\n\n"
            + _body(question_type, uk_answer),
            "en": _frontmatter(
                qid=qid,
                title=names[qid]["en_title"],
                description=names[qid]["en_title"],
                section=section,
                question_type=question_type,
                language="en",
                other="uk",
                sources=sources,
            )
            + "\n\n"
            + _body(question_type, "TODO"),
        }
        if apply:
            for language, text in files.items():
                path = ROOT / "content" / language / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
        written.append((qid, relative))

    print(f"lab file {number} -> {section}: {len(written)} questions, {len(worklist)} for the worklist")
    for item in worklist:
        print(f"  {item['question_id']}  {item['source']}  {item['reason']}")
    if not apply:
        print("\ndry run; pass --apply to write the files")
        return 0

    paths = dict(written)
    with REGISTRY_PATH.open(encoding="utf-8", newline="") as handle:
        registry = list(csv.DictReader(handle))
    for entry in registry:
        if entry["id"] in paths:
            entry["status"] = "published"
            entry["current_path"] = paths[entry["id"]]
    with REGISTRY_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REGISTRY_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(registry)

    rows_all = list(_load_map().values())
    for row in rows_all:
        if row["question_id"] in paths:
            row["state"] = "written"
    with MAP_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MAP_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_all)

    WORKLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if WORKLIST_PATH.exists():
        with WORKLIST_PATH.open(encoding="utf-8", newline="") as handle:
            existing = [r for r in csv.DictReader(handle) if r["question_id"] not in paths]
    with WORKLIST_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["question_id", "source", "reason"], lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(existing + worklist)

    print(f"\nwrote {2 * len(written)} files, updated the registry, the map and the worklist")
    return 0


def status() -> int:
    rows = list(_load_map().values())
    if not rows:
        print("nothing bound yet; run `bind --apply`")
        return 0
    written = {
        match.group(1)
        for path in (ROOT / "content/uk/embedded").rglob("*.md")
        if (match := re.search(r"^id:\s*(\S+)", path.read_text(encoding="utf-8"), re.M))
    }
    done = sum(1 for row in rows if row["question_id"] in written)
    print(f"bound {len(rows)}   written {done}   pending {len(rows) - done}")
    for number, (section, _prefix) in sorted(LAB_SECTIONS.items()):
        group = [row for row in rows if row["section"] == section]
        ready = sum(1 for row in group if row["question_id"] in written)
        print(f"  {number}  {section:36s} {ready:3d}/{len(group):3d}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    bind_parser = sub.add_parser("bind", help="allocate and reserve IDs for the source records")
    bind_parser.add_argument("--apply", action="store_true", help="write; otherwise dry run")
    generate_parser = sub.add_parser("generate", help="write the skeletons for one lab file")
    generate_parser.add_argument("number", help="lab file number, e.g. `03`")
    generate_parser.add_argument(
        "--names",
        type=pathlib.Path,
        required=True,
        help="JSON of {question_id: {slug, en_title}} - the one step a script cannot do",
    )
    generate_parser.add_argument("--apply", action="store_true", help="write; otherwise dry run")
    sub.add_parser("status", help="how much of the bound set is written")
    args = parser.parse_args(argv)
    if args.command == "bind":
        return bind(args.apply)
    if args.command == "generate":
        return generate(args.number, args.names, args.apply)
    return status()


if __name__ == "__main__":
    sys.exit(main())
