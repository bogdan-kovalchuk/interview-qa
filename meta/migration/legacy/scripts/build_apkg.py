#!/usr/bin/env python3
"""Build the production Anki package from accepted TSV cards.

The authoring collection is persistent build state. It preserves Anki-assigned
GUIDs so a learner can import a later package without losing card scheduling.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from anki.collection import Collection, DeckIdLimit, ExportAnkiPackageOptions
    from anki.notes import Note
except ImportError as error:  # pragma: no cover - exercised by CLI users without the extra
    raise SystemExit(
        "Anki build dependency is missing. Create .venv and install "
        "requirements/anki-build.txt."
    ) from error


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "authoring" / "manifest.json"
TEMPLATE_PATH = ROOT / "authoring" / "NOTE_TYPE_TEMPLATE.md"
CARDS_DIR = ROOT / "cards"
AUTHORING_COLLECTION = ROOT / "authoring" / "collection" / "Python Interview Questions.anki2"
RELEASE_PACKAGE = ROOT / "cards" / "Python Interview Questions.apkg"
IDENTITY_MANIFEST = ROOT / "tracking" / "apkg_note_identity.csv"
NOTE_TYPE_NAME = "Python Interview Basic"
TEMPLATE_NAME = "Card 1"


@dataclass(frozen=True)
class CardSource:
    card_id: str
    topic_id: str
    front: str
    back: str
    tags: tuple[str, ...]


def read_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_template(path: Path) -> tuple[str, str, str]:
    blocks = re.findall(r"```(?:html|css)\n(.*?)\n```", path.read_text(encoding="utf-8"), re.DOTALL)
    if len(blocks) != 3:
        raise ValueError(f"{path}: expected Front, Back, and Styling code blocks")
    return blocks[0], blocks[1], blocks[2]


def read_cards(cards_dir: Path, topics: list[dict[str, str]]) -> list[CardSource]:
    cards: list[CardSource] = []
    seen_ids: set[str] = set()
    for topic in topics:
        path = cards_dir / f"{topic['id']}_{topic['slug']}.txt"
        if not path.exists():
            raise ValueError(f"missing accepted card file: {path}")
        for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines()[5:], start=6):
            if not line.strip():
                continue
            if line.count("\t") != 2:
                raise ValueError(f"{path}:{line_number}: expected exactly two TAB characters")
            front, back, tag_field = line.split("\t")
            tags = tuple(tag_field.split())
            ids = [tag.removeprefix("card::") for tag in tags if tag.startswith("card::")]
            if len(ids) != 1 or not re.fullmatch(r"PYI_\d{2}_\d{3}", ids[0]):
                raise ValueError(f"{path}:{line_number}: expected one stable card::PYI_NN_NNN tag")
            card_id = ids[0]
            if card_id in seen_ids:
                raise ValueError(f"duplicate card ID in accepted cards: {card_id}")
            seen_ids.add(card_id)
            if not back.strip():
                raise ValueError(f"{path}:{line_number}: accepted card has an empty Back")
            cards.append(CardSource(card_id, topic["id"], front, back, tags))
    return cards


def ensure_note_type(collection: Collection, front_template: str, back_template: str, css: str) -> dict:
    model = collection.models.by_name(NOTE_TYPE_NAME)
    if model is None:
        model = collection.models.new(NOTE_TYPE_NAME)
        collection.models.add_field(model, collection.models.new_field("Front"))
        collection.models.add_field(model, collection.models.new_field("Back"))
        template = collection.models.new_template(TEMPLATE_NAME)
        template["qfmt"] = front_template
        template["afmt"] = back_template
        collection.models.add_template(model, template)
        model["css"] = css
        collection.models.add(model)
        return model

    fields = [field["name"] for field in model["flds"]]
    templates = model["tmpls"]
    if fields != ["Front", "Back"] or len(templates) != 1 or templates[0]["name"] != TEMPLATE_NAME:
        raise ValueError(
            f"{NOTE_TYPE_NAME} structure changed; package updates require an explicit migration"
        )
    changed = (
        model["css"] != css
        or templates[0]["qfmt"] != front_template
        or templates[0]["afmt"] != back_template
    )
    if changed:
        model["css"] = css
        templates[0]["qfmt"] = front_template
        templates[0]["afmt"] = back_template
        collection.models.update_dict(model)
    return collection.models.by_name(NOTE_TYPE_NAME)


def ensure_decks(collection: Collection, root_deck: str, topics: list[dict[str, str]]) -> dict[str, int]:
    collection.decks.id(root_deck)
    deck_ids: dict[str, int] = {}
    for topic in topics:
        deck_ids[topic["id"]] = collection.decks.id(f"{root_deck}::{topic['deck_name']}")
    return deck_ids


def note_ids_for_card_id(collection: Collection, card_id: str) -> list[int]:
    return list(collection.find_notes(f"tag:card::{card_id}"))


def reject_unplanned_authoring_notes(collection: Collection, root_deck: str, cards: list[CardSource]) -> None:
    expected_ids = {card.card_id for card in cards}
    actual_ids: set[str] = set()
    for note_id in collection.find_notes(f'deck:"{root_deck}"'):
        note = collection.get_note(note_id)
        ids = [tag.removeprefix("card::") for tag in note.tags if tag.startswith("card::")]
        if len(ids) != 1:
            raise ValueError(f"authoring note {note_id} must have exactly one card:: tag")
        if ids[0] in actual_ids:
            raise ValueError(f"authoring collection contains duplicate {ids[0]}")
        actual_ids.add(ids[0])
    retired = sorted(actual_ids - expected_ids)
    if retired:
        raise ValueError(
            "authoring collection contains retired card IDs; an explicit migration is required: "
            f"{', '.join(retired)}"
        )


def synchronize_cards(collection: Collection, model: dict, cards: list[CardSource], deck_ids: dict[str, int]) -> tuple[int, int]:
    added = updated = 0
    for card in cards:
        note_ids = note_ids_for_card_id(collection, card.card_id)
        if len(note_ids) > 1:
            raise ValueError(f"authoring collection contains duplicate {card.card_id}")
        if not note_ids:
            note = Note(collection, model)
            note["Front"] = card.front
            note["Back"] = card.back
            note.tags = list(card.tags)
            collection.add_note(note, deck_ids[card.topic_id])
            added += 1
            continue
        note = collection.get_note(note_ids[0])
        if note.note_type()["name"] != NOTE_TYPE_NAME:
            raise ValueError(f"{card.card_id}: authoring note has the wrong note type")
        if (
            note["Front"] != card.front
            or note["Back"] != card.back
            or set(note.tags) != set(card.tags)
        ):
            note["Front"] = card.front
            note["Back"] = card.back
            note.tags = list(card.tags)
            collection.update_note(note)
            updated += 1
    return added, updated


def write_identity_manifest(collection: Collection, cards: list[CardSource], path: Path) -> None:
    rows: list[tuple[str, str, str]] = []
    for card in sorted(cards, key=lambda item: item.card_id):
        note_ids = note_ids_for_card_id(collection, card.card_id)
        if len(note_ids) != 1:
            raise ValueError(f"{card.card_id}: expected one authoring note before export")
        note = collection.get_note(note_ids[0])
        rows.append((card.card_id, note.guid, str(note.id)))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["card_id", "anki_guid", "authoring_note_id"])
        writer.writerows(rows)


def build(
    manifest_path: Path = MANIFEST_PATH,
    template_path: Path = TEMPLATE_PATH,
    cards_dir: Path = CARDS_DIR,
    authoring_collection: Path = AUTHORING_COLLECTION,
    output_package: Path = RELEASE_PACKAGE,
    identity_manifest: Path = IDENTITY_MANIFEST,
) -> dict[str, int]:
    manifest = read_manifest(manifest_path)
    topics = manifest["topics"]
    root_deck = manifest["deck"]
    if not isinstance(topics, list) or not isinstance(root_deck, str):
        raise ValueError(f"{manifest_path}: invalid package manifest")
    cards = read_cards(cards_dir, topics)
    front_template, back_template, css = extract_template(template_path)
    authoring_collection.parent.mkdir(parents=True, exist_ok=True)
    output_package.parent.mkdir(parents=True, exist_ok=True)
    collection = Collection(str(authoring_collection))
    try:
        model = ensure_note_type(collection, front_template, back_template, css)
        deck_ids = ensure_decks(collection, root_deck, topics)
        added, updated = synchronize_cards(collection, model, cards, deck_ids)
        reject_unplanned_authoring_notes(collection, root_deck, cards)
        write_identity_manifest(collection, cards, identity_manifest)
        root_deck_id = collection.decks.id(root_deck)
        exported = collection.export_anki_package(
            out_path=str(output_package),
            options=ExportAnkiPackageOptions(
                with_scheduling=False,
                with_deck_configs=False,
                with_media=True,
                legacy=False,
            ),
            limit=DeckIdLimit(deck_id=root_deck_id),
        )
    finally:
        collection.close()
    if exported != len(cards):
        raise ValueError(f"exported {exported} notes, expected {len(cards)}")
    return {"cards": len(cards), "added": added, "updated": updated, "exported": exported}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST_PATH)
    parser.add_argument("--template", type=Path, default=TEMPLATE_PATH)
    parser.add_argument("--cards-dir", type=Path, default=CARDS_DIR)
    parser.add_argument("--authoring-collection", type=Path, default=AUTHORING_COLLECTION)
    parser.add_argument("--output", type=Path, default=RELEASE_PACKAGE)
    parser.add_argument("--identity-manifest", type=Path, default=IDENTITY_MANIFEST)
    args = parser.parse_args()
    try:
        result = build(
            manifest_path=args.manifest,
            template_path=args.template,
            cards_dir=args.cards_dir,
            authoring_collection=args.authoring_collection,
            output_package=args.output,
            identity_manifest=args.identity_manifest,
        )
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Built {exported} notes ({added} added, {updated} updated): {output}".format(
        **result, output=args.output
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
