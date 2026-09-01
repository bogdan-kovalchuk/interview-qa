"""Measure how Anki package import handles tags omitted by an update.

The harness creates its own collection and never accepts a user profile as input.
Run it once with a new, non-existent work directory. Detailed evidence is JSON.
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
import shutil
import sys
import time
from pathlib import Path
from typing import Any

import genanki
from anki.collection import Collection
from anki.import_export_pb2 import (
    ImportAnkiPackageOptions,
    ImportAnkiPackageRequest,
)
from google.protobuf.json_format import MessageToDict


MODEL_ID = 1600000000001
MODEL_NAME = "Interview QA Basic"
DECK_ID = 1600000000201
DECK_NAME = "Interview QA Spike::Tag Refresh"

FIELD_DEFINITIONS = [
    {"name": "Front", "ord": 0, "id": 1600000001001},
    {"name": "Back", "ord": 1, "id": 1600000001002},
    {"name": "Reference", "ord": 2, "id": 1600000001003},
    {"name": "Sources", "ord": 3, "id": 1600000001004},
    {"name": "QID", "ord": 4, "id": 1600000001005},
]
TEMPLATE_DEFINITIONS = [
    {
        "name": "Card 1",
        "ord": 0,
        "id": 1600000001101,
        "qfmt": "{{Front}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
    }
]

SEED_RECORDS = [
    {
        "qid": "x-tags-0001",
        "guid": "tagrefresh01",
        "tags": ["drop::b", "keep::a", "qid::x-tags-0001"],
        "kept_tag": "keep::a",
        "removed_tag": "drop::b",
        "added_tag": "add::c",
    },
    {
        "qid": "x-tags-0002",
        "guid": "tagrefresh02",
        "tags": ["keep::todo", "qid::x-tags-0002", "todo::short-answer"],
        "kept_tag": "keep::todo",
        "removed_tag": "todo::short-answer",
        "added_tag": "added::todo-cleared",
    },
    {
        "qid": "x-tags-0003",
        "guid": "tagrefresh03",
        "tags": ["keep::role", "qid::x-tags-0003", "role::python-backend"],
        "kept_tag": "keep::role",
        "removed_tag": "role::python-backend",
        "added_tag": "added::role-cleared",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--work-dir",
        type=Path,
        required=True,
        help="New, non-existent directory for disposable collections and packages.",
    )
    parser.add_argument("--output", type=Path, required=True, help="JSON evidence path.")
    return parser.parse_args()


def make_model() -> genanki.Model:
    return genanki.Model(
        model_id=MODEL_ID,
        name=MODEL_NAME,
        fields=FIELD_DEFINITIONS,
        templates=TEMPLATE_DEFINITIONS,
    )


def fields_for(record: dict[str, str], revision: str) -> list[str]:
    qid = record["qid"]
    return [
        f"Front {qid} {revision}",
        f"Back {qid} {revision}",
        f"https://example.invalid/uk/q/{qid}/",
        f"Controlled fixture {revision}",
        qid,
    ]


def package_records(revision: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for seed in SEED_RECORDS:
        tags = (
            list(seed["tags"])
            if revision == "seed"
            else [seed["kept_tag"], seed["added_tag"], f"qid::{seed['qid']}"]
        )
        records.append(
            {
                **seed,
                "fields": fields_for(seed, revision),
                "tags": sorted(tags),
            }
        )
    return records


def write_package(path: Path, records: list[dict[str, Any]], timestamp: int) -> None:
    model = make_model()
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for record in records:
        deck.add_note(
            genanki.Note(
                model=model,
                fields=record["fields"],
                tags=record["tags"],
                guid=record["guid"],
            )
        )
    genanki.Package(deck).write_to_file(str(path), timestamp=float(timestamp))


def options_dict(options: ImportAnkiPackageOptions) -> dict[str, Any]:
    return MessageToDict(
        options,
        preserving_proto_field_name=True,
        always_print_fields_with_no_presence=True,
    )


def import_package(
    col: Collection,
    package: Path,
    options: ImportAnkiPackageOptions,
) -> dict[str, Any]:
    request = ImportAnkiPackageRequest(package_path=str(package), options=options)
    response = col.import_anki_package(request)
    return MessageToDict(response, preserving_proto_field_name=True)


def note_id_for_guid(col: Collection, guid: str) -> int:
    note_id = col.db.scalar("select id from notes where guid = ?", guid)
    if not note_id:
        raise RuntimeError(f"fixture note disappeared: {guid}")
    return int(note_id)


def snapshot(col: Collection, records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for record in records:
        note_id = note_id_for_guid(col, record["guid"])
        note = col.get_note(note_id)
        result[record["qid"]] = {
            "note_id": note_id,
            "guid": note.guid,
            "fields": list(note.fields),
            "tags": sorted(note.tags),
            "mod": int(col.db.scalar("select mod from notes where id = ?", note_id)),
        }
    return result


def run_scenario(
    *,
    name: str,
    base_collection: Path,
    update_package: Path,
    update_records: list[dict[str, Any]],
    scenario_dir: Path,
    options_factory: Any,
) -> dict[str, Any]:
    scenario_dir.mkdir()
    collection_path = scenario_dir / "collection.anki2"
    shutil.copy2(base_collection, collection_path)
    col = Collection(str(collection_path))
    try:
        before = snapshot(col, update_records)
        options = options_factory(col)
        import_log = import_package(col, update_package, options)
        after = snapshot(col, update_records)
    finally:
        col.close()

    notes: dict[str, Any] = {}
    for record in update_records:
        qid = record["qid"]
        before_tags = before[qid]["tags"]
        after_tags = after[qid]["tags"]
        notes[qid] = {
            "guid": record["guid"],
            "tags_before": before_tags,
            "tags_in_package": record["tags"],
            "tags_after": after_tags,
            "kept_tag": record["kept_tag"],
            "removed_tag": record["removed_tag"],
            "added_tag": record["added_tag"],
            "omitted_tag_was_kept": record["removed_tag"] in after_tags,
            "added_tag_is_present": record["added_tag"] in after_tags,
            "fields_updated": after[qid]["fields"] == record["fields"],
            "note_id_unchanged": before[qid]["note_id"] == after[qid]["note_id"],
            "mod_before": before[qid]["mod"],
            "mod_after": after[qid]["mod"],
        }

    update_applied = all(note["fields_updated"] for note in notes.values())
    omitted_tags_kept = all(note["omitted_tag_was_kept"] for note in notes.values())
    added_tags_present = all(note["added_tag_is_present"] for note in notes.values())
    return {
        "name": name,
        "options": options_dict(options),
        "update_applied_to_all_notes": update_applied,
        "all_omitted_tags_kept": omitted_tags_kept,
        "all_omitted_tags_removed": all(
            not note["omitted_tag_was_kept"] for note in notes.values()
        ),
        "all_added_tags_present": added_tags_present,
        "answer": "kept" if omitted_tags_kept else "removed",
        "notes": notes,
        "import_log": import_log,
    }


def intended_options(_: Collection) -> ImportAnkiPackageOptions:
    return ImportAnkiPackageOptions(
        merge_notetypes=True,
        update_notes=1,
        update_notetypes=1,
        with_scheduling=False,
        with_deck_configs=False,
    )


def cloned_options(serialized: bytes) -> ImportAnkiPackageOptions:
    options = ImportAnkiPackageOptions()
    options.ParseFromString(serialized)
    return options


def run(args: argparse.Namespace) -> dict[str, Any]:
    args.work_dir.mkdir(parents=True, exist_ok=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    seed_records = package_records("seed")
    update_records = package_records("update")
    seed_timestamp = int(time.time()) + 100
    update_timestamp = seed_timestamp + 100
    seed_package = args.work_dir / "seed.apkg"
    update_package = args.work_dir / "update.apkg"
    write_package(seed_package, seed_records, seed_timestamp)
    write_package(update_package, update_records, update_timestamp)

    # Capture the package-import UI preset before any explicit import can persist
    # different choices in the collection configuration.
    # The captured preset serializes all flags as false. In the measured
    # desktop_default scenario Anki still updates fields on matching notes; keep
    # the observation separate from an unmeasured explanation of protobuf
    # defaults. Evidence: tag-refresh-evidence.json.
    preset_probe_dir = args.work_dir / "desktop-preset-probe"
    preset_probe_dir.mkdir()
    preset_probe_path = preset_probe_dir / "collection.anki2"
    preset_probe_col = Collection(str(preset_probe_path))
    try:
        pristine_desktop_preset = (
            preset_probe_col._backend.get_import_anki_package_presets()
        )
        pristine_desktop_preset_bytes = pristine_desktop_preset.SerializeToString()
    finally:
        preset_probe_col.close()

    base_dir = args.work_dir / "fixture-base"
    base_dir.mkdir()
    base_collection = base_dir / "collection.anki2"
    base_col = Collection(str(base_collection))
    try:
        seed_import_log = import_package(base_col, seed_package, intended_options(base_col))
        base_snapshot = snapshot(base_col, seed_records)
    finally:
        base_col.close()

    expected_seed_tags = {record["qid"]: record["tags"] for record in seed_records}
    actual_seed_tags = {qid: note["tags"] for qid, note in base_snapshot.items()}
    if actual_seed_tags != expected_seed_tags:
        raise RuntimeError(
            f"controlled fixture seed mismatch: {actual_seed_tags!r} != {expected_seed_tags!r}"
        )

    scenarios = {
        "intended": run_scenario(
            name="update_notes=always, merge_notetypes=true",
            base_collection=base_collection,
            update_package=update_package,
            update_records=update_records,
            scenario_dir=args.work_dir / "intended",
            options_factory=intended_options,
        ),
        "desktop_default": run_scenario(
            name="Anki Desktop package-import preset",
            base_collection=base_collection,
            update_package=update_package,
            update_records=update_records,
            scenario_dir=args.work_dir / "desktop-default",
            options_factory=lambda _: cloned_options(pristine_desktop_preset_bytes),
        ),
    }

    for scenario_name, scenario in scenarios.items():
        if not scenario["update_applied_to_all_notes"]:
            raise RuntimeError(f"{scenario_name} did not update every fixture note")

    evidence = {
        "environment": {
            "os": platform.platform(),
            "python": sys.version,
            "anki": importlib.metadata.version("anki"),
            "genanki": importlib.metadata.version("genanki"),
        },
        "fixture": {
            "model_id": MODEL_ID,
            "model_name": MODEL_NAME,
            "field_names": [field["name"] for field in FIELD_DEFINITIONS],
            "template_names": [template["name"] for template in TEMPLATE_DEFINITIONS],
            "note_count": len(seed_records),
            "seed_timestamp": seed_timestamp,
            "update_timestamp": update_timestamp,
            "seed_import_log": seed_import_log,
            "seed_notes": base_snapshot,
        },
        "scenarios": scenarios,
        "todo_case": {
            name: {
                "tag": "todo::short-answer",
                "present_before": "todo::short-answer"
                in scenario["notes"]["x-tags-0002"]["tags_before"],
                "present_in_package": "todo::short-answer"
                in scenario["notes"]["x-tags-0002"]["tags_in_package"],
                "present_after": "todo::short-answer"
                in scenario["notes"]["x-tags-0002"]["tags_after"],
                "disappears_on_its_own": "todo::short-answer"
                not in scenario["notes"]["x-tags-0002"]["tags_after"],
            }
            for name, scenario in scenarios.items()
        },
    }
    args.output.write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return evidence


def main() -> int:
    args = parse_args()
    evidence = run(args)
    summary = {
        name: {
            "answer": scenario["answer"],
            "todo_disappears": evidence["todo_case"][name]["disappears_on_its_own"],
        }
        for name, scenario in evidence["scenarios"].items()
    }
    print(json.dumps(summary, ensure_ascii=False))
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
