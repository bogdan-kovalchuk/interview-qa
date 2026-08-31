"""The single implementation of the question lifecycle table."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict

from .model import Language, Question, SectionName, Status, required_text_sections


class Completeness(str, Enum):
    EMPTY = "empty"
    STUB = "stub"
    PARTIAL = "partial"
    COMPLETE = "complete"


class PageMode(str, Enum):
    ABSENT = "absent"
    PAGE = "page"
    TOMBSTONE = "tombstone"


class LifecycleDecision(BaseModel):
    model_config = ConfigDict(frozen=True)

    language: Language
    completeness: Completeness
    production_page: PageMode
    preview_page: PageMode
    navigation: bool
    card_in_apkg: bool
    reference_filled: bool
    card_blocked_reason: str | None


def _is_todo(question: Question, name: SectionName) -> bool:
    section = question.section(name)
    return section is None or section.content.strip() == "TODO"


def completeness_for(question: Question) -> Completeness:
    """Compute completeness from required textual sections only."""
    if _is_todo(question, SectionName.SHORT_ANSWER):
        return Completeness.EMPTY

    required = required_text_sections(
        question.frontmatter.type, question.frontmatter.level
    )
    if all(not _is_todo(question, section) for section in required):
        return Completeness.COMPLETE
    if not _is_todo(question, SectionName.DETAILED_EXPLANATION):
        return Completeness.PARTIAL
    return Completeness.STUB


def lifecycle_for(
    question: Question,
    language: Language | str,
    *,
    in_withdrawal_window: bool = False,
) -> LifecycleDecision:
    """Apply questions.md section 8 to one language of one question.

    ``in_withdrawal_window`` is release context that is not stored in a question.
    It controls the one conditional card state in the normative table.
    """
    requested_language = Language(language)
    if question.language is not requested_language:
        raise ValueError(
            f"question language is {question.language.value}, not {requested_language.value}"
        )

    completeness = completeness_for(question)
    status = question.frontmatter.status
    export_enabled = question.frontmatter.anki.export

    if status is Status.DRAFT:
        return LifecycleDecision(
            language=requested_language,
            completeness=completeness,
            production_page=PageMode.ABSENT,
            preview_page=PageMode.PAGE,
            navigation=False,
            card_in_apkg=False,
            reference_filled=False,
            card_blocked_reason="blocked:status-draft",
        )
    if status is Status.REVIEW:
        return LifecycleDecision(
            language=requested_language,
            completeness=completeness,
            production_page=PageMode.ABSENT,
            preview_page=PageMode.PAGE,
            navigation=False,
            card_in_apkg=False,
            reference_filled=False,
            card_blocked_reason="blocked:status-review",
        )
    if status is Status.WITHDRAWN:
        card = export_enabled and in_withdrawal_window
        if not export_enabled:
            reason = "blocked:anki-export-disabled"
        elif not in_withdrawal_window:
            reason = "blocked:outside-removal-window"
        else:
            reason = None
        return LifecycleDecision(
            language=requested_language,
            completeness=completeness,
            production_page=PageMode.TOMBSTONE,
            preview_page=PageMode.TOMBSTONE,
            navigation=False,
            card_in_apkg=card,
            reference_filled=card,
            card_blocked_reason=reason,
        )

    if not export_enabled:
        card = False
        reason = "blocked:anki-export-disabled"
    elif completeness is Completeness.EMPTY:
        card = False
        reason = "blocked:short-answer"
    else:
        card = True
        reason = None
    return LifecycleDecision(
        language=requested_language,
        completeness=completeness,
        production_page=PageMode.PAGE,
        preview_page=PageMode.PAGE,
        navigation=True,
        card_in_apkg=card,
        reference_filled=card,
        card_blocked_reason=reason,
    )
