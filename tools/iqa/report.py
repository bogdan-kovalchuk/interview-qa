"""The progress report: dist/export/progress.{json,csv} and ``python -m iqa report``.

Single generator for the table described in meta/SITE.md's "Звіт прогресу" - one row
per question, per-language columns, and the same table rolled up by section, track,
project, language, question type and body-section field. Everything here is derived
from ``tools/iqa/model.py`` and ``tools/iqa/lifecycle.py``; there is no second notion
of "done" - ``completeness`` and the lifecycle decision are read, never recomputed.

``/{lang}/status/`` on the site renders ``dist/export/progress.json`` (mirrored into
``site/src/data/`` by ``site/scripts/build.mjs``, the same way ``tools/iqa/mirror.py``
mirrors ``content/`` - the site never reads ``content/`` or ``dist/export/`` directly,
only its own generated copy). ``dist/export/progress.csv`` is for opening in a
spreadsheet, per meta/SITE.md.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from typing import Any

from .export import group_by_id, read_all_questions
from .lifecycle import Completeness, _is_todo, lifecycle_for
from .mirror import QID_TOKEN_RE
from .model import Language, Question, required_text_sections


# Identical formula to packaging/anki/build.py:guid_for and
# packaging/anki/test-deck/build_test_deck.py:guid_for (meta/ANKI.md "GUID").
# This is a second reading of the frozen formula, not a second definition of it -
# the same relationship packaging/anki/build.py already documents against the
# test-deck copy. tests/test_report.py asserts all three agree.
GUID_SALT = "iqa:v1:"
BASE91 = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)


def guid_for(qid: str) -> str:
    digest = hashlib.sha256((GUID_SALT + qid).encode("utf-8")).digest()[:8]
    n = int.from_bytes(digest, "big")
    out: list[str] = []
    while n:
        n, rem = divmod(n, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out)) or BASE91[0]


def _qid_targets(question: Question) -> set[str]:
    return {match.group(1).lower() for match in QID_TOKEN_RE.finditer(question.body.raw)}


def _missing_required_sections(question: Question) -> list[str]:
    required = required_text_sections(question.frontmatter.type, question.frontmatter.level)
    return [section.value for section in required if _is_todo(question, section)]


def _language_row(
    question: Question | None,
    other: Question | None,
    known_ids: set[str],
) -> dict[str, Any]:
    if question is None:
        return {
            "exists": False,
            "completeness": None,
            "needs_reconciliation": False,
            "qid_resolvable": None,
            "card": None,
            "missing_required_sections": [],
            "updated": None,
        }

    decision = lifecycle_for(question, question.language)
    if decision.card_in_apkg:
        card = "ships"
    else:
        card = decision.card_blocked_reason

    needs_reconciliation = False
    if other is not None:
        own_view_of_other = question.frontmatter.reconciled_with.get(other.language)
        if own_view_of_other is not None:
            needs_reconciliation = other.frontmatter.content_revision > own_view_of_other

    targets = _qid_targets(question)
    qid_resolvable = all(target in known_ids for target in targets) if targets else True

    return {
        "exists": True,
        "completeness": decision.completeness.value,
        "needs_reconciliation": needs_reconciliation,
        "qid_resolvable": qid_resolvable,
        "card": card,
        "missing_required_sections": _missing_required_sections(question),
        "updated": question.frontmatter.updated.isoformat(),
    }


def _question_row(question_id: str, by_language: dict[Language, Question], known_ids: set[str]) -> dict[str, Any]:
    primary = by_language.get(Language.EN) or next(iter(by_language.values()))
    frontmatter = primary.frontmatter

    languages: dict[str, Any] = {}
    for language in Language:
        question = by_language.get(language)
        other = next((q for lang, q in by_language.items() if lang is not language), None)
        languages[language.value] = _language_row(question, other, known_ids)

    updated_values = [row["updated"] for row in languages.values() if row["updated"]]
    sources = frontmatter.sources
    non_community = sum(1 for source in sources if source.kind.value != "community")

    return {
        "id": question_id,
        "track": frontmatter.track,
        "section": frontmatter.section,
        "slug": primary.slug,
        "status": frontmatter.status.value,
        "level": frontmatter.level.value,
        "type": frontmatter.type.value,
        "guid": guid_for(question_id),
        "sources_count": len(sources),
        "sources_has_noncommunity": non_community > 0,
        "programs": [],
        "updated": max(updated_values) if updated_values else None,
        "languages": languages,
    }


def _empty_completeness_counts() -> dict[str, int]:
    return {value.value: 0 for value in Completeness}


def _add_row_to_bucket(bucket: dict[str, Any], row: dict[str, Any]) -> None:
    bucket["total"] += 1
    for language_code, language_row in row["languages"].items():
        if not language_row["exists"]:
            continue
        per_language = bucket["languages"].setdefault(language_code, _empty_completeness_counts())
        per_language[language_row["completeness"]] += 1


def _new_bucket() -> dict[str, Any]:
    return {"total": 0, "languages": {}}


def build_aggregates(rows: list[dict[str, Any]], questions: list[Question]) -> dict[str, Any]:
    by_track: dict[str, Any] = {}
    by_section: dict[str, Any] = {}
    by_language: dict[str, Any] = {"en": _empty_completeness_counts(), "uk": _empty_completeness_counts()}
    by_type: dict[str, Any] = {}
    totals = _new_bucket()

    for row in rows:
        _add_row_to_bucket(totals, row)
        _add_row_to_bucket(by_track.setdefault(row["track"], _new_bucket()), row)
        section_key = f"{row['track']}/{row['section']}"
        _add_row_to_bucket(by_section.setdefault(section_key, _new_bucket()), row)
        _add_row_to_bucket(by_type.setdefault(row["type"], _new_bucket()), row)
        for language_code, language_row in row["languages"].items():
            if language_row["exists"]:
                by_language[language_code][language_row["completeness"]] += 1

    # Systemic gaps: for each body-section field (SectionName), how many questions that
    # require it actually have it written, per language. This is the cut meta/SITE.md
    # calls out as most useful - it is exactly how "392/401 miss Detailed explanation"
    # becomes visible as one row instead of being buried in per-question detail.
    by_section_field: dict[str, Any] = {}
    for question in questions:
        required = required_text_sections(question.frontmatter.type, question.frontmatter.level)
        for section in required:
            entry = by_section_field.setdefault(
                section.value, {"en": {"written": 0, "applicable": 0}, "uk": {"written": 0, "applicable": 0}}
            )
            language_entry = entry[question.language.value]
            language_entry["applicable"] += 1
            if not _is_todo(question, section):
                language_entry["written"] += 1

    return {
        "totals": totals,
        "by_track": by_track,
        "by_section": by_section,
        "by_language": by_language,
        "by_type": by_type,
        "by_section_field": by_section_field,
        "by_program": {},
    }


def build_report(content_root: Path) -> dict[str, Any]:
    questions = read_all_questions(content_root)
    grouped = group_by_id(questions)
    known_ids = set(grouped)

    rows = [_question_row(qid, grouped[qid], known_ids) for qid in sorted(grouped)]
    aggregates = build_aggregates(rows, questions)
    return {"questions": rows, "aggregates": aggregates}


CSV_FIELDS = [
    "id",
    "track",
    "section",
    "slug",
    "status",
    "level",
    "type",
    "guid",
    "sources_count",
    "sources_has_noncommunity",
    "updated",
    "en_exists",
    "en_completeness",
    "en_needs_reconciliation",
    "en_qid_resolvable",
    "en_card",
    "en_missing_required_sections",
    "uk_exists",
    "uk_completeness",
    "uk_needs_reconciliation",
    "uk_qid_resolvable",
    "uk_card",
    "uk_missing_required_sections",
]


def _csv_row(row: dict[str, Any]) -> dict[str, Any]:
    flat = {
        "id": row["id"],
        "track": row["track"],
        "section": row["section"],
        "slug": row["slug"],
        "status": row["status"],
        "level": row["level"],
        "type": row["type"],
        "guid": row["guid"],
        "sources_count": row["sources_count"],
        "sources_has_noncommunity": row["sources_has_noncommunity"],
        "updated": row["updated"] or "",
    }
    for language_code in ("en", "uk"):
        language_row = row["languages"][language_code]
        flat[f"{language_code}_exists"] = language_row["exists"]
        flat[f"{language_code}_completeness"] = language_row["completeness"] or ""
        flat[f"{language_code}_needs_reconciliation"] = language_row["needs_reconciliation"]
        flat[f"{language_code}_qid_resolvable"] = (
            "" if language_row["qid_resolvable"] is None else language_row["qid_resolvable"]
        )
        flat[f"{language_code}_card"] = language_row["card"] or ""
        flat[f"{language_code}_missing_required_sections"] = ";".join(
            language_row["missing_required_sections"]
        )
    return flat


def report_csv(report: dict[str, Any]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in report["questions"]:
        writer.writerow(_csv_row(row))
    return buffer.getvalue()


def report_json(report: dict[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_report(content_root: Path, json_destination: Path, csv_destination: Path) -> int:
    report = build_report(content_root)
    json_destination.parent.mkdir(parents=True, exist_ok=True)
    json_destination.write_text(report_json(report), encoding="utf-8", newline="\n")
    csv_destination.parent.mkdir(parents=True, exist_ok=True)
    csv_destination.write_text(report_csv(report), encoding="utf-8", newline="\n")
    return len(report["questions"])


def run(root: Path) -> int:
    """Write dist/export/progress.json and dist/export/progress.csv. Used by `iqa build`."""
    count = write_report(
        root / "content",
        root / "dist" / "export" / "progress.json",
        root / "dist" / "export" / "progress.csv",
    )
    print(f"Reported {count} questions into dist/export/progress.{{json,csv}}")
    return 0


def _print_todo(report: dict[str, Any]) -> None:
    """`iqa report --todo`: the next thing to write, grouped by track/section.

    Lists every (question, language) pair whose completeness is not `complete`,
    sorted by track/section/id so working through a section top to bottom clears it.
    Printed, not written - this is a "what next" read, not a build artefact.
    """
    pending = []
    for row in report["questions"]:
        for language_code in ("en", "uk"):
            language_row = row["languages"][language_code]
            if not language_row["exists"]:
                pending.append((row, language_code, "missing file"))
            elif language_row["completeness"] != Completeness.COMPLETE.value:
                missing = ", ".join(language_row["missing_required_sections"]) or "(nothing required missing)"
                pending.append((row, language_code, f"{language_row['completeness']}: {missing}"))

    pending.sort(key=lambda item: (item[0]["track"], item[0]["section"], item[0]["id"], item[1]))
    if not pending:
        print("Nothing to do: every question is complete in both languages.")
        return
    print(f"{len(pending)} (question, language) pairs are not complete:\n")
    for row, language_code, detail in pending:
        print(f"{row['track']}/{row['section']}  {row['id']}  {language_code}  {detail}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--todo",
        action="store_true",
        help="print the next incomplete (question, language) pairs instead of writing files",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()

    if args.todo:
        report = build_report(root / "content")
        _print_todo(report)
        return 0

    return run(root)


if __name__ == "__main__":
    raise SystemExit(main())
