#!/usr/bin/env python3
"""Merge completed Back batches into a draft TSV by stable card ID.

A batch row replaces the matching draft row only when:
- the batch file starts with the exact five-line header;
- the card ID exists in the draft exactly once;
- the Front field is byte-identical to the draft Front (provenance hash safety);
- the Back field is non-empty;
- the batch tags keep every draft tag except ``stage::FrontOnly`` and add only
  optional tags from the runtime/version/source/review/gil namespaces.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_cards import EXPECTED_HEADER  # noqa: E402

CARD_PREFIX = "card::"
REMOVABLE_TAGS = {"stage::FrontOnly"}
OPTIONAL_ADD_NAMESPACES = {"runtime", "version", "source", "review", "gil"}


def read_rows(path: Path, errors: list[str]) -> list[tuple[str, str, str]]:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        errors.append(f"{path}: not valid UTF-8: {exc}")
        return []
    lines = text.splitlines()
    if lines[:5] != EXPECTED_HEADER:
        errors.append(f"{path}: first five lines do not match the required header")
        return []
    rows: list[tuple[str, str, str]] = []
    for line_number, line in enumerate(lines[5:], start=6):
        if not line.strip():
            continue
        if line.count("\t") != 2:
            errors.append(
                f"{path}:{line_number}: expected exactly 2 TABs, "
                f"found {line.count(chr(9))}"
            )
            continue
        front, back, tags_field = line.split("\t")
        rows.append((front, back, tags_field))
    return rows


def card_id_of(tags_field: str) -> str | None:
    ids = [tag for tag in tags_field.split() if tag.startswith(CARD_PREFIX)]
    return ids[0] if len(ids) == 1 else None


def merge(
    draft_path: Path, batch_paths: list[Path]
) -> tuple[list[str], list[str]]:
    """Return (merged card IDs, errors). The draft is rewritten only on success."""
    errors: list[str] = []
    draft_rows = read_rows(draft_path, errors)
    draft_index: dict[str, int] = {}
    for position, (_front, _back, tags_field) in enumerate(draft_rows):
        card_id = card_id_of(tags_field)
        if card_id is None:
            errors.append(f"{draft_path}:{position + 6}: row without one card:: ID")
            continue
        if card_id in draft_index:
            errors.append(f"{draft_path}: duplicate {card_id}")
            continue
        draft_index[card_id] = position

    replacements: dict[str, tuple[str, str, str]] = {}
    for batch_path in batch_paths:
        for offset, (front, back, tags_field) in enumerate(read_rows(batch_path, errors)):
            location = f"{batch_path}:{offset + 6}"
            card_id = card_id_of(tags_field)
            if card_id is None:
                errors.append(f"{location}: row without one card:: ID")
                continue
            if card_id in replacements:
                errors.append(f"{location}: duplicate {card_id} across batches")
                continue
            if card_id not in draft_index:
                errors.append(f"{location}: {card_id} is not in the draft")
                continue
            draft_front, _draft_back, draft_tags_field = draft_rows[draft_index[card_id]]
            if front != draft_front:
                errors.append(f"{location}: Front differs from the draft for {card_id}")
                continue
            if not back.strip():
                errors.append(f"{location}: Back must be non-empty for {card_id}")
                continue
            if "stage::FrontOnly" in tags_field.split():
                errors.append(
                    f"{location}: stage::FrontOnly must be removed for {card_id}"
                )
                continue
            draft_tags = set(draft_tags_field.split())
            batch_tags = set(tags_field.split())
            removed = (draft_tags - batch_tags) - REMOVABLE_TAGS
            if removed:
                errors.append(
                    f"{location}: tags removed for {card_id}: "
                    f"{', '.join(sorted(removed))}"
                )
                continue
            added = batch_tags - draft_tags
            bad_adds = sorted(
                tag
                for tag in added
                if tag.split("::", 1)[0] not in OPTIONAL_ADD_NAMESPACES
            )
            if bad_adds:
                errors.append(
                    f"{location}: unsupported added tags for {card_id}: "
                    f"{', '.join(bad_adds)}"
                )
                continue
            replacements[card_id] = (front, back, tags_field)

    if errors:
        return [], errors

    final_rows = list(draft_rows)
    for card_id, row in replacements.items():
        final_rows[draft_index[card_id]] = row
    body = "".join(
        f"{front}\t{back}\t{tags_field}\n" for front, back, tags_field in final_rows
    )
    draft_path.write_text(
        "\n".join(EXPECTED_HEADER) + "\n" + body, encoding="utf-8", newline=""
    )
    return sorted(replacements), []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path)
    parser.add_argument("batches", nargs="+", type=Path)
    args = parser.parse_args()

    merged, errors = merge(args.draft, args.batches)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Merge aborted: {len(errors)} error(s), draft not modified.")
        return 1
    print(f"Merged {len(merged)} card(s): {', '.join(merged) if merged else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
