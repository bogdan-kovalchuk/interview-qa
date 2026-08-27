"""Command-line entry point for the Interview QA tools."""

from __future__ import annotations

import argparse
from pathlib import Path

from . import build as build_module
from .export import write_export
from .model import export_question_schema
from .pinned_actions import main as pinned_actions_main
from .report import main as report_main
from .validate import print_report, validate_repository


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="iqa")
    subcommands = parser.add_subparsers(dest="command", required=True)

    validate = subcommands.add_parser("validate", help="validate content-only quality gates")
    validate.add_argument("--root", type=Path, default=Path.cwd())

    schema = subcommands.add_parser("export-schema", help="regenerate the question JSON Schema")
    schema.add_argument("--root", type=Path, default=Path.cwd())

    export = subcommands.add_parser(
        "export", help="write dist/export/questions.json from the model"
    )
    export.add_argument("--root", type=Path, default=Path.cwd())
    export.add_argument("--out", type=Path, default=None)
    export.add_argument("--base", default="/interview-qa")
    export.add_argument(
        "--in-withdrawal-window",
        action="store_true",
        help="treat withdrawn questions as still inside their two-release removal window",
    )

    build = subcommands.add_parser(
        "build", help="the one build path: validate -> mirror -> astro build -> verify"
    )
    build.add_argument("--root", type=Path, default=Path.cwd())

    report = subcommands.add_parser(
        "report", help="write dist/export/progress.{json,csv}, or print the next TODO with --todo"
    )
    report.add_argument("--root", type=Path, default=Path.cwd())
    report.add_argument(
        "--todo",
        action="store_true",
        help="print the next incomplete (question, language) pairs instead of writing files",
    )

    pinned_actions = subcommands.add_parser(
        "check-pinned-actions",
        help="fail if any `uses:` in .github/workflows/ is not a 40-hex commit SHA",
    )
    pinned_actions.add_argument(
        "--workflows", type=Path, default=Path(".github/workflows")
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "check-pinned-actions":
        return pinned_actions_main(["--workflows", str(args.workflows)])

    root = args.root.resolve()
    if args.command == "export-schema":
        destination = root / "meta" / "schema" / "question.schema.json"
        export_question_schema(destination)
        print(destination.as_posix())
        return 0

    if args.command == "export":
        destination = args.out if args.out is not None else root / "dist" / "export" / "questions.json"
        count = write_export(
            root / "content",
            destination,
            base=args.base,
            in_withdrawal_window=args.in_withdrawal_window,
        )
        print(f"Exported {count} questions into {destination.as_posix()}")
        return 0

    if args.command == "build":
        return build_module.run(root)

    if args.command == "report":
        report_argv = ["--root", str(root)]
        if args.todo:
            report_argv.append("--todo")
        return report_main(report_argv)

    report = validate_repository(root)
    print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
