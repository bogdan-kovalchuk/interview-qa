"""Read the frozen M4 migration input: `meta/migration/legacy/*`.

Pure parsing, no classification and no writing - `migrate_legacy.py` is the
only caller. Kept separate so the parsing step can be checked (and re-run)
on its own; see tools/migration_work/ for the exploratory version this was
promoted from.
"""
from __future__ import annotations

import csv
import glob
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CARDS_DIR = ROOT / "meta" / "migration" / "legacy" / "cards"
FRONT_SOURCES = ROOT / "meta" / "migration" / "legacy" / "front-sources.csv"
CODE_CHECKS = ROOT / "meta" / "migration" / "legacy" / "code-checks.csv"


def _parse_tags(tag_field: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for token in tag_field.split():
        if "::" not in token:
            continue
        ns, val = token.split("::", 1)
        out.setdefault(ns, []).append(val)
    return out


def load_cards() -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for path in sorted(glob.glob(str(CARDS_DIR / "*.txt"))):
        fname = Path(path).stem
        with open(path, encoding="utf-8") as handle:
            lines = handle.readlines()
        order = 0
        for line in lines:
            if line.startswith("#"):
                continue
            line = line.rstrip("\r\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                raise ValueError(f"{path}: expected 3 columns, got {len(parts)}: {line[:80]!r}")
            front, back, tags_field = parts
            tags = _parse_tags(tags_field)
            card_ids = tags.get("card")
            if not card_ids or len(card_ids) != 1:
                raise ValueError(f"{path}: missing/multiple card:: tag: {tags_field!r}")
            order += 1
            cards.append(
                {
                    "legacy_card_id": card_ids[0],
                    "topic_file": fname,
                    "order_in_file": order,
                    "front_html": front,
                    "back_html": back,
                    "tags": tags,
                }
            )
    return cards


def load_front_sources() -> dict[str, dict[str, str]]:
    with open(FRONT_SOURCES, encoding="utf-8", newline="") as handle:
        return {row["card_id"]: row for row in csv.DictReader(handle)}


def load_code_checks() -> dict[str, dict[str, str]]:
    with open(CODE_CHECKS, encoding="utf-8", newline="") as handle:
        return {row["card_id"]: row for row in csv.DictReader(handle)}


def load_all() -> list[dict[str, Any]]:
    """Every card, joined with its front-sources.csv and code-checks.csv rows.

    Raises if the join is not exact - every card must have one front-sources
    row, and every front-sources row must match a card (checkpoint 1: nothing
    silently dropped).
    """
    cards = load_cards()
    if len(cards) != 392:
        raise SystemExit(f"expected 392 legacy cards, found {len(cards)}")

    sources = load_front_sources()
    checks = load_code_checks()

    missing = [c["legacy_card_id"] for c in cards if c["legacy_card_id"] not in sources]
    if missing:
        raise SystemExit(f"cards with no front-sources.csv row: {missing}")
    extra = sorted(set(sources) - {c["legacy_card_id"] for c in cards})
    if extra:
        raise SystemExit(f"front-sources.csv rows with no matching card: {extra}")

    for card in cards:
        cid = card["legacy_card_id"]
        row = sources[cid]
        card["official_refs"] = [u.strip() for u in row["official_refs"].split("|") if u.strip()]
        card["community_ref"] = row["community_answer_ref"].strip() or None
        card["front_sha256"] = row["front_sha256"]
        card["source_role"] = row["source_role"]
        card["back_status"] = row["back_status"]
        card["code_check"] = checks.get(cid)

    return cards
