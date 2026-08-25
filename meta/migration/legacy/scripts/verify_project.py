#!/usr/bin/env python3
"""Validate project-wide topic, coverage, status, and release-gate consistency."""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OVERVIEW_CAP = 7
BRIEF_STATUSES = {"missing", "planned", "complete"}
SOURCE_STATUSES = {"missing", "recorded", "verified"}
CONTENT_STATUSES = {
    "missing",
    "empty",
    "fronts_drafted",
    "fronts_reviewed",
    "backs_drafted",
    "ready",
}
REVIEW_STATUSES = {"not_started", "in_progress", "reviewed", "accepted"}
CODE_CHECK_STATUSES = {"deferred_until_back", "verified", "not_executable"}
BRIEF_ROW_RE = re.compile(
    r"^\|.*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|$"
)
TAXONOMY_ROW_RE = re.compile(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def card_rows(path: Path) -> list[tuple[str, str, list[str]]]:
    rows: list[tuple[str, str, list[str]]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines()[5:]:
        if line.strip() and line.count("\t") == 2:
            front, back, tags = line.split("\t")
            rows.append((front, back, tags.split()))
    return rows


def brief_counts(path: Path) -> tuple[int, int, int]:
    middle = senior = total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        match = BRIEF_ROW_RE.match(line)
        if match:
            middle += int(match.group(1))
            senior += int(match.group(2))
            total += int(match.group(3))
    return middle, senior, total


def validate_project(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    manifest = json.loads(
        (root / "authoring" / "manifest.json").read_text(encoding="utf-8")
    )
    if manifest.get("deck") != "Python Interview Questions":
        errors.append("manifest deck must be Python Interview Questions")
    topics = {item["id"]: item for item in manifest["topics"]}
    deck_names = [item.get("deck_name") for item in topics.values()]
    if any(not isinstance(name, str) or not name for name in deck_names) or len(set(deck_names)) != len(topics):
        errors.append("manifest topic deck_name values must be present and unique")
    expected_names = {f"{item['id']}_{item['slug']}.txt" for item in topics.values()}

    cards_dir = root / "cards"
    actual_names = {path.name for path in cards_dir.glob("*.txt")}
    if actual_names != expected_names:
        errors.append(
            "card TSV filenames do not match manifest: "
            f"missing={sorted(expected_names - actual_names)}, "
            f"extra={sorted(actual_names - expected_names)}"
        )

    taxonomy = (root / "authoring" / "TAXONOMY.md").read_text(encoding="utf-8")
    taxonomy_topics = {
        match.group(1): match.group(2)
        for line in taxonomy.splitlines()
        if (match := TAXONOMY_ROW_RE.match(line))
    }
    manifest_topics = {topic_id: item["slug"] for topic_id, item in topics.items()}
    if taxonomy_topics != manifest_topics:
        errors.append("manifest topics do not match authoring/TAXONOMY.md")

    coverage_rows = read_csv(root / "tracking" / "coverage.csv")
    plan_rows = read_csv(root / "tracking" / "front_coverage_plan.csv")
    coverage = {row["topic_id"]: row for row in coverage_rows}
    plan = {row["topic_id"]: row for row in plan_rows}
    expected_ids = set(topics)
    if set(coverage) != expected_ids or len(coverage_rows) != len(expected_ids):
        errors.append("tracking/coverage.csv topic IDs do not match manifest")
    if set(plan) != expected_ids or len(plan_rows) != len(expected_ids):
        errors.append("tracking/front_coverage_plan.csv topic IDs do not match manifest")

    actual: dict[str, dict[str, int]] = {}
    accepted_counts: dict[str, int] = {topic_id: 0 for topic_id in expected_ids}
    accepted_code_ids: set[str] = set()
    all_card_ids: set[str] = set()
    for topic_id, item in topics.items():
        name = f"{topic_id}_{item['slug']}.txt"
        path = cards_dir / name
        rows = card_rows(path) if path.exists() else []
        actual[topic_id] = {
            "total": len(rows),
            "middle": sum("level::Middle" in tags for _, _, tags in rows),
            "senior": sum("level::Senior" in tags for _, _, tags in rows),
        }
        for _, _, tags in rows:
            all_card_ids.update(tag.removeprefix("card::") for tag in tags if tag.startswith("card::"))

        accepted_counts[topic_id] = len(rows)
        for _, _, tags in rows:
            if "stage::FrontOnly" in tags:
                errors.append(f"{path}: Front-only card is not allowed in package source")
            if "type::Code" in tags:
                ids = [tag.removeprefix("card::") for tag in tags if tag.startswith("card::")]
                if len(ids) != 1:
                    errors.append(f"{path}: Code card requires one stable card ID")
                else:
                    accepted_code_ids.add(ids[0])

    for topic_id, item in topics.items():
        row = coverage.get(topic_id)
        planned = plan.get(topic_id)
        if row is None or planned is None:
            continue
        if row["topic_slug"] != item["slug"]:
            errors.append(f"topic {topic_id}: coverage slug does not match manifest")
        if row["scope"] != item["scope"] or row["priority"] != item["priority"]:
            errors.append(f"topic {topic_id}: coverage scope/priority does not match manifest")
        if row["brief_status"] not in BRIEF_STATUSES:
            errors.append(f"topic {topic_id}: invalid brief_status {row['brief_status']!r}")
        if row["sources_status"] not in SOURCE_STATUSES:
            errors.append(f"topic {topic_id}: invalid sources_status {row['sources_status']!r}")
        if row["content_status"] not in CONTENT_STATUSES:
            errors.append(f"topic {topic_id}: invalid content_status {row['content_status']!r}")
        if row["review_status"] not in REVIEW_STATUSES:
            errors.append(f"topic {topic_id}: invalid review_status {row['review_status']!r}")

        front_count = int(row["front_count"])
        accepted = int(row["accepted_cards"])
        if front_count != actual[topic_id]["total"]:
            errors.append(f"topic {topic_id}: front_count does not match card TSV")
        if accepted != accepted_counts[topic_id]:
            errors.append(f"topic {topic_id}: accepted_cards does not match card TSV")
        if row["content_status"] == "fronts_reviewed":
            if row["review_status"] != "reviewed" or not row["last_reviewed"]:
                errors.append(f"topic {topic_id}: reviewed Fronts require review status and date")
        if row["last_reviewed"]:
            try:
                date.fromisoformat(row["last_reviewed"])
            except ValueError:
                errors.append(f"topic {topic_id}: last_reviewed must use YYYY-MM-DD")

        planned_total = int(planned["planned_total"])
        planned_middle = int(planned["planned_middle"])
        planned_senior = int(planned["planned_senior"])
        if int(row["planned_fronts"]) != planned_total:
            errors.append(f"topic {topic_id}: coverage and plan totals differ")
        if row["content_status"] in {"fronts_reviewed", "backs_drafted", "ready"}:
            if (
                actual[topic_id]["total"] != planned_total
                or actual[topic_id]["middle"] != planned_middle
                or actual[topic_id]["senior"] != planned_senior
            ):
                errors.append(f"topic {topic_id}: reviewed card TSV does not match level plan")

        brief_path = root / "sources" / "notes" / f"{topic_id}_{item['slug']}.md"
        if not brief_path.exists():
            errors.append(f"topic {topic_id}: topic brief is missing")
        elif brief_counts(brief_path) != (planned_middle, planned_senior, planned_total):
            errors.append(f"topic {topic_id}: brief coverage table does not match plan")

        if item["scope"] == "Overview" and (
            planned_total > OVERVIEW_CAP or actual[topic_id]["total"] > OVERVIEW_CAP
        ):
            errors.append(f"topic {topic_id}: Overview cap of {OVERVIEW_CAP} exceeded")

    code_check_path = root / "tracking" / "code_checks.csv"
    code_checks = read_csv(code_check_path)
    checks_by_id: dict[str, dict[str, str]] = {}
    for row in code_checks:
        card_id = row["card_id"]
        if card_id in checks_by_id:
            errors.append(f"tracking/code_checks.csv: duplicate {card_id}")
        checks_by_id[card_id] = row
        if row["status"] not in CODE_CHECK_STATUSES:
            errors.append(f"{card_id}: invalid Code-check status {row['status']!r}")
        if card_id not in all_card_ids and card_id not in accepted_code_ids:
            errors.append(f"tracking/code_checks.csv: unknown card ID {card_id}")
    for card_id in sorted(accepted_code_ids):
        check = checks_by_id.get(card_id)
        if check is None:
            errors.append(f"{card_id}: package-source Code card has no executable check record")
        elif check["status"] == "deferred_until_back":
            errors.append(f"{card_id}: deferred Code check is not allowed in package source")
        elif check["status"] == "verified" and not (
            check["python_version"] and check["evidence"]
        ):
            errors.append(f"{card_id}: verified Code check requires version and evidence")
        elif check["status"] == "not_executable" and not check["notes"]:
            errors.append(f"{card_id}: not_executable requires reviewer notes")

    card_files = sorted(cards_dir.glob("*.txt"))
    accepted_total = sum(int(row["accepted_cards"]) for row in coverage_rows)
    smoke_rows = read_csv(root / "tracking" / "anki_smoke.csv")
    if card_files or accepted_total:
        passed_files = {row["source_file"] for row in smoke_rows if row["result"] == "pass"}
        for card_file in card_files:
            relative = card_file.relative_to(root).as_posix()
            if relative not in passed_files:
                errors.append(f"{relative}: no passing Anki smoke record")

    package_relative = manifest.get("package")
    authoring_relative = manifest.get("authoring_collection")
    if not isinstance(package_relative, str) or not (root / package_relative).is_file():
        errors.append("production .apkg is missing")
    if not isinstance(authoring_relative, str) or not (root / authoring_relative).is_file():
        errors.append("persistent authoring collection is missing")
    identity_path = root / "tracking" / "apkg_note_identity.csv"
    if not identity_path.is_file():
        errors.append("tracking/apkg_note_identity.csv is missing")
    else:
        identities = read_csv(identity_path)
        identity_ids = [row.get("card_id", "") for row in identities]
        expected_identity_ids = sorted(card_id for card_id in all_card_ids if card_id)
        if sorted(identity_ids) != expected_identity_ids or len(identity_ids) != len(set(identity_ids)):
            errors.append("APKG identity manifest does not match accepted card IDs")
    if isinstance(package_relative, str) and package_relative not in {
        row["source_file"] for row in smoke_rows if row["result"] == "pass"
    }:
        errors.append("production .apkg has no passing smoke record")

    return errors


def main() -> int:
    errors = validate_project()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked project metadata and release gates: {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
