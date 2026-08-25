#!/usr/bin/env python3
"""Verify front-only card IDs and their future-Back provenance records."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path


CARD_ID_RE = re.compile(r"^PYI_[0-9]{2}_[0-9]{3}$")
COMMIT_PERMALINK_RE = re.compile(
    r"^https://github\.com/[^/]+/[^/]+/blob/[0-9a-f]{40}/.+#L[0-9]+(?:-L[0-9]+)?$"
)
REQUIRED_COLUMNS = [
    "card_id",
    "topic_tag",
    "card_file",
    "front_sha256",
    "community_answer_ref",
    "official_refs",
    "source_role",
    "back_status",
    "notes",
]
SOURCE_ROLES = {"candidate_plus_official", "official_only"}
BACK_STATUSES = {"pending", "drafted", "reviewed", "accepted"}


def load_register(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            return {}, [f"{path}: unexpected columns: {reader.fieldnames!r}"]
        records: dict[str, dict[str, str]] = {}
        for line_number, row in enumerate(reader, start=2):
            card_id = row["card_id"]
            if not CARD_ID_RE.fullmatch(card_id):
                errors.append(f"{path}:{line_number}: invalid card_id {card_id!r}")
            if card_id in records:
                errors.append(f"{path}:{line_number}: duplicate card_id {card_id!r}")
            records[card_id] = row
            if row["source_role"] not in SOURCE_ROLES:
                errors.append(
                    f"{path}:{line_number}: invalid source_role {row['source_role']!r}"
                )
            if row["back_status"] not in BACK_STATUSES:
                errors.append(
                    f"{path}:{line_number}: invalid back_status {row['back_status']!r}"
                )
            if not row["official_refs"]:
                errors.append(f"{path}:{line_number}: official_refs must be non-empty")
            elif any(
                not ref.startswith("https://")
                for ref in row["official_refs"].split("|")
            ):
                errors.append(f"{path}:{line_number}: invalid official_refs URL")
            if row["source_role"] == "candidate_plus_official" and not COMMIT_PERMALINK_RE.fullmatch(
                row["community_answer_ref"]
            ):
                errors.append(
                    f"{path}:{line_number}: community answer must be a commit-pinned line permalink"
                )
            if row["source_role"] == "official_only" and row["community_answer_ref"]:
                errors.append(
                    f"{path}:{line_number}: official_only record must not have community_answer_ref"
                )
    return records, errors


def collect_cards(target: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    cards: dict[str, dict[str, str]] = {}
    for path in sorted(target.rglob("*.txt")):
        relative = path.as_posix()
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        for line_number, line in enumerate(lines[5:], start=6):
            if not line.strip() or line.count("\t") != 2:
                continue
            front, back, tags_field = line.split("\t")
            tags = tags_field.split()
            ids = [tag.removeprefix("card::") for tag in tags if tag.startswith("card::")]
            if len(ids) != 1 or not CARD_ID_RE.fullmatch(ids[0]):
                errors.append(f"{path}:{line_number}: invalid or missing card ID")
                continue
            card_id = ids[0]
            if card_id in cards:
                first = cards[card_id]
                errors.append(
                    f"{path}:{line_number}: duplicate {card_id}; first seen at "
                    f"{first['path']}:{first['line']}"
                )
                continue
            topics = [tag for tag in tags if tag.startswith("topic::")]
            cards[card_id] = {
                "front_sha256": hashlib.sha256(front.encode("utf-8")).hexdigest(),
                "topic_tag": topics[0] if len(topics) == 1 else "",
                "path": relative,
                "line": str(line_number),
                "front_only": "stage::FrontOnly" in tags or not back.strip(),
            }
    return cards, errors


def verify(cards_dir: Path, register_path: Path) -> tuple[int, int, list[str]]:
    records, errors = load_register(register_path)
    cards, card_errors = collect_cards(cards_dir)
    errors.extend(card_errors)

    for card_id, card in cards.items():
        record = records.get(card_id)
        if record is None:
            errors.append(f"{card['path']}:{card['line']}: no provenance row for {card_id}")
            continue
        if record["front_sha256"] != card["front_sha256"]:
            errors.append(f"{card_id}: front_sha256 does not match the TSV Front")
        if record["topic_tag"] != card["topic_tag"]:
            errors.append(f"{card_id}: topic_tag does not match the TSV tags")
        expected_path = Path(record["card_file"]).as_posix()
        actual_path = Path(card["path"]).as_posix()
        if not actual_path.endswith(expected_path):
            errors.append(f"{card_id}: card_file does not match {actual_path}")
        status = record["back_status"]
        if card["front_only"] and status != "pending":
            errors.append(
                f"{card_id}: front-only card requires back_status pending, "
                f"found {status!r}"
            )
        if not card["front_only"] and status not in {"drafted", "reviewed", "accepted"}:
            errors.append(
                f"{card_id}: completed card requires back_status "
                f"drafted/reviewed/accepted, found {status!r}"
            )

    orphaned = sorted(set(records) - set(cards))
    for card_id in orphaned:
        errors.append(f"{register_path}: orphaned provenance row {card_id}")

    return len(cards), len(records), errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cards", type=Path, default=Path("cards"))
    parser.add_argument("--register", type=Path, default=Path("tracking/front_sources.csv"))
    args = parser.parse_args()

    card_count, record_count, errors = verify(args.cards, args.register)

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"Checked {card_count} card(s) and {record_count} provenance row(s): "
        f"{len(errors)} error(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
