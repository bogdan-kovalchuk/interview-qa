#!/usr/bin/env python3
"""Rebuild provenance rows for fronts carrying ref::* source tags."""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

from verify_front_sources import REQUIRED_COLUMNS


ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
REGISTER = ROOT / "tracking" / "front_sources.csv"
ANSWER_INDEX = ROOT / "sources" / "community" / "tavor118_answer_index.csv"
NOTES = ROOT / "sources" / "notes"


def load_existing() -> dict[str, dict[str, str]]:
    with REGISTER.open(encoding="utf-8", newline="") as handle:
        return {row["card_id"]: row for row in csv.DictReader(handle)}


def load_answer_index() -> dict[str, str]:
    with ANSWER_INDEX.open(encoding="utf-8", newline="") as handle:
        return {row["ref_tag"]: row["answer_ref"] for row in csv.DictReader(handle)}


def official_refs(topic_id: str) -> str:
    brief = next(NOTES.glob(f"{topic_id}_*.md"))
    urls = []
    for line in brief.read_text(encoding="utf-8").splitlines():
        if line.startswith("- Official:") or line.startswith("- Official project docs:"):
            urls.extend(re.findall(r"https://\S+", line))
        elif line.startswith("- Official Python library:") or line.startswith("- Official PostgreSQL:"):
            urls.extend(re.findall(r"https://\S+", line))
        elif line.startswith("- Official Git:") or line.startswith("- Official GitHub Actions:"):
            urls.extend(re.findall(r"https://\S+", line))
    if not urls:
        raise ValueError(f"no official refs found in {brief}")
    return "|".join(dict.fromkeys(urls))


def main() -> None:
    existing = load_existing()
    answer_index = load_answer_index()
    rows: list[dict[str, str]] = []

    for path in sorted(CARDS.glob("*.txt")):
        relative = path.relative_to(ROOT).as_posix()
        for line in path.read_text(encoding="utf-8-sig").splitlines()[5:]:
            if not line.strip() or line.count("\t") != 2:
                continue
            front, _back, tags_field = line.split("\t")
            tags = tags_field.split()
            card_ids = [tag.removeprefix("card::") for tag in tags if tag.startswith("card::")]
            topics = [tag for tag in tags if tag.startswith("topic::")]
            refs = [tag.removeprefix("ref::") for tag in tags if tag.startswith("ref::")]
            if len(card_ids) != 1 or len(topics) != 1:
                raise ValueError(f"invalid ID/topic tags in {path}")
            card_id = card_ids[0]
            topic_id = card_id.split("_")[1]
            if card_id in existing:
                row = dict(existing[card_id])
                row["card_file"] = relative
                row["front_sha256"] = hashlib.sha256(front.encode("utf-8")).hexdigest()
            elif len(refs) == 1:
                ref_tag = refs[0]
                if ref_tag == "OFFICIAL":
                    community_ref = ""
                    source_role = "official_only"
                else:
                    community_ref = answer_index[ref_tag]
                    source_role = "candidate_plus_official"
                row = {
                    "card_id": card_id,
                    "topic_tag": topics[0],
                    "card_file": relative,
                    "front_sha256": hashlib.sha256(front.encode("utf-8")).hexdigest(),
                    "community_answer_ref": community_ref,
                    "official_refs": official_refs(topic_id),
                    "source_role": source_role,
                    "back_status": "drafted" if _back.strip() else "pending",
                    "notes": f"source locator {ref_tag}",
                }
            else:
                raise ValueError(f"expected one ref::* tag for {card_id}")
            rows.append(row)

    rows.sort(key=lambda row: row["card_id"])
    with REGISTER.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Rebuilt {len(rows)} provenance row(s)")


if __name__ == "__main__":
    main()
