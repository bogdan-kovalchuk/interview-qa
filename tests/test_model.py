from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from iqa.model import parse_question_file, question_schema, schema_json


ROOT = Path(__file__).resolve().parents[1]


def test_all_real_questions_parse_and_match_generated_schema() -> None:
    schema = question_schema()
    validator = Draft202012Validator(schema)
    files = sorted((ROOT / "content").rglob("*.md"))

    assert len(files) == 18
    for path in files:
        question = parse_question_file(path, content_root=ROOT / "content")
        assert list(validator.iter_errors(question.model_dump(mode="json"))) == []


def test_generated_schema_is_reproducible() -> None:
    path = ROOT / "meta" / "schema" / "question.schema.json"
    assert path.read_text(encoding="utf-8") == schema_json()
    assert json.loads(path.read_text(encoding="utf-8")) == question_schema()
