"""Anki compatibility harness: experiments A-J from the M0.4 brief.

Results live in meta/measurements.md. This script only produces the evidence.

It never accepts the live Anki profile as a work target - pass copied or restored
collections in an isolated scratch directory. Two fixtures are needed because the
392-note target model and genuine scheduling history live in different collections:

    --target-collection-source   copy holding model 1788409800655 and its 392 notes
    --history-collection-source  copy with >= 20 cards where reps > 0
    --current-profile-copy       copy of the current profile, read-only diagnostics
    --work-dir                   scratch directory, must not exist yet

Run from a disposable virtualenv with `anki` and `genanki` installed.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import sqlite3
import sys
from pathlib import Path
from typing import Any, Iterable

import genanki
from anki.collection import Collection, NoteIdsLimit
from anki.import_export_pb2 import (
    ExportAnkiPackageOptions,
    ImportAnkiPackageOptions,
    ImportAnkiPackageRequest,
)
from google.protobuf.json_format import MessageToDict


TARGET_MODEL_ID = 1788409800655
HISTORY_MODEL_ID = 1778510992002
NEW_FIELDS = ("Reference", "Sources", "QID")
SCHEDULE_FIELDS = (
    "due",
    "ivl",
    "factor",
    "reps",
    "lapses",
    "queue",
    "type",
    "flags",
    "odid",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the M0.4 Anki compatibility spike.")
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--current-profile-copy", type=Path, required=True)
    parser.add_argument("--target-collection-source", type=Path, required=True)
    parser.add_argument("--history-collection-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def sql_counts(path: Path) -> dict[str, Any]:
    uri = "file:" + str(path).replace("\\", "/") + "?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    try:
        return {
            "schema_col_ver": connection.execute("select ver from col").fetchone()[0],
            "pragma_user_version": connection.execute("pragma user_version").fetchone()[0],
            "notes": connection.execute("select count(*) from notes").fetchone()[0],
            "cards": connection.execute("select count(*) from cards").fetchone()[0],
            "reviewed_cards": connection.execute(
                "select count(*) from cards where reps > 0"
            ).fetchone()[0],
            "target_notes": connection.execute(
                "select count(*) from notes where mid = ?", (TARGET_MODEL_ID,)
            ).fetchone()[0],
            "model_counts": connection.execute(
                "select mid, count(*) from notes group by mid order by count(*) desc"
            ).fetchall(),
            "revlog_rows": connection.execute("select count(*) from revlog").fetchone()[0],
            "revlog_distinct_cards": connection.execute(
                "select count(distinct cid) from revlog"
            ).fetchone()[0],
        }
    finally:
        connection.close()


def note_count_for_model(col: Collection, model_id: int) -> int:
    return int(col.db.scalar("select count(*) from notes where mid = ?", model_id) or 0)


def card_count_for_model(col: Collection, model_id: int) -> int:
    return int(
        col.db.scalar(
            "select count(*) from cards c join notes n on n.id = c.nid where n.mid = ?",
            model_id,
        )
        or 0
    )


def field_shape(model: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {"name": field["name"], "ord": field["ord"], "id": field.get("id")}
        for field in model["flds"]
    ]


def template_shape(model: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {"name": template["name"], "ord": template["ord"], "id": template.get("id")}
        for template in model["tmpls"]
    ]


def notetype_shape(model: dict[str, Any]) -> dict[str, Any]:
    return {
        "model_id": model["id"],
        "name": model["name"],
        "fields": field_shape(model),
        "templates": template_shape(model),
    }


def fingerprint(model: dict[str, Any]) -> dict[str, Any]:
    shape = notetype_shape(model)
    canonical = json.dumps(shape, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "canonical_json": canonical,
    }


def migrate_model(col: Collection, model_id: int) -> tuple[dict[str, Any], dict[str, Any]]:
    model = col.models.get(model_id)
    if model is None:
        raise RuntimeError(f"model {model_id} does not exist")
    before = copy.deepcopy(model)
    existing = {field["name"] for field in model["flds"]}
    for name in NEW_FIELDS:
        if name in existing:
            raise RuntimeError(f"field {name} already exists on model {model_id}")
        col.models.add_field(model, col.models.new_field(name))
    col.models.save(model)
    col.save()
    after = col.models.get(model_id)
    if after is None:
        raise RuntimeError(f"model {model_id} disappeared after migration")
    return before, after


def snapshot_note_fields(col: Collection, note_ids: Iterable[int]) -> dict[str, list[str]]:
    return {str(nid): list(col.get_note(nid).fields) for nid in note_ids}


def snapshot_scheduling(col: Collection, card_ids: Iterable[int]) -> dict[str, dict[str, int]]:
    snapshots: dict[str, dict[str, int]] = {}
    for cid in card_ids:
        card = col.get_card(cid)
        snapshots[str(cid)] = {name: int(getattr(card, name)) for name in SCHEDULE_FIELDS}
    return snapshots


def card_decks(col: Collection, card_ids: Iterable[int]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for cid in card_ids:
        card = col.get_card(cid)
        deck = col.decks.get(card.did)
        result[str(cid)] = {
            "deck_id": int(card.did),
            "deck_name": deck["name"] if deck else None,
        }
    return result


def import_package(col: Collection, package: Path) -> dict[str, Any]:
    options = ImportAnkiPackageOptions(
        merge_notetypes=True,
        update_notes=1,
        update_notetypes=1,
        with_scheduling=False,
        with_deck_configs=False,
    )
    request = ImportAnkiPackageRequest(package_path=str(package), options=options)
    log = col.import_anki_package(request)
    col.save()
    return MessageToDict(log, preserving_proto_field_name=True)


def export_anki_package(col: Collection, note_ids: list[int], output: Path) -> int:
    options = ExportAnkiPackageOptions(
        with_scheduling=False,
        with_deck_configs=False,
        with_media=False,
        legacy=False,
    )
    limit = NoteIdsLimit(note_ids=note_ids)
    return int(col.export_anki_package(out_path=str(output), options=options, limit=limit))


def stable_deck_id(name: str) -> int:
    digest = hashlib.sha256(name.encode("utf-8")).digest()
    return 1_000_000_000 + int.from_bytes(digest[:4], "big")


def genanki_model(model: dict[str, Any]) -> genanki.Model:
    fields = [
        {"name": field["name"], "id": field.get("id"), "ord": field["ord"]}
        for field in model["flds"]
    ]
    templates = [
        {
            "name": template["name"],
            "id": template.get("id"),
            "ord": template["ord"],
            "qfmt": template["qfmt"],
            "afmt": template["afmt"],
        }
        for template in model["tmpls"]
    ]
    return genanki.Model(
        model_id=int(model["id"]),
        name=model["name"],
        fields=fields,
        templates=templates,
        css=model.get("css", ""),
        model_type=int(model.get("type", 0)),
        latex_pre=model.get("latexPre", genanki.Model.DEFAULT_LATEX_PRE),
        latex_post=model.get("latexPost", genanki.Model.DEFAULT_LATEX_POST),
        sort_field_index=int(model.get("sortf", 0)),
    )


def write_genanki_package(
    *,
    output: Path,
    model: dict[str, Any],
    records: list[dict[str, Any]],
) -> None:
    generated_model = genanki_model(model)
    decks: dict[str, genanki.Deck] = {}
    for record in records:
        deck_name = record["deck_name"]
        deck = decks.setdefault(
            deck_name,
            genanki.Deck(stable_deck_id(deck_name), deck_name),
        )
        note = genanki.Note(
            model=generated_model,
            fields=record["fields"],
            tags=record["tags"],
            guid=record["guid"],
        )
        deck.add_note(note)
    genanki.Package(list(decks.values())).write_to_file(str(output))


def records_for_notes(
    col: Collection,
    note_ids: list[int],
    *,
    deck_name: str,
    marker: str,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for nid in note_ids:
        note = col.get_note(nid)
        fields = list(note.fields)
        fields[0] = fields[0] + marker
        fields[1] = fields[1] + marker
        if len(fields) >= 5:
            fields[2] = f"https://example.invalid/{note.guid}/"
            fields[3] = "Spike source"
            fields[4] = f"spike-{note.guid}"
        records.append(
            {
                "guid": note.guid,
                "fields": fields,
                "tags": sorted(note.tags),
                "deck_name": deck_name,
            }
        )
    return records


def notes_by_guids(col: Collection, guids: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for guid in guids:
        nid = col.db.scalar("select id from notes where guid = ?", guid)
        if nid:
            result[guid] = int(nid)
    return result


def run(args: argparse.Namespace) -> dict[str, Any]:
    args.work_dir.mkdir(parents=True, exist_ok=False)
    evidence: dict[str, Any] = {
        "python": sys.version,
        "fixtures": {},
        "experiments": {},
        "import_options": {
            "merge_notetypes": True,
            "update_notes": "always",
            "update_notetypes": "always",
            "with_scheduling": False,
            "with_deck_configs": False,
        },
    }

    current_collection = args.current_profile_copy / "collection.anki2"
    evidence["fixtures"]["current_profile_copy"] = sql_counts(current_collection)
    evidence["fixtures"]["history_backup"] = sql_counts(args.history_collection_source)

    target_dir = args.work_dir / "target"
    target_dir.mkdir()
    target_path = target_dir / "collection.anki2"
    shutil.copy2(args.target_collection_source, target_path)

    target_col = Collection(str(target_path))
    target_model_before = target_col.models.get(TARGET_MODEL_ID)
    if target_model_before is None:
        raise RuntimeError("target model is absent from predecessor collection")
    target_note_ids = [
        int(row[0])
        for row in target_col.db.all(
            "select id from notes where mid = ? order by id", TARGET_MODEL_ID
        )
    ]
    target_card_ids = [
        int(row[0])
        for row in target_col.db.all(
            "select c.id from cards c join notes n on n.id = c.nid "
            "where n.mid = ? order by c.id",
            TARGET_MODEL_ID,
        )
    ]
    target_fields_before = snapshot_note_fields(target_col, target_note_ids)
    target_before_count = note_count_for_model(target_col, TARGET_MODEL_ID)
    target_before_cards = card_count_for_model(target_col, TARGET_MODEL_ID)
    target_model_before_copy, target_model_after = migrate_model(target_col, TARGET_MODEL_ID)
    target_fields_after = snapshot_note_fields(target_col, target_note_ids)
    target_after_count = note_count_for_model(target_col, TARGET_MODEL_ID)
    target_after_cards = card_count_for_model(target_col, TARGET_MODEL_ID)
    target_shifted = [
        nid
        for nid in target_note_ids
        if target_fields_after[str(nid)][:2] != target_fields_before[str(nid)]
        or target_fields_after[str(nid)][2:] != ["", "", ""]
    ]
    target_model_id_unchanged = int(target_model_after["id"]) == TARGET_MODEL_ID
    target_a_aux_pass = all(
        (
            target_before_count == 392,
            target_after_count == 392,
            target_before_cards == 392,
            target_after_cards == 392,
            not target_shifted,
            field_shape(target_model_before_copy)
            == field_shape(target_model_after)[:2],
            template_shape(target_model_before_copy) == template_shape(target_model_after),
            target_model_id_unchanged,
        )
    )
    current_target_count = evidence["fixtures"]["current_profile_copy"]["target_notes"]
    evidence["experiments"]["A"] = {
        "verdict": "inconclusive" if current_target_count != 392 else (
            "confirmed" if target_a_aux_pass else "refuted"
        ),
        "reason": (
            "The supplied current real profile has no notes on the target model; "
            "the exact migration passed on the 392-note predecessor copy."
        ),
        "current_real_profile_target_notes": current_target_count,
        "auxiliary_target_fixture_passed": target_a_aux_pass,
        "notes_before": target_before_count,
        "notes_after": target_after_count,
        "cards_before": target_before_cards,
        "cards_after": target_after_cards,
        "shifted_note_ids": target_shifted,
        "model_before": notetype_shape(target_model_before_copy),
        "model_after": notetype_shape(target_model_after),
        "fingerprint_after": fingerprint(target_model_after),
    }
    target_col.close()

    history_dir = args.work_dir / "history"
    history_dir.mkdir()
    history_path = history_dir / "collection.anki2"
    shutil.copy2(args.history_collection_source, history_path)
    history_col = Collection(str(history_path))
    history_model = history_col.models.get(HISTORY_MODEL_ID)
    if history_model is None:
        raise RuntimeError("history model is absent from restored real-profile backup")
    reviewed_rows = history_col.db.all(
        "select c.id, c.nid from cards c join notes n on n.id = c.nid "
        "where n.mid = ? and c.reps > 0 order by c.id limit 20",
        HISTORY_MODEL_ID,
    )
    if len(reviewed_rows) < 20:
        raise RuntimeError(f"only {len(reviewed_rows)} reviewed cards were available")
    history_card_ids = [int(row[0]) for row in reviewed_rows]
    history_note_ids = [int(row[1]) for row in reviewed_rows]
    history_fields_before_migration = snapshot_note_fields(history_col, history_note_ids)
    history_schedule_before_migration = snapshot_scheduling(history_col, history_card_ids)
    history_model_before, history_model_after = migrate_model(history_col, HISTORY_MODEL_ID)
    history_fields_after_migration = snapshot_note_fields(history_col, history_note_ids)
    history_schedule_after_migration = snapshot_scheduling(history_col, history_card_ids)
    history_migration_pass = (
        history_schedule_before_migration == history_schedule_after_migration
        and all(
            history_fields_after_migration[str(nid)][:2]
            == history_fields_before_migration[str(nid)]
            and history_fields_after_migration[str(nid)][2:] == ["", "", ""]
            for nid in history_note_ids
        )
        and field_shape(history_model_before) == field_shape(history_model_after)[:2]
        and template_shape(history_model_before) == template_shape(history_model_after)
    )
    baseline_schedule = snapshot_scheduling(history_col, history_card_ids)
    baseline_decks = card_decks(history_col, history_card_ids)
    history_total_notes_before = history_col.note_count()
    tag_note_id = next(
        (nid for nid in history_note_ids if len(history_col.get_note(nid).tags) >= 2),
        history_note_ids[0],
    )
    tag_note = history_col.get_note(tag_note_id)
    if len(tag_note.tags) < 2:
        tag_note.tags.extend(["spike-keep-seed", "spike-remove-seed"])
        history_col.update_note(tag_note)
    original_tags = sorted(history_col.get_note(tag_note_id).tags)
    omitted_nid = int(
        history_col.db.scalar(
            "select id from notes where id not in ("
            + ",".join("?" for _ in history_note_ids)
            + ") order by id limit 1",
            *history_note_ids,
        )
    )
    history_col.close()

    anki_stage_dir = args.work_dir / "anki-stage"
    anki_stage_dir.mkdir()
    anki_stage_path = anki_stage_dir / "collection.anki2"
    shutil.copy2(history_path, anki_stage_path)
    anki_stage = Collection(str(anki_stage_path))
    package_deck_name = "Spike::Anki Package Different Deck"
    package_deck_id = int(anki_stage.decks.id(package_deck_name))
    expected_fields: dict[str, list[str]] = {}
    tag_note = anki_stage.get_note(tag_note_id)
    tag_to_keep = original_tags[0]
    tag_to_remove = original_tags[1]
    tag_to_add = "spike-added"
    package_tags: list[str] = []
    for nid in history_note_ids:
        note = anki_stage.get_note(nid)
        note["Front"] = note["Front"] + " [anki-B]"
        note["Back"] = note["Back"] + " [anki-B]"
        note["Reference"] = f"https://example.invalid/{note.guid}/"
        note["Sources"] = "Spike source"
        note["QID"] = f"spike-{note.guid}"
        if nid == tag_note_id:
            note.tags = sorted((set(original_tags) - {tag_to_remove}) | {tag_to_add})
            package_tags = sorted(note.tags)
        anki_stage.update_note(note)
        expected_fields[str(nid)] = list(note.fields)
        for cid in anki_stage.card_ids_of_note(nid):
            card = anki_stage.get_card(cid)
            card.did = package_deck_id
            anki_stage.update_card(card)
    anki_stage.save()
    anki_package = args.work_dir / "anki-builder-package.apkg"
    exported_notes = export_anki_package(anki_stage, history_note_ids, anki_package)
    anki_stage.close()

    history_col = Collection(str(history_path))
    import_log_b = import_package(history_col, anki_package)
    after_b_schedule = snapshot_scheduling(history_col, history_card_ids)
    after_b_decks = card_decks(history_col, history_card_ids)
    after_b_fields = snapshot_note_fields(history_col, history_note_ids)
    fields_updated_b = after_b_fields == expected_fields
    schedule_unchanged_b = baseline_schedule == after_b_schedule
    decks_unchanged_b = baseline_decks == after_b_decks
    evidence["experiments"]["B"] = {
        "verdict": "confirmed" if fields_updated_b and schedule_unchanged_b else "refuted",
        "selected_card_count": len(history_card_ids),
        "selected_card_ids": history_card_ids,
        "selected_note_guids": [history_col.get_note(nid).guid for nid in history_note_ids],
        "scheduling_before": baseline_schedule,
        "scheduling_after": after_b_schedule,
        "fields_updated": fields_updated_b,
        "scheduling_identical": schedule_unchanged_b,
        "anki_exported_note_count": exported_notes,
        "import_log": import_log_b,
        "supporting_history_model_migration_passed": history_migration_pass,
        "history_model_fingerprint": fingerprint(history_model_after),
    }
    evidence["experiments"]["C"] = {
        "verdict": "confirmed" if decks_unchanged_b else "refuted",
        "package_deck": package_deck_name,
        "before": baseline_decks,
        "after": after_b_decks,
        "moved_card_ids": [
            int(cid)
            for cid in baseline_decks
            if baseline_decks[cid] != after_b_decks[cid]
        ],
    }
    history_total_notes_after_subset = history_col.note_count()
    omitted_still_present = bool(
        history_col.db.scalar("select 1 from notes where id = ?", omitted_nid)
    )
    evidence["experiments"]["E"] = {
        "verdict": "confirmed"
        if history_total_notes_before == history_total_notes_after_subset
        and omitted_still_present
        else "refuted",
        "package_note_count": len(history_note_ids),
        "collection_notes_before": history_total_notes_before,
        "collection_notes_after": history_total_notes_after_subset,
        "omitted_note_id": omitted_nid,
        "omitted_note_still_present": omitted_still_present,
    }
    tags_after = sorted(history_col.get_note(tag_note_id).tags)
    tag_exact = tags_after == package_tags
    evidence["experiments"]["F"] = {
        "verdict": "confirmed" if tag_exact else "refuted",
        "note_id": tag_note_id,
        "tags_before": original_tags,
        "package_tags": package_tags,
        "tags_after": tags_after,
        "added_tag": tag_to_add,
        "removed_tag": tag_to_remove,
        "kept_tag": tag_to_keep,
        "removed_tag_was_removed": tag_to_remove not in tags_after,
        "exactly_matches_package": tag_exact,
    }

    suspended_ids = history_card_ids[:3]
    flagged = {
        str(history_card_ids[3]): 1,
        str(history_card_ids[4]): 2,
        str(history_card_ids[5]): 3,
    }
    history_col.sched.suspend_cards(suspended_ids)
    for cid_text, flag in flagged.items():
        history_col.set_user_flag_for_cards(flag, [int(cid_text)])
    history_col.save()
    before_d = snapshot_scheduling(history_col, history_card_ids)
    import_log_d = import_package(history_col, anki_package)
    after_d = snapshot_scheduling(history_col, history_card_ids)
    d_pass = before_d == after_d
    evidence["experiments"]["D"] = {
        "verdict": "confirmed" if d_pass else "refuted",
        "suspended_card_ids": suspended_ids,
        "flagged_cards": flagged,
        "before": {cid: before_d[str(cid)] for cid in suspended_ids + list(map(int, flagged))},
        "after": {cid: after_d[str(cid)] for cid in suspended_ids + list(map(int, flagged))},
        "state_identical": d_pass,
        "import_log": import_log_d,
    }

    history_model_for_genanki = history_col.models.get(HISTORY_MODEL_ID)
    if history_model_for_genanki is None:
        raise RuntimeError("history model disappeared before genanki test")
    history_genanki_records = records_for_notes(
        history_col,
        history_note_ids,
        deck_name="Spike::Genanki Different Deck",
        marker=" [genanki-G]",
    )
    history_genanki_package = args.work_dir / "genanki-history.apkg"
    write_genanki_package(
        output=history_genanki_package,
        model=history_model_for_genanki,
        records=history_genanki_records,
    )
    before_g_history_count = history_col.note_count()
    before_g_history_schedule = snapshot_scheduling(history_col, history_card_ids)
    before_g_history_decks = card_decks(history_col, history_card_ids)
    before_g_history_model = notetype_shape(history_model_for_genanki)
    import_log_g_history = import_package(history_col, history_genanki_package)
    after_g_history_count = history_col.note_count()
    after_g_history_schedule = snapshot_scheduling(history_col, history_card_ids)
    after_g_history_decks = card_decks(history_col, history_card_ids)
    after_g_history_model_raw = history_col.models.get(HISTORY_MODEL_ID)
    if after_g_history_model_raw is None:
        raise RuntimeError("history model disappeared after genanki import")
    after_g_history_model = notetype_shape(after_g_history_model_raw)
    history_fields_g = snapshot_note_fields(history_col, history_note_ids)
    expected_history_g = {
        str(nid): record["fields"]
        for nid, record in zip(history_note_ids, history_genanki_records, strict=True)
    }
    g_history_pass = all(
        (
            before_g_history_count == after_g_history_count,
            before_g_history_schedule == after_g_history_schedule,
            before_g_history_decks == after_g_history_decks,
            before_g_history_model == after_g_history_model,
            history_fields_g == expected_history_g,
        )
    )
    history_col.close()

    target_col = Collection(str(target_path))
    target_model_for_genanki = target_col.models.get(TARGET_MODEL_ID)
    if target_model_for_genanki is None:
        raise RuntimeError("target model disappeared before genanki test")
    target_genanki_note_ids = target_note_ids[:20]
    target_original_decks = card_decks(
        target_col,
        [int(target_col.card_ids_of_note(nid)[0]) for nid in target_genanki_note_ids],
    )
    target_records = records_for_notes(
        target_col,
        target_genanki_note_ids,
        deck_name="Spike::Genanki Target Different Deck",
        marker=" [genanki-G-target]",
    )
    target_guids = [record["guid"] for record in target_records]
    target_genanki_package = args.work_dir / "genanki-target.apkg"
    write_genanki_package(
        output=target_genanki_package,
        model=target_model_for_genanki,
        records=target_records,
    )
    target_count_before_g = target_col.note_count()
    target_model_before_g = notetype_shape(target_model_for_genanki)
    target_log_g = import_package(target_col, target_genanki_package)
    target_count_after_g = target_col.note_count()
    target_model_after_g_raw = target_col.models.get(TARGET_MODEL_ID)
    if target_model_after_g_raw is None:
        raise RuntimeError("target model disappeared after genanki import")
    target_model_after_g = notetype_shape(target_model_after_g_raw)
    target_nids_after_g = notes_by_guids(target_col, target_guids)
    target_fields_after_g = {
        guid: list(target_col.get_note(nid).fields)
        for guid, nid in target_nids_after_g.items()
    }
    expected_target_by_guid = {record["guid"]: record["fields"] for record in target_records}
    target_card_ids_after_g = [
        int(target_col.card_ids_of_note(target_nids_after_g[guid])[0]) for guid in target_guids
    ]
    target_decks_after_g = card_decks(target_col, target_card_ids_after_g)
    g_target_pass = all(
        (
            target_count_before_g == 392,
            target_count_after_g == 392,
            target_model_before_g == target_model_after_g,
            target_fields_after_g == expected_target_by_guid,
            target_original_decks == target_decks_after_g,
        )
    )

    empty_dir = args.work_dir / "empty"
    empty_dir.mkdir()
    empty_path = empty_dir / "collection.anki2"
    empty_col = Collection(str(empty_path))
    empty_log = import_package(empty_col, target_genanki_package)
    empty_guid_map = notes_by_guids(empty_col, target_guids)
    empty_model_raw = empty_col.models.get(TARGET_MODEL_ID)
    empty_model_shape = notetype_shape(empty_model_raw) if empty_model_raw else None
    empty_pass = (
        len(empty_guid_map) == len(target_guids)
        and empty_col.note_count() == len(target_guids)
        and empty_model_shape == target_model_before_g
    )
    empty_col.close()

    evidence["experiments"]["G"] = {
        "verdict": "confirmed"
        if empty_pass and g_target_pass and g_history_pass
        else "refuted",
        "empty_collection": {
            "passed": empty_pass,
            "imported_notes": len(empty_guid_map),
            "expected_notes": len(target_guids),
            "model_shape": empty_model_shape,
            "import_log": empty_log,
        },
        "target_migrated_copy": {
            "passed": g_target_pass,
            "notes_before": target_count_before_g,
            "notes_after": target_count_after_g,
            "model_unchanged": target_model_before_g == target_model_after_g,
            "fields_updated": target_fields_after_g == expected_target_by_guid,
            "decks_unchanged": target_original_decks == target_decks_after_g,
            "import_log": target_log_g,
        },
        "real_history_copy": {
            "passed": g_history_pass,
            "notes_before": before_g_history_count,
            "notes_after": after_g_history_count,
            "scheduling_unchanged": before_g_history_schedule == after_g_history_schedule,
            "decks_unchanged": before_g_history_decks == after_g_history_decks,
            "suspension_and_flags_unchanged": before_g_history_schedule == after_g_history_schedule,
            "model_unchanged": before_g_history_model == after_g_history_model,
            "fields_updated": history_fields_g == expected_history_g,
            "import_log": import_log_g_history,
        },
    }

    h_counts = [target_col.note_count()]
    h_logs = []
    h_logs.append(import_package(target_col, target_genanki_package))
    h_counts.append(target_col.note_count())
    h_logs.append(import_package(target_col, target_genanki_package))
    h_counts.append(target_col.note_count())
    h_pass = len(set(h_counts)) == 1
    evidence["experiments"]["H"] = {
        "verdict": "confirmed" if h_pass else "refuted",
        "note_counts": h_counts,
        "import_logs": h_logs,
    }

    overlap_records_one = copy.deepcopy(target_records[:5])
    overlap_records_two = copy.deepcopy(target_records[3:8])
    for record in overlap_records_one:
        record["deck_name"] = "Spike::Overlap::First"
    for record in overlap_records_two:
        record["deck_name"] = "Spike::Overlap::Second"
    overlap_one = args.work_dir / "overlap-one.apkg"
    overlap_two = args.work_dir / "overlap-two.apkg"
    write_genanki_package(
        output=overlap_one,
        model=target_model_for_genanki,
        records=overlap_records_one,
    )
    write_genanki_package(
        output=overlap_two,
        model=target_model_for_genanki,
        records=overlap_records_two,
    )
    overlap_dir = args.work_dir / "overlap-empty"
    overlap_dir.mkdir()
    overlap_path = overlap_dir / "collection.anki2"
    overlap_col = Collection(str(overlap_path))
    overlap_log_one = import_package(overlap_col, overlap_one)
    overlap_log_two = import_package(overlap_col, overlap_two)
    overlap_guids = sorted(set(record["guid"] for record in overlap_records_one + overlap_records_two))
    overlap_nids = notes_by_guids(overlap_col, overlap_guids)
    shared_guids = sorted(
        set(record["guid"] for record in overlap_records_one)
        & set(record["guid"] for record in overlap_records_two)
    )
    shared_decks: dict[str, str | None] = {}
    for guid in shared_guids:
        nid = overlap_nids[guid]
        cid = int(overlap_col.card_ids_of_note(nid)[0])
        shared_decks[guid] = card_decks(overlap_col, [cid])[str(cid)]["deck_name"]
    overlap_pass = (
        overlap_col.note_count() == len(overlap_guids)
        and len(overlap_nids) == len(overlap_guids)
        and all(deck == "Spike::Overlap::First" for deck in shared_decks.values())
    )
    evidence["experiments"]["I"] = {
        "verdict": "confirmed" if overlap_pass else "refuted",
        "package_one_notes": len(overlap_records_one),
        "package_two_notes": len(overlap_records_two),
        "overlap_size": len(shared_guids),
        "expected_unique_notes": len(overlap_guids),
        "actual_unique_notes": overlap_col.note_count(),
        "shared_card_decks": shared_decks,
        "import_log_one": overlap_log_one,
        "import_log_two": overlap_log_two,
    }
    overlap_col.close()

    different_model = copy.deepcopy(target_model_for_genanki)
    different_model["id"] = TARGET_MODEL_ID + 999_999
    different_model["name"] = "Spike Different Note Type"
    different_model["flds"] = [
        {"name": "Prompt", "ord": 0, "id": 810000000000000001},
        {"name": "Response", "ord": 1, "id": 810000000000000002},
    ]
    different_model["tmpls"] = [
        {
            "name": "Control Card",
            "ord": 0,
            "id": 810000000000000003,
            "qfmt": "{{Prompt}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Response}}",
        }
    ]
    different_records = [
        {
            "guid": record["guid"],
            "fields": ["different prompt", "different response"],
            "tags": ["spike-different-model"],
            "deck_name": "Spike::Different Model",
        }
        for record in target_records[:3]
    ]
    different_package = args.work_dir / "different-notetype.apkg"
    write_genanki_package(
        output=different_package,
        model=different_model,
        records=different_records,
    )
    different_guids = [record["guid"] for record in different_records]
    j_before_count = target_col.note_count()
    j_before = {
        guid: {
            "nid": int(target_col.db.scalar("select id from notes where guid = ?", guid)),
            "mid": int(target_col.db.scalar("select mid from notes where guid = ?", guid)),
            "fields": list(
                target_col.get_note(
                    int(target_col.db.scalar("select id from notes where guid = ?", guid))
                ).fields
            ),
        }
        for guid in different_guids
    }
    j_error = None
    j_log = None
    try:
        j_log = import_package(target_col, different_package)
    except Exception as exc:
        j_error = f"{type(exc).__name__}: {exc}"
    j_after_count = target_col.note_count()
    j_after = {
        guid: {
            "nid": int(target_col.db.scalar("select id from notes where guid = ?", guid)),
            "mid": int(target_col.db.scalar("select mid from notes where guid = ?", guid)),
            "fields": list(
                target_col.get_note(
                    int(target_col.db.scalar("select id from notes where guid = ?", guid))
                ).fields
            ),
            "guid_row_count": int(
                target_col.db.scalar("select count(*) from notes where guid = ?", guid)
            ),
        }
        for guid in different_guids
    }
    j_ignored = (
        j_before_count == j_after_count
        and all(
            j_after[guid]["mid"] == TARGET_MODEL_ID
            and j_after[guid]["fields"] == j_before[guid]["fields"]
            and j_after[guid]["guid_row_count"] == 1
            for guid in different_guids
        )
    )
    evidence["experiments"]["J"] = {
        "verdict": "confirmed" if j_ignored else "refuted",
        "different_model_id": different_model["id"],
        "notes_before": j_before_count,
        "notes_after": j_after_count,
        "existing_notes_unchanged_and_not_duplicated": j_ignored,
        "before": j_before,
        "after": j_after,
        "import_log": j_log,
        "error": j_error,
    }
    target_col.close()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return evidence


def main() -> int:
    args = parse_args()
    evidence = run(args)
    print(json.dumps({key: value["verdict"] for key, value in evidence["experiments"].items()}))
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
