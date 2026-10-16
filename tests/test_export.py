from __future__ import annotations

from pathlib import Path

from corpus import EN_CARDS, QUESTIONS, UK_CARDS
from iqa.export import build_export, canonical_path, resolver_path
from iqa.model import Language


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"


def test_export_covers_every_question_in_both_languages() -> None:
    payload = build_export(CONTENT)
    assert payload["base"] == "/interview-qa"
    assert len(payload["questions"]) == QUESTIONS
    for question in payload["questions"]:
        assert set(question) == {"id", "track", "section", "languages"}
        assert set(question["languages"]) == {"en", "uk"}


def test_paths_match_the_site_url_contract() -> None:
    payload = build_export(CONTENT)
    by_id = {question["id"]: question for question in payload["questions"]}
    py_gil = by_id["py-gil-0001"]["languages"]["uk"]
    assert py_gil["path"] == (
        "/interview-qa/uk/q/py-gil-0001/free-threaded-build-removes-the-gil-not-contention/"
    )
    assert py_gil["resolver_path"] == "/interview-qa/uk/q/py-gil-0001/"


def test_card_carries_only_the_short_answer_and_question_code() -> None:
    payload = build_export(CONTENT)
    written = {"en": 0, "uk": 0}
    for question in payload["questions"]:
        for language, entry in question["languages"].items():
            assert set(entry["card"]) == {"short_answer", "question_code"}
            if entry["card"]["short_answer"] is not None:
                written[language] += 1
    assert written == {"en": EN_CARDS, "uk": UK_CARDS}


def test_unwritten_short_answer_is_exported_as_none_not_todo() -> None:
    payload = build_export(CONTENT)
    answers = [
        entry["card"]["short_answer"]
        for question in payload["questions"]
        for entry in question["languages"].values()
    ]
    assert None in answers
    assert "TODO" not in answers


def test_helpers_agree_on_url_shape() -> None:
    assert canonical_path("/interview-qa", Language.UK, "py-gil-0001", "slug") == (
        "/interview-qa/uk/q/py-gil-0001/slug/"
    )
    assert resolver_path("/interview-qa", Language.UK, "py-gil-0001") == "/interview-qa/uk/q/py-gil-0001/"
