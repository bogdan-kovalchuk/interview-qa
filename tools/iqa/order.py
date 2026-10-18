"""Reading order of the questions inside a section: ``meta/order.yml``.

A section reads in question-ID order by default, which is the order of the deck it
came from. A section whose questions came from several sources, or got questions
added later, lists its question IDs in ``meta/order.yml`` from easiest to hardest.
A listed section lists every one of its questions exactly once; the validator
checks that. The site navigation and the Anki decks both sort through
``sort_key``, so the two can never disagree.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def load_order(path: Path) -> dict[str, list[str]]:
    """``{"track/section": [question id, ...]}``; empty when the file does not exist."""
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a mapping of `track/section` to a list of ids")
    return {str(key): [str(item) for item in (value or [])] for key, value in data.items()}


def positions(order: dict[str, list[str]]) -> dict[str, int]:
    """Question id -> its position inside its listed section."""
    return {
        question_id: index
        for listed in order.values()
        for index, question_id in enumerate(listed)
    }


def sort_key(position_of: dict[str, int], question_id: str) -> tuple[int, str]:
    """Listed questions by their position; unlisted sections fall back to the id."""
    return (position_of.get(question_id, 0), question_id)
