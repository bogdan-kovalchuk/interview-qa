#!/usr/bin/env python3
"""Import the production package into a disposable collection and validate it."""

from __future__ import annotations

import argparse
import csv
import json
import tempfile
from pathlib import Path

from anki.collection import Collection, ImportAnkiPackageOptions, ImportAnkiPackageRequest


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MANIFEST = ROOT / "authoring" / "manifest.json"
DEFAULT_PACKAGE = ROOT / "cards" / "Python Interview Questions.apkg"
DEFAULT_IDENTITIES = ROOT / "tracking" / "apkg_note_identity.csv"


def verify(package: Path, manifest_path: Path, identities_path: Path) -> dict[str, int]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    root_deck = manifest["deck"]
    topics = manifest["topics"]
    with identities_path.open(encoding="utf-8", newline="") as handle:
        identities = list(csv.DictReader(handle))
    if len(identities) != len({row["card_id"] for row in identities}):
        raise ValueError("identity manifest contains duplicate card IDs")
    with tempfile.TemporaryDirectory() as temporary_dir:
        learner = Collection(str(Path(temporary_dir) / "learner.anki2"))
        try:
            learner.import_anki_package(
                ImportAnkiPackageRequest(
                    package_path=str(package),
                    options=ImportAnkiPackageOptions(
                        with_scheduling=False,
                        with_deck_configs=False,
                    ),
                )
            )
            actual_children = {
                item.name for item in learner.decks.all_names_and_ids()
                if item.name.startswith(f"{root_deck}::")
            }
            expected_children = {
                f"{root_deck}::{topic['deck_name']}" for topic in topics
            }
            if actual_children != expected_children:
                raise ValueError(
                    f"package child decks differ: missing={sorted(expected_children - actual_children)}, "
                    f"extra={sorted(actual_children - expected_children)}"
                )
            note_ids = learner.find_notes(f'deck:"{root_deck}"')
            card_ids = learner.find_cards(f'deck:"{root_deck}"')
            if len(note_ids) != len(identities) or len(card_ids) != len(identities):
                raise ValueError(
                    f"package contains {len(note_ids)} notes and {len(card_ids)} cards; "
                    f"expected {len(identities)}"
                )
            if any(learner.get_card(card_id).reps or learner.get_card(card_id).lapses for card_id in card_ids):
                raise ValueError("package imported author scheduling data")
            for row in identities:
                note_ids_for_card = learner.find_notes(f"tag:card::{row['card_id']}")
                if len(note_ids_for_card) != 1:
                    raise ValueError(f"package cannot locate exactly one {row['card_id']}")
                if learner.get_note(note_ids_for_card[0]).guid != row["anki_guid"]:
                    raise ValueError(f"package GUID drift for {row['card_id']}")
        finally:
            learner.close()
    return {"notes": len(identities), "cards": len(identities), "subdecks": len(topics)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--identities", type=Path, default=DEFAULT_IDENTITIES)
    args = parser.parse_args()
    result = verify(args.package, args.manifest, args.identities)
    print("Verified {notes} notes, {cards} cards, and {subdecks} subdecks.".format(**result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
