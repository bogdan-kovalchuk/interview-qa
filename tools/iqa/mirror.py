"""Generate the Starlight docs mirror from generator-agnostic question Markdown.

This is the one place that turns authored ``content/`` into what the site renders.
Per ``meta/SITE.md`` and ``meta/QUESTIONS.md``, it is responsible for everything the
site is not allowed to see for itself:

- materialising citation tokens ``[^source_id]`` into real Markdown footnote
  definitions built from ``sources`` in frontmatter, so no raw ``[^...]`` token
  reaches the HTML;
- rendering the ``Sources`` section from frontmatter, replacing the
  ``<!-- generated from frontmatter -->`` placeholder;
- substituting the visible section (and subsection) headings for the page's own
  language from ``meta/vocabulary.yml``, since the headings in ``content/`` are
  always the English structural identifiers;
- filtering by ``status`` through ``tools/iqa/lifecycle.py`` - the single
  implementation of the lifecycle table in ``meta/QUESTIONS.md`` section 8 - with
  an explicit ``--preview`` mode that also includes ``draft``/``review``.

Uses ``tools/iqa/model.py`` to parse content; nothing here re-parses Markdown with
ad-hoc regex beyond substituting inline ``qid:`` and citation tokens inside
already-parsed section text.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from typing import Any

import yaml

from .lifecycle import PageMode, lifecycle_for
from .model import Language, ParsedSection, Question, SectionName, Source, parse_question_file


CITATION_RE = re.compile(r"\[\^([a-z0-9]+(?:-[a-z0-9]+)*)\]")
QID_TOKEN_RE = re.compile(r"qid:([a-z0-9][a-z0-9-]*)", re.IGNORECASE)

TOMBSTONE_TEXT: dict[Language, str] = {
    Language.EN: (
        "This question has been withdrawn. The page is kept as a placeholder, not removed as a 404."
    ),
    Language.UK: "Це питання вилучено. Сторінка лишається як позначка, а не видається як 404.",
}


def load_vocabulary(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: vocabulary must be a mapping")
    return value


def _label(table: dict[str, Any], key: str, language: Language, *, what: str) -> str:
    entry = table.get(key)
    if not isinstance(entry, dict) or language.value not in entry:
        raise ValueError(f"no {language.value} label for {what} `{key}` in meta/vocabulary.yml")
    return entry[language.value]


def section_label(vocabulary: dict[str, Any], heading: str, language: Language) -> str:
    return _label(vocabulary.get("section_labels") or {}, heading, language, what="section")


def subsection_label(vocabulary: dict[str, Any], heading: str, language: Language) -> str:
    return _label(vocabulary.get("subsection_labels") or {}, heading, language, what="subsection")


def replace_qids(text: str, known_ids: set[str], base: str, language: Language) -> str:
    def replace(match: re.Match[str]) -> str:
        target_id = match.group(1)
        if target_id not in known_ids:
            raise ValueError(f"unknown qid target {target_id}")
        return f"{base}/{language.value}/q/{target_id}/"

    return QID_TOKEN_RE.sub(replace, text)


def render_sources(sources: tuple[Source, ...]) -> str:
    """One line per source: ``title`` as link text, ``url`` as href.

    ``version``, ``accessed``, ``kind`` and ``applicability`` stay on the page's
    frontmatter only, per meta/ANKI.md's "Рендер Sources" - and per SITE.md's rule
    that templates carry no bare English/Ukrainian string, only vocabulary keys.
    Adding those fields here would mean inventing new UI strings with no entry in
    meta/vocabulary.yml to localise them.
    """
    if not sources:
        return ""
    return "\n".join(f"- [{source.title}]({source.url})" for source in sources)


def render_footnotes(body_raw: str, sources: tuple[Source, ...]) -> str:
    used = sorted(set(CITATION_RE.findall(body_raw)))
    if not used:
        return ""
    by_id = {source.source_id: source for source in sources}
    lines = []
    for source_id in used:
        source = by_id.get(source_id)
        if source is None:
            raise ValueError(f"citation `[^{source_id}]` has no matching source")
        lines.append(f"[^{source_id}]: [{source.title}]({source.url})")
    return "\n".join(lines)


def render_section(
    section: ParsedSection,
    language: Language,
    vocabulary: dict[str, Any],
    known_ids: set[str],
    base: str,
) -> str:
    heading = section_label(vocabulary, section.heading, language)
    if section.subsections:
        parts = [f"## {heading}"]
        for subsection in section.subsections:
            sub_heading = subsection_label(vocabulary, subsection.heading, language)
            content = replace_qids(subsection.content, known_ids, base, language)
            parts.append(f"### {sub_heading}\n\n{content}")
        return "\n\n".join(parts)
    content = replace_qids(section.content, known_ids, base, language)
    return f"## {heading}\n\n{content}"


def render_body(question: Question, vocabulary: dict[str, Any], known_ids: set[str], base: str) -> str:
    rendered_sections: list[str] = []
    for section in question.body.sections:
        if section.heading == SectionName.SOURCES.value:
            heading = section_label(vocabulary, section.heading, question.language)
            sources_markdown = render_sources(question.frontmatter.sources)
            rendered_sections.append(f"## {heading}\n\n{sources_markdown}".rstrip())
        else:
            rendered_sections.append(
                render_section(section, question.language, vocabulary, known_ids, base)
            )
    body = "\n\n".join(rendered_sections)
    footnotes = render_footnotes(question.body.raw, question.frontmatter.sources)
    if footnotes:
        body = f"{body}\n\n{footnotes}"
    return body.strip() + "\n"


def render_tombstone(question: Question) -> str:
    return TOMBSTONE_TEXT[question.language] + "\n"


def _frontmatter_yaml(question: Question, computed: dict[str, Any]) -> str:
    payload = question.frontmatter.model_dump(mode="json")
    payload.update(computed)
    return yaml.safe_dump(payload, allow_unicode=True, sort_keys=True, default_flow_style=False).rstrip("\n")


def mirror_question(
    question: Question,
    output_root: Path,
    base: str,
    known_ids: set[str],
    working_directory: Path,
    source_path: Path,
    vocabulary: dict[str, Any],
    *,
    preview: bool,
) -> tuple[str, str, str] | None:
    decision = lifecycle_for(question, question.language)
    page_mode = decision.preview_page if preview else decision.production_page
    if page_mode is PageMode.ABSENT:
        return None

    language = question.language
    question_id = question.frontmatter.id
    file_slug = question.slug
    route_slug = f"{language.value}/q/{question_id}/{file_slug}"
    canonical = f"{base}/{route_slug}/"
    try:
        source_label = source_path.relative_to(working_directory).as_posix()
    except ValueError:
        source_label = source_path.as_posix()

    if page_mode is PageMode.TOMBSTONE:
        body_markdown = render_tombstone(question)
    else:
        body_markdown = render_body(question, vocabulary, known_ids, base)

    computed = {
        "slug": route_slug,
        "canonical": canonical,
        "source_path": source_label,
        "question_id": question_id,
        "language": language.value,
        "completeness": decision.completeness.value,
    }
    rendered = f"---\n{_frontmatter_yaml(question, computed)}\n---\n\n{body_markdown}"

    destination = output_root / language.value / "q" / question_id / f"{file_slug}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8", newline="\n")
    return language.value, question_id, question.frontmatter.title


def write_locale_indexes(output_root: Path, questions: list[tuple[str, str, str]], base: str) -> None:
    by_language: dict[str, list[tuple[str, str]]] = {}
    for language, question_id, title in questions:
        by_language.setdefault(language, []).append((question_id, title))

    titles = {"en": "Interview questions", "uk": "Питання для співбесід"}
    descriptions = {
        "en": "Bilingual technical interview questions.",
        "uk": "Двомовні питання для технічних співбесід.",
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


def generate(source: Path, output: Path, base: str, *, preview: bool = False, root: Path | None = None) -> int:
    working_directory = Path.cwd().resolve()
    source = source.resolve()
    output = output.resolve()
    base = "/" + base.strip("/")
    root = (root or source.parent).resolve()

    if not source.is_dir():
        raise ValueError(f"source directory does not exist: {source}")
    if output == source or output in source.parents or source in output.parents:
        raise ValueError("source and output directories must not contain one another")

    source_files = sorted(
        path for path in source.rglob("*.md") if len(path.relative_to(source).parts) >= 2
    )
    if not source_files:
        raise ValueError(f"no language-prefixed Markdown files found under {source}")

    vocabulary = load_vocabulary(root / "meta" / "vocabulary.yml")

    parsed = [parse_question_file(path, content_root=source) for path in source_files]
    known_ids = {question.frontmatter.id for question in parsed}

    per_language_ids: set[tuple[str, str]] = set()
    for question in parsed:
        pair = (question.language.value, question.frontmatter.id)
        if pair in per_language_ids:
            raise ValueError(f"duplicate question id for language: {pair}")
        per_language_ids.add(pair)

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}-", dir=output.parent))
    try:
        mirrored: list[tuple[str, str, str]] = []
        for question, path in zip(parsed, source_files):
            result = mirror_question(
                question,
                temporary,
                base,
                known_ids,
                working_directory,
                path,
                vocabulary,
                preview=preview,
            )
            if result is not None:
                mirrored.append(result)
        write_locale_indexes(temporary, mirrored, base)
        if output.exists():
            shutil.rmtree(output)
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)

    return len(mirrored)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("content"))
    parser.add_argument("--out", type=Path, default=Path("site/src/content/docs"))
    parser.add_argument("--base", default="/interview-qa")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--preview",
        action="store_true",
        help="include draft/review questions, per the lifecycle table's preview column",
    )
    args = parser.parse_args()

    try:
        count = generate(args.source, args.out, args.base, preview=args.preview, root=args.root)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    mode = "preview" if args.preview else "production"
    print(f"Mirrored {count} question pages ({mode}) into {args.out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
