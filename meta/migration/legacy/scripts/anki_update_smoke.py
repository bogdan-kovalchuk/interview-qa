#!/usr/bin/env python3
"""Prove that an updated package preserves an existing learner card's schedule."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from anki.collection import (
    Collection,
    DeckIdLimit,
    ExportAnkiPackageOptions,
    ImportAnkiPackageOptions,
    ImportAnkiPackageRequest,
)


ROOT = Path(__file__).resolve().parent.parent
AUTHORING = ROOT / "authoring" / "collection" / "Python Interview Questions.anki2"
PACKAGE = ROOT / "cards" / "Python Interview Questions.apkg"
ROOT_DECK = "Python Interview Questions"
CARD_ID = "PYI_01_001"
MARKER = "[APKG update smoke marker]"


def import_package(collection: Collection, package: Path, *, always_update: bool = False) -> None:
    collection.import_anki_package(
        ImportAnkiPackageRequest(
            package_path=str(package),
            options=ImportAnkiPackageOptions(
                update_notes=1 if always_update else 0,
                with_scheduling=False,
                with_deck_configs=False,
            ),
        )
    )


def state(collection: Collection, card_id: str) -> tuple[str, int, int, int, int, int, int, int]:
    note_ids = collection.find_notes(f"tag:card::{card_id}")
    if len(note_ids) != 1:
        raise ValueError(f"expected one note for {card_id}")
    note = collection.get_note(note_ids[0])
    card_ids = collection.find_cards(f"nid:{note.id}")
    if len(card_ids) != 1:
        raise ValueError(f"expected one card for {card_id}")
    card = collection.get_card(card_ids[0])
    return (note.guid, card.id, card.queue, card.due, card.ivl, card.reps, card.lapses, card.factor)


def run() -> dict[str, object]:
    with tempfile.TemporaryDirectory() as temporary_dir:
        temp = Path(temporary_dir)
        authoring_copy = temp / "authoring.anki2"
        package_v2 = temp / "Python Interview Questions v2.apkg"
        learner_path = temp / "learner.anki2"
        shutil.copy2(AUTHORING, authoring_copy)

        learner = Collection(str(learner_path))
        try:
            import_package(learner, PACKAGE)
            before = state(learner, CARD_ID)
            card = learner.get_card(before[1])
            card.queue = 2
            card.type = 2
            card.due = 47
            card.ivl = 13
            card.reps = 8
            card.lapses = 2
            card.factor = 2450
            learner.update_card(card)
            scheduled = state(learner, CARD_ID)

            authoring = Collection(str(authoring_copy))
            try:
                note_id = authoring.find_notes(f"tag:card::{CARD_ID}")[0]
                note = authoring.get_note(note_id)
                note["Back"] += MARKER
                authoring.update_note(note)
                root_id = authoring.decks.id(ROOT_DECK)
                authoring.export_anki_package(
                    out_path=str(package_v2),
                    options=ExportAnkiPackageOptions(
                        with_scheduling=False,
                        with_deck_configs=False,
                        with_media=True,
                        legacy=False,
                    ),
                    limit=DeckIdLimit(deck_id=root_id),
                )
            finally:
                authoring.close()

            import_package(learner, package_v2, always_update=True)
            after = state(learner, CARD_ID)
            note_id = learner.find_notes(f"tag:card::{CARD_ID}")[0]
            if MARKER not in learner.get_note(note_id)["Back"]:
                raise ValueError("updated package did not update the card Back")
            if scheduled != after:
                raise ValueError(f"scheduling changed: before={scheduled}, after={after}")
            return {"card_id": CARD_ID, "guid": after[0], "card_db_id": after[1], "state_preserved": True}
        finally:
            learner.close()


if __name__ == "__main__":
    print(run())
