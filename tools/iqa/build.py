"""The one build path: validate -> export -> mirror -> astro build -> verify.

Exposed as a single command (``python -m iqa build`` or ``iqa build`` once
installed) so there is exactly one way to produce a production site build, and
no way to reach ``astro build`` while skipping validation or mirroring.

``npm run build`` (``site/scripts/build.mjs``) itself refuses to run
``astro build`` without first regenerating the mirror from the current
``content/`` - that is enforced there, not duplicated here, so there is exactly
one place that decides what the mirror contains. This module only adds the two
gates on either side of it: content validation before, and build verification
after.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

from .export import run as run_export
from .validate import print_report, validate_repository


def run(root: Path) -> int:
    root = root.resolve()

    print("== 1/4: validate content ==")
    report = validate_repository(root)
    print_report(report)
    if not report.ok:
        print("Content validation failed; refusing to mirror or build.", file=sys.stderr)
        return 1

    # The deck builder reads dist/export/questions.json and nothing else, so the export
    # belongs inside the one build path. Left outside it, a stale questions.json would
    # silently produce a deck from old content - the exact failure mode the mirror guard
    # exists to prevent.
    print("\n== 2/4: export dist/export/questions.json ==")
    exported = run_export(root)
    if exported != 0:
        print("Export failed; refusing to build.", file=sys.stderr)
        return exported

    print("\n== 3/4: npm run build (regenerates the mirror, then astro build) ==")
    npm = shutil.which("npm")
    if npm is None:
        print("npm not found on PATH", file=sys.stderr)
        return 1
    site_build = subprocess.run([npm, "run", "build"], cwd=str(root / "site"))
    if site_build.returncode != 0:
        print("Site build failed.", file=sys.stderr)
        return site_build.returncode

    print("\n== 4/4: verify build ==")
    verify = subprocess.run(
        [sys.executable, str(root / "tools" / "verify_build.py")], cwd=str(root)
    )
    return verify.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    return run(args.root)


if __name__ == "__main__":
    raise SystemExit(main())
