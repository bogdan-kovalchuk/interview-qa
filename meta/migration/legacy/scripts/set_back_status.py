#!/usr/bin/env python3
"""Update back_status for provenance rows in tracking/front_sources.csv.

Select rows by card IDs and/or by two-digit topic ID, then set one valid
status for all of them. Refuses to touch rows that are not selected.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_front_sources import BACK_STATUSES, CARD_ID_RE, REQUIRED_COLUMNS  # noqa: E402


def set_status(
    register_path: Path, status: str, card_ids: list[str], topic_id: str | None
) -> tuple[list[str], list[str]]:
    """Return (updated card IDs, errors)."""
    errors: list[str] = []
    if status not in BACK_STATUSES:
        errors.append(f"invalid status {status!r}; expected one of {sorted(BACK_STATUSES)}")
    selected_ids = set()
    for card_id in card_ids:
        if not CARD_ID_RE.fullmatch(card_id):
            errors.append(f"invalid card ID {card_id!r}")
            continue
        selected_ids.add(card_id)
    if topic_id is not None and not topic_id.isdigit():
        errors.append(f"topic ID must be numeric, got {topic_id!r}")
    if errors:
        return [], errors

    with register_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            return [], [f"{register_path}: unexpected columns: {reader.fieldnames!r}"]
        rows = list(reader)

    updated: list[str] = []
    seen = set()
    for row in rows:
        card_id = row["card_id"]
        seen.add(card_id)
        matches = bool(selected_ids and card_id in selected_ids)
        if topic_id is not None:
            matches = matches or card_id.startswith(f"PYI_{topic_id.zfill(2)}_")
        if matches and row["back_status"] != status:
            row["back_status"] = status
            updated.append(card_id)

    missing = sorted(selected_ids - seen)
    for card_id in missing:
        errors.append(f"{register_path}: no row for {card_id}")
    if errors:
        return [], errors

    with register_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return sorted(updated), []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("status", help="one of: pending, drafted, reviewed, accepted")
    parser.add_argument("--ids", default="", help="comma-separated card IDs")
    parser.add_argument("--topic", default=None, help="two-digit topic ID")
    parser.add_argument(
        "--register", type=Path, default=Path("tracking/front_sources.csv")
    )
    args = parser.parse_args()

    card_ids = [part.strip() for part in args.ids.split(",") if part.strip()]
    if not card_ids and args.topic is None:
        print("ERROR: provide --ids and/or --topic", file=sys.stderr)
        return 1
    updated, errors = set_status(args.register, args.status, card_ids, args.topic)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Updated {len(updated)} row(s) to back_status={args.status}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
