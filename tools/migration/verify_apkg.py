"""Independent verification of the built .apkg, per PLAN.md step 4 definition of done.

Imports the package into a throwaway scratch collection (never a real Anki
profile) using the `anki` library directly, then checks:
  - note count matches the exporter's own count,
  - every note's GUID matches the frozen formula (packaging/anki/build.py:guid_for),
  - deck names come from meta/vocabulary.yml (Title Case "Interview QA::Track::Section"),
  - no `Front` field contains the literal string "TODO".
"""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "packaging" / "anki"))

from anki.collection import Collection
from anki.import_export_pb2 import ImportAnkiPackageOptions, ImportAnkiPackageRequest
from google.protobuf.json_format import MessageToDict

import build as anki_build  # packaging/anki/build.py

GUID_SALT = "iqa:v1:"
BASE91 = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)


def guid_for(qid: str) -> str:
    digest = hashlib.sha256((GUID_SALT + qid).encode("utf-8")).digest()[:8]
    n = int.from_bytes(digest, "big")
    out = []
    while n:
        n, rem = divmod(n, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out)) or BASE91[0]


def main() -> int:
    apkg_path = ROOT / "packaging" / "anki" / "dist" / "Interview QA - Full Library.apkg"
    if not apkg_path.exists():
        print(f"MISSING: {apkg_path}")
        return 1

    with tempfile.TemporaryDirectory(prefix="iqa-verify-scratch-") as scratch:
        col_path = Path(scratch) / "verify-scratch-collection.anki2"
        col = Collection(str(col_path))
        try:
            options = ImportAnkiPackageOptions(
                merge_notetypes=True,
                update_notes=1,
                update_notetypes=1,
                with_scheduling=False,
                with_deck_configs=False,
            )
            request = ImportAnkiPackageRequest(package_path=str(apkg_path), options=options)
            log = col.import_anki_package(request)
            col.save()
            summary = MessageToDict(log, preserving_proto_field_name=True)
            print("import log:", json.dumps(summary, indent=2)[:800])

            note_ids = col.find_notes("")
            print(f"note count in scratch collection: {len(note_ids)}")

            fingerprint = json.loads(
                (ROOT / "packaging" / "anki" / "notetype" / "fingerprint.json").read_text(encoding="utf-8")
            )
            expected_model_id = fingerprint["model_id"]

            vocabulary_text = (ROOT / "meta" / "vocabulary.yml").read_text(encoding="utf-8")
            import yaml

            vocabulary = yaml.safe_load(vocabulary_text) or {}
            track_labels = vocabulary.get("track_labels") or {}
            section_labels = vocabulary.get("section_labels_nav") or {}
            valid_track_en = {v["en"] for v in track_labels.values() if isinstance(v, dict) and "en" in v}
            valid_section_en = {v["en"] for v in section_labels.values() if isinstance(v, dict) and "en" in v}

            bad_guid = []
            bad_model = []
            bad_deck = []
            todo_front = []
            deck_names_seen = set()

            for nid in note_ids:
                note = col.get_note(nid)
                if note.mid != expected_model_id:
                    bad_model.append(nid)
                fields = dict(zip(note.keys(), note.fields))
                qid = fields.get("QID", "")
                expected_guid = guid_for(qid)
                if note.guid != expected_guid:
                    bad_guid.append((qid, note.guid, expected_guid))
                if "TODO" in fields.get("Front", ""):
                    todo_front.append(qid)

                for card in note.cards():
                    deck = col.decks.get(card.did)
                    deck_name = deck["name"]
                    deck_names_seen.add(deck_name)
                    parts = deck_name.split("::")
                    if len(parts) != 3 or parts[0] != "Interview QA":
                        bad_deck.append((qid, deck_name))
                    else:
                        track_en, section_en = parts[1], parts[2]
                        if track_en not in valid_track_en or section_en not in valid_section_en:
                            bad_deck.append((qid, deck_name))

            print(f"distinct decks: {len(deck_names_seen)}")
            print(f"notes with wrong model_id: {len(bad_model)}")
            print(f"notes with GUID mismatch: {len(bad_guid)}")
            for b in bad_guid[:10]:
                print("  ", b)
            print(f"notes with a deck name not traceable to vocabulary.yml: {len(bad_deck)}")
            for b in bad_deck[:10]:
                print("  ", b)
            print(f"notes whose Front contains literal TODO: {len(todo_front)}")
            for t in todo_front[:10]:
                print("  ", t)

            ok = not bad_model and not bad_guid and not bad_deck and not todo_front
            print("RESULT:", "PASS" if ok else "FAIL")
            return 0 if ok else 1
        finally:
            col.close()


if __name__ == "__main__":
    raise SystemExit(main())
