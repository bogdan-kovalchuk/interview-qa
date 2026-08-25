"""Generate the Starlight docs mirror from generator-agnostic question Markdown."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile


FRONTMATTER = re.compile(r"\A---[ \t]*\r?\n(?P<header>.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
QID_TOKEN = re.compile(r"qid:([a-z0-9][a-z0-9-]*)", re.IGNORECASE)
INJECTED_KEYS = {"canonical", "language", "question_id", "slug", "source_path"}


def scalar(header: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:[ \t]*(.+?)[ \t]*$", header)
    if not match:
        raise ValueError(f"missing required frontmatter field: {key}")
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    if not value:
        raise ValueError(f"empty required frontmatter field: {key}")
    return value


def remove_injected_fields(header: str) -> str:
    kept = []
    for line in header.splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line)
        if match and match.group(1) in INJECTED_KEYS:
            continue
        kept.append(line)
    return "\n".join(kept).rstrip()


def source_label(path: Path, working_directory: Path) -> str:
    try:
        return path.relative_to(working_directory).as_posix()
    except ValueError:
        return path.as_posix()


def mirror_question(
    source_file: Path,
    relative_file: Path,
    output_root: Path,
    base: str,
    known_ids: set[str],
    working_directory: Path,
) -> tuple[str, str, str]:
    text = source_file.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError(f"{source_file}: missing YAML frontmatter")

    language = relative_file.parts[0]
    question_id = scalar(match.group("header"), "id")
    title = scalar(match.group("header"), "title")
    file_slug = source_file.stem
    route_slug = f"{language}/q/{question_id}/{file_slug}"
    canonical = f"{base}/{route_slug}/"
    source_path = source_label(source_file, working_directory)

    body = text[match.end() :]

    def replace_qid(token: re.Match[str]) -> str:
        target_id = token.group(1)
        if target_id not in known_ids:
            raise ValueError(f"{source_file}: unknown qid target {target_id}")
        return f"{base}/{language}/q/{target_id}/"

    body = QID_TOKEN.sub(replace_qid, body)
    original_header = remove_injected_fields(match.group("header"))
    computed = [
        f"slug: {json.dumps(route_slug, ensure_ascii=False)}",
        f"canonical: {json.dumps(canonical, ensure_ascii=False)}",
        f"source_path: {json.dumps(source_path, ensure_ascii=False)}",
        f"question_id: {json.dumps(question_id, ensure_ascii=False)}",
        f"language: {json.dumps(language, ensure_ascii=False)}",
    ]
    rendered = f"---\n{original_header}\n" + "\n".join(computed) + f"\n---\n{body}"

    destination = output_root / language / "q" / question_id / f"{file_slug}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8", newline="\n")
    return language, question_id, title


def write_locale_indexes(output_root: Path, questions: list[tuple[str, str, str]], base: str) -> None:
    by_language: dict[str, list[tuple[str, str]]] = {}
    for language, question_id, title in questions:
        by_language.setdefault(language, []).append((question_id, title))

    titles = {"en": "Interview questions", "uk": "Питання для співбесід"}
    descriptions = {
        "en": "Bilingual interview question spike fixtures.",
        "uk": "Двомовні тестові питання для перевірки архітектури.",
    }
    for language, entries in sorted(by_language.items()):
        lines = [
            "---",
            f"title: {json.dumps(titles.get(language, 'Interview questions'), ensure_ascii=False)}",
            f"description: {json.dumps(descriptions.get(language, 'Interview questions.'), ensure_ascii=False)}",
            "sidebar:",
            "  hidden: true",
            "---",
            "",
        ]
        for question_id, title in sorted(entries):
            lines.append(f"- [{title}]({base}/{language}/q/{question_id}/)")
        lines.append("")
        destination = output_root / language / "index.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def generate(source: Path, output: Path, base: str) -> int:
    working_directory = Path.cwd().resolve()
    source = source.resolve()
    output = output.resolve()
    base = "/" + base.strip("/")

    if not source.is_dir():
        raise ValueError(f"source directory does not exist: {source}")
    if output == source or output in source.parents or source in output.parents:
        raise ValueError("source and output directories must not contain one another")

    source_files = sorted(path for path in source.rglob("*.md") if len(path.relative_to(source).parts) >= 2)
    if not source_files:
        raise ValueError(f"no language-prefixed Markdown files found under {source}")

    known_ids: set[str] = set()
    per_language_ids: set[tuple[str, str]] = set()
    for path in source_files:
        relative = path.relative_to(source)
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            raise ValueError(f"{path}: missing YAML frontmatter")
        question_id = scalar(match.group("header"), "id")
        pair = (relative.parts[0], question_id)
        if pair in per_language_ids:
            raise ValueError(f"duplicate question id for language: {pair}")
        per_language_ids.add(pair)
        known_ids.add(question_id)

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}-", dir=output.parent))
    try:
        questions = [
            mirror_question(
                path,
                path.relative_to(source),
                temporary,
                base,
                known_ids,
                working_directory,
            )
            for path in source_files
        ]
        write_locale_indexes(temporary, questions, base)
        if output.exists():
            shutil.rmtree(output)
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)

    return len(source_files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("content"))
    parser.add_argument("--out", type=Path, default=Path("site/src/content/docs"))
    parser.add_argument("--base", default="/interview-qa")
    args = parser.parse_args()

    try:
        count = generate(args.source, args.out, args.base)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Mirrored {count} question files into {args.out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
