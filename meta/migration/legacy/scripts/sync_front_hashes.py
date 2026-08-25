#!/usr/bin/env python3
"""Synchronize exact Front SHA-256 values into the provenance register."""

from __future__ import annotations

import csv
import hashlib
import os
from pathlib import Path

from verify_front_sources import REQUIRED_COLUMNS


ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
REGISTER = ROOT / "tracking" / "front_sources.csv"


def collect_hashes() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(CARDS.glob("*.txt")):
        for line in path.read_text(encoding="utf-8-sig").splitlines()[5:]:
            if not line.strip() or line.count("\t") != 2:
                continue
            front, _back, tags_field = line.split("\t")
            tags = tags_field.split()
            ids = [tag.removeprefix("card::") for tag in tags if tag.startswith("card::")]
            if "stage::FrontOnly" in tags and len(ids) == 1:
                if ids[0] in result:
                    raise ValueError(f"duplicate card ID in TSV files: {ids[0]}")
                result[ids[0]] = hashlib.sha256(front.encode("utf-8")).hexdigest()
    return result


def main() -> None:
    hashes = collect_hashes()
    with REGISTER.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            raise ValueError(f"unexpected register columns: {reader.fieldnames!r}")
        rows = list(reader)

    registered = {row["card_id"] for row in rows}
    missing = sorted(set(hashes) - registered)
    orphaned = sorted(registered - set(hashes))
    if missing or orphaned:
        raise ValueError(f"registry mismatch: missing={missing}, orphaned={orphaned}")

    for row in rows:
        row["front_sha256"] = hashes[row["card_id"]]

    temp = REGISTER.with_suffix(".csv.tmp")
    with temp.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temp, REGISTER)
    print(f"Updated {len(rows)} front hash(es) in {REGISTER.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
