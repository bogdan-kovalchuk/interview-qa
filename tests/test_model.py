from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from iqa.model import parse_body, parse_question_file, question_schema, schema_json


ROOT = Path(__file__).resolve().parents[1]


def test_all_real_questions_parse_and_match_generated_schema() -> None:
    schema = question_schema()
    validator = Draft202012Validator(schema)
    files = sorted((ROOT / "content").rglob("*.md"))

    assert len(files) == 802
    for path in files:
        question = parse_question_file(path, content_root=ROOT / "content")
        assert list(validator.iter_errors(question.model_dump(mode="json"))) == []


def test_a_comment_inside_a_fence_is_code_not_a_heading() -> None:
    """A `#` line at column 0 inside a code fence must stay code.

    A Markdown heading and a Python or shell comment are the same characters.
    Reading them as headings had two effects, both real: `# note` tripped the
    `sections` gate's "heading level 1 is forbidden", and `## note` became a
    phantom section, silently changing the section sequence the question is
    validated and rendered against.
    """
    body = "\n".join(
        [
            "## Short answer",
            "",
            "Text.",
            "",
            "## Detailed explanation",
            "",
            "Lead-in:",
            "",
            "```python",
            "# a standalone comment at column 0",
            "## still a comment, not a section",
            "def f():",
            "    ...",
            "```",
            "",
            "## Sources",
            "",
            "<!-- generated from frontmatter -->",
            "",
        ]
    )

    parsed = parse_body(body)

    assert [section.heading for section in parsed.sections] == [
        "Short answer",
        "Detailed explanation",
        "Sources",
    ]
    detailed = next(s for s in parsed.sections if s.heading == "Detailed explanation")
    assert "# a standalone comment at column 0" in detailed.content
    assert detailed.subsections == ()


def test_generated_schema_is_reproducible() -> None:
    path = ROOT / "meta" / "schema" / "question.schema.json"
    assert path.read_text(encoding="utf-8") == schema_json()
    assert json.loads(path.read_text(encoding="utf-8")) == question_schema()
