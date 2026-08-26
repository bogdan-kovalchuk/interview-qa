"""Command-line entry point for the Interview QA tools."""

from __future__ import annotations

import argparse
from pathlib import Path

from .model import export_question_schema
from .validate import print_report, validate_repository


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="iqa")
    subcommands = parser.add_subparsers(dest="command", required=True)

    validate = subcommands.add_parser("validate", help="validate content-only quality gates")
    validate.add_argument("--root", type=Path, default=Path.cwd())

    schema = subcommands.add_parser("export-schema", help="regenerate the question JSON Schema")
    schema.add_argument("--root", type=Path, default=Path.cwd())
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    root = args.root.resolve()
    if args.command == "export-schema":
        destination = root / "meta" / "schema" / "question.schema.json"
        export_question_schema(destination)
        print(destination.as_posix())
        return 0

    report = validate_repository(root)
    print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
