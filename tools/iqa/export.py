"""Export the canonical machine-readable view of every question.

This is the single place that turns ``content/`` into data other tools consume:
the deck builder (``anki/build.py``) and, later, the progress report.
Nothing downstream re-parses Markdown; everything downstream reads this file.

Per ``meta/decisions.md`` sections 5-6, cross-references (``see_also``,
``prerequisites``) are exported as ``{"qid": "..."}`` objects, never as URLs -
only the site and Anki materialise a ``qid:`` reference into a URL, and each
does so in its own form.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
from typing import Any

from .lifecycle import lifecycle_for
from .model import Language, Question, QuestionType, SectionName, parse_question_file


def read_all_questions(content_root: Path) -> list[Question]:
    """Parse every question file under ``content_root`` through the canonical model.

    Shared with ``tools/verify_build.py`` so the expected page set it checks
    against is computed the same way the export and the mirror compute theirs -
    one parse of the model, not a second Markdown reader.
    """
    return [
        parse_question_file(path, content_root=content_root)
        for path in sorted(content_root.rglob("*.md"))
    ]


def group_by_id(questions: list[Question]) -> dict[str, dict[Language, Question]]:
    grouped: dict[str, dict[Language, Question]] = defaultdict(dict)
    for question in questions:
        grouped[question.frontmatter.id][question.language] = question
    return grouped




def canonical_path(base: str, language: Language, question_id: str, slug: str) -> str:
    """The full canonical page path, with the readable slug."""
    return f"{base}/{language.value}/q/{question_id}/{slug}/"


def resolver_path(base: str, language: Language, question_id: str) -> str:
    """The short resolver-page path that content links and Anki materialise to."""
    return f"{base}/{language.value}/q/{question_id}/"


def _raw_section(question: Question, name: SectionName) -> str | None:
    """Raw (unrendered) Markdown of one section, or ``None`` if absent/unwritten (`TODO`).

    Citation tokens and Markdown syntax are left as authored - each consumer of
    questions.json renders its own form (the site mirror turns them into
    footnotes; the Anki builder strips them), the same way a `qid:` token is
    materialised once per consumer rather than once in this file.
    """
    section = question.section(name)
    if section is None or section.content.strip() == "TODO":
        return None
    return section.content


def _card_payload(question: Question) -> dict[str, Any]:
    """The only body content this export carries: exactly what meta/anki.md's

    field table says a card is built from - `Short answer` for every type, plus
    `Task`/`Constraints` for `coding` and `Scale prompt` for `system-design`.
    Everything else in the body stays in content/, read only by the site mirror.
    """
    question_type = question.frontmatter.type
    return {
        "short_answer": _raw_section(question, SectionName.SHORT_ANSWER),
        "task": (
            _raw_section(question, SectionName.TASK)
            if question_type is QuestionType.CODING
            else None
        ),
        "constraints": (
            _raw_section(question, SectionName.CONSTRAINTS)
            if question_type is QuestionType.CODING
            else None
        ),
        "scale_prompt": (
            _raw_section(question, SectionName.SCALE_PROMPT)
            if question_type is QuestionType.SYSTEM_DESIGN
            else None
        ),
    }


def _language_payload(
    question: Question, base: str, *, in_withdrawal_window: bool
) -> dict[str, Any]:
    decision = lifecycle_for(question, question.language, in_withdrawal_window=in_withdrawal_window)
    frontmatter = question.frontmatter
    return {
        "status": frontmatter.status.value,
        "title": frontmatter.title,
        "description": frontmatter.description,
        "slug": question.slug,
        "path": canonical_path(base, question.language, frontmatter.id, question.slug),
        "resolver_path": resolver_path(base, question.language, frontmatter.id),
        "updated": frontmatter.updated.isoformat(),
        "content_revision": frontmatter.content_revision,
        "reconciled_with": {
            language.value: revision for language, revision in frontmatter.reconciled_with.items()
        },
        "completeness": decision.completeness.value,
        "lifecycle": {
            "production_page": decision.production_page.value,
            "preview_page": decision.preview_page.value,
            "navigation": decision.navigation,
            "card_in_apkg": decision.card_in_apkg,
            "reference_filled": decision.reference_filled,
            "card_blocked_reason": decision.card_blocked_reason,
        },
        "sources": [
            source.model_dump(mode="json") for source in frontmatter.sources
        ],
        "card": _card_payload(question),
    }


def _question_payload(
    question_id: str,
    by_language: dict[Language, Question],
    base: str,
    *,
    in_withdrawal_window: bool,
) -> dict[str, Any]:
    # Language-neutral facets are authoritative on the English file (decisions.md #14);
    # fall back to whichever language exists so a question missing English stub still exports.
    primary = by_language.get(Language.EN) or next(iter(by_language.values()))
    frontmatter = primary.frontmatter
    return {
        "id": question_id,
        "track": frontmatter.track,
        "section": frontmatter.section,
        "level": frontmatter.level.value,
        "type": frontmatter.type.value,
        "tags": list(frontmatter.tags),
        "frameworks": list(frontmatter.frameworks),
        "anki": {"export": frontmatter.anki.export},
        "execution": (
            frontmatter.execution.model_dump(mode="json")
            if frontmatter.execution is not None
            else None
        ),
        "applies_to": [item.model_dump(mode="json") for item in frontmatter.applies_to],
        "see_also": [{"qid": target} for target in frontmatter.see_also],
        "prerequisites": [{"qid": target} for target in frontmatter.prerequisites],
        "languages": {
            language.value: _language_payload(
                question, base, in_withdrawal_window=in_withdrawal_window
            )
            for language, question in sorted(by_language.items(), key=lambda item: item[0].value)
        },
    }


def build_export(
    content_root: Path, *, base: str = "/interview-qa", in_withdrawal_window: bool = False
) -> dict[str, Any]:
    base = "/" + base.strip("/")
    questions = read_all_questions(content_root)
    grouped = group_by_id(questions)
    return {
        "base": base,
        "questions": [
            _question_payload(qid, grouped[qid], base, in_withdrawal_window=in_withdrawal_window)
            for qid in sorted(grouped)
        ],
    }


def export_json(
    content_root: Path, *, base: str = "/interview-qa", in_withdrawal_window: bool = False
) -> str:
    payload = build_export(content_root, base=base, in_withdrawal_window=in_withdrawal_window)
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_export(
    content_root: Path,
    destination: Path,
    *,
    base: str = "/interview-qa",
    in_withdrawal_window: bool = False,
) -> int:
    payload = build_export(content_root, base=base, in_withdrawal_window=in_withdrawal_window)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8", newline="\n")
    return len(payload["questions"])


def run(root: Path, base: str = "/interview-qa", in_withdrawal_window: bool = False) -> int:
    """Write dist/export/questions.json for a repository root. Used by `iqa build`."""
    payload = build_export(
        root / "content", base=base, in_withdrawal_window=in_withdrawal_window
    )
    destination = root / "dist" / "export" / "questions.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Exported {len(payload['questions'])} questions into {destination.as_posix()}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("content"))
    parser.add_argument("--out", type=Path, default=Path("dist/export/questions.json"))
    parser.add_argument("--base", default="/interview-qa")
    parser.add_argument(
        "--in-withdrawal-window",
        action="store_true",
        help="treat withdrawn questions as still inside their two-release removal window",
    )
    args = parser.parse_args()

    payload = build_export(
        args.source.resolve(), base=args.base, in_withdrawal_window=args.in_withdrawal_window
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Exported {len(payload['questions'])} questions into {args.out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
