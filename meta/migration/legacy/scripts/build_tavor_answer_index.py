#!/usr/bin/env python3
"""Build a copyright-safe line index for the audited tavor118 Q&A snapshot."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from pathlib import Path


EXPECTED_COMMIT = "02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141"
REPOSITORY_URL = "https://github.com/tavor118/pj_python_interview_questions_and_answers"
BADGE_RE = re.compile(r"\s*\[(?:\D+?)(\d+)/\d+]\s*$")


def heading_lines(lines: list[str]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    in_fence = False
    for number, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,3}) ", line)
        if match:
            result.append((number, len(match.group(1))))
    return result


def source_code(relative: Path) -> str:
    value = relative.with_suffix("").as_posix().upper()
    return re.sub(r"[^A-Z0-9]+", "_", value).strip("_")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("sources/community/tavor118_answer_index.csv"),
    )
    args = parser.parse_args()

    actual_commit = subprocess.check_output(
        ["git", "-C", str(args.source_repo), "rev-parse", "HEAD"], text=True
    ).strip()
    if actual_commit != EXPECTED_COMMIT:
        raise ValueError(f"expected {EXPECTED_COMMIT}, got {actual_commit}")

    docs = args.source_repo / "docs"
    rows: list[dict[str, str | int]] = []
    for path in sorted(docs.rglob("*.md")):
        if path.name == "top_questions.md":
            continue
        relative = path.relative_to(docs)
        lines = path.read_text(encoding="utf-8").splitlines()
        headings = heading_lines(lines)
        question_number = 0
        for position, (start, level) in enumerate(headings):
            if level != 3:
                continue
            question_number += 1
            end = (
                headings[position + 1][0] - 1
                if position + 1 < len(headings)
                else len(lines)
            )
            heading = lines[start - 1]
            badge = BADGE_RE.search(heading)
            score = int(badge.group(1)) if badge else ""
            ref_tag = f"TV_{source_code(relative)}_{question_number:02d}"
            rows.append(
                {
                    "ref_tag": ref_tag,
                    "source_file": relative.as_posix(),
                    "question_ordinal": question_number,
                    "start_line": start,
                    "end_line": end,
                    "popularity_score": score,
                    "answer_ref": (
                        f"{REPOSITORY_URL}/blob/{EXPECTED_COMMIT}/docs/"
                        f"{relative.as_posix()}#L{start}-L{end}"
                    ),
                }
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} answer locator(s) to {args.output}")


if __name__ == "__main__":
    main()
