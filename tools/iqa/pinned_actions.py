"""Implements the `pinned-actions` quality gate (meta/quality-gates.md).

A GitHub Actions `uses:` reference that names a tag (`@v4`) or a branch
(`@main`) can change what code runs on the next checkout without anything in
this repository changing - the tag can be moved, deliberately or by a
compromised account. Pinning by the 40-character commit SHA the tag currently
resolves to removes that: the SHA is immutable, and updating it is a visible,
reviewable diff.

This module does not resolve or verify SHAs against GitHub - it only checks
the *form* of every `uses:` value in `.github/workflows/*.yml` (and `.yaml`):
a 40-hex-character commit SHA, or a reference to a local action/reusable
workflow in this repository (`./...`), which has no remote tag to spoof.
Resolving a new SHA when an action is added or upgraded is a human (or
agent) action, done once, by looking the tag up on GitHub and recording it -
never guessed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import yaml

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
# Matches `owner/repo[/subpath]@ref`, capturing the ref after the last `@`.
USES_RE = re.compile(r"^(?P<spec>[^@\s]+)@(?P<ref>[^\s#]+)")


@dataclass(frozen=True)
class Violation:
    path: Path
    uses: str
    reason: str

    def __str__(self) -> str:
        return f"{self.path.as_posix()}: uses: {self.uses!r} {self.reason}"


def _iter_uses(document: object) -> list[str]:
    """Walk a parsed workflow YAML document and collect every `uses:` value."""
    found: list[str] = []
    if isinstance(document, dict):
        for key, value in document.items():
            if key == "uses" and isinstance(value, str):
                found.append(value)
            else:
                found.extend(_iter_uses(value))
    elif isinstance(document, list):
        for item in document:
            found.extend(_iter_uses(item))
    return found


def find_violations(workflows_dir: Path) -> list[Violation]:
    """Return every `uses:` reference under `workflows_dir` that is not pinned.

    "Pinned" means either a local reference (`./path/to/action`, no remote tag
    to move) or `owner/repo[/sub]@<40-hex-sha>`. Anything else - a version tag,
    a branch name, a short SHA - is a violation.
    """
    violations: list[Violation] = []
    if not workflows_dir.is_dir():
        return violations
    for path in sorted(workflows_dir.glob("*.yml")) + sorted(workflows_dir.glob("*.yaml")):
        try:
            document = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            violations.append(Violation(path, "<unparseable>", f"is not valid YAML: {error}"))
            continue
        for uses in _iter_uses(document):
            if uses.startswith("./") or uses.startswith("docker://"):
                # A local action/reusable workflow, or a Docker image reference -
                # neither has a movable git tag in this repository's action sense.
                continue
            match = USES_RE.match(uses)
            if match is None:
                violations.append(Violation(path, uses, "has no `@ref`; a commit SHA is required"))
                continue
            ref = match.group("ref")
            if not SHA_RE.fullmatch(ref):
                violations.append(
                    Violation(path, uses, f"is pinned to `{ref}`, not a 40-hex commit SHA")
                )
    return violations


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workflows",
        type=Path,
        default=Path(".github/workflows"),
        help="directory of workflow YAML files to check",
    )
    args = parser.parse_args(argv)

    violations = find_violations(args.workflows)
    if not violations:
        print(f"pinned-actions: all `uses:` references under {args.workflows} are pinned by commit SHA")
        return 0
    print(f"pinned-actions: {len(violations)} unpinned action reference(s)")
    for violation in violations:
        print(f"FAIL [pinned-actions] {violation}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
