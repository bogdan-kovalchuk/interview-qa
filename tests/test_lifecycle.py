from __future__ import annotations

from pathlib import Path

import pytest

from iqa.lifecycle import Completeness, PageMode, completeness_for, lifecycle_for
from iqa.model import parse_question_text


FIXTURES = Path(__file__).parent / "fixtures"


def load_question(path: Path):
    return parse_question_text(
        path.read_text(encoding="utf-8"),
        language="en",
        slug="lifecycle-fixture-question",
        source_path=f"en/python/concurrency-and-gil/{path.name}",
    )


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("empty", Completeness.EMPTY),
        ("stub", Completeness.STUB),
        ("partial", Completeness.PARTIAL),
    ],
)
def test_todo_completeness_fixtures(name: str, expected: Completeness) -> None:
    question = load_question(FIXTURES / "states" / f"{name}.md")
    assert completeness_for(question) is expected


def test_draft_status_fixture() -> None:
    decision = lifecycle_for(load_question(FIXTURES / "statuses" / "draft.md"), "en")
    assert decision.production_page is PageMode.ABSENT
    assert decision.preview_page is PageMode.PAGE
    assert not decision.navigation
    assert not decision.card_in_apkg
    assert not decision.reference_filled
    assert decision.card_blocked_reason == "blocked:status-draft"


def test_review_status_fixture() -> None:
    decision = lifecycle_for(load_question(FIXTURES / "statuses" / "review.md"), "en")
    assert decision.production_page is PageMode.ABSENT
    assert decision.preview_page is PageMode.PAGE
    assert not decision.navigation
    assert not decision.card_in_apkg
    assert decision.card_blocked_reason == "blocked:status-review"


def test_published_status_fixture() -> None:
    decision = lifecycle_for(load_question(FIXTURES / "statuses" / "published.md"), "en")
    assert decision.production_page is PageMode.PAGE
    assert decision.preview_page is PageMode.PAGE
    assert decision.navigation
    assert decision.card_in_apkg
    assert decision.reference_filled
    assert decision.card_blocked_reason is None


def test_published_empty_card_is_blocked_only_by_short_answer() -> None:
    decision = lifecycle_for(load_question(FIXTURES / "states" / "empty.md"), "en")
    assert decision.production_page is PageMode.PAGE
    assert decision.navigation
    assert not decision.card_in_apkg
    assert decision.card_blocked_reason == "blocked:short-answer"


def test_withdrawn_status_fixture() -> None:
    question = load_question(FIXTURES / "statuses" / "withdrawn.md")
    outside = lifecycle_for(question, "en")
    inside = lifecycle_for(question, "en", in_withdrawal_window=True)

    assert outside.production_page is PageMode.TOMBSTONE
    assert outside.preview_page is PageMode.TOMBSTONE
    assert not outside.navigation
    assert not outside.card_in_apkg
    assert outside.card_blocked_reason == "blocked:outside-removal-window"
    assert inside.card_in_apkg
    assert inside.reference_filled
    assert inside.card_blocked_reason is None
