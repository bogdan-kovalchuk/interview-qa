"""Export the canonical machine-readable view of every question.

This is the single place that turns ``content/`` into data other tools consume:
the deck builder (``tools/iqa/anki.py``). Nothing downstream re-parses Markdown;
everything downstream reads this file.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
from typing import Any

from .model import Language, Question, SectionName, is_written, parse_question_file


def read_all_questions(content_root: Path) -> list[Question]:
    """Parse every question file under ``content_root`` through the canonical model.

    Shared with ``tools/iqa/verify_build.py`` so the expected page set it checks
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

    Citation tokens and Markdown syntax are left as authored - each consumer
    renders its own form, the same way a `qid:` token is materialised once per
    consumer rather than once in this file.
    """
    if not is_written(question, name):
        return None
    section = question.section(name)
    assert section is not None
    return section.content


def _language_payload(question: Question, base: str) -> dict[str, Any]:
    frontmatter = question.frontmatter
    return {
        "title": frontmatter.title,
        "slug": question.slug,
        "path": canonical_path(base, question.language, frontmatter.id, question.slug),
        "resolver_path": resolver_path(base, question.language, frontmatter.id),
        "sources": [source.model_dump(mode="json") for source in frontmatter.sources],
        # Only what a card is built from. The card ships exactly when
        # `short_answer` is written in this language; the explanation stays on
        # the site, which reads content/ through the mirror.
        "card": {
            "short_answer": _raw_section(question, SectionName.SHORT_ANSWER),
            "question_code": _raw_section(question, SectionName.QUESTION_CODE),
        },
    }


def _question_payload(
    question_id: str, by_language: dict[Language, Question], base: str
) -> dict[str, Any]:
    primary = by_language.get(Language.EN) or next(iter(by_language.values()))
    return {
        "id": question_id,
        "track": primary.frontmatter.track,
        "section": primary.frontmatter.section,
        "languages": {
            language.value: _language_payload(question, base)
            for language, question in sorted(by_language.items(), key=lambda item: item[0].value)
        },
    }


def build_export(content_root: Path, *, base: str = "/interview-qa") -> dict[str, Any]:
    base = "/" + base.strip("/")
    grouped = group_by_id(read_all_questions(content_root))
    return {
        "base": base,
        "questions": [_question_payload(qid, grouped[qid], base) for qid in sorted(grouped)],
    }


def write_export(content_root: Path, destination: Path, *, base: str = "/interview-qa") -> int:
    payload = build_export(content_root, base=base)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8", newline="\n")
    return len(payload["questions"])


def run(root: Path, base: str = "/interview-qa") -> int:
    """Write dist/export/questions.json for a repository root. Used by `iqa build`."""
    destination = root / "dist" / "export" / "questions.json"
    count = write_export(root / "content", destination, base=base)
    print(f"Exported {count} questions into {destination.as_posix()}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("content"))
    parser.add_argument("--out", type=Path, default=Path("dist/export/questions.json"))
    parser.add_argument("--base", default="/interview-qa")
    args = parser.parse_args()
    count = write_export(args.source.resolve(), args.out, base=args.base)
    print(f"Exported {count} questions into {args.out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
