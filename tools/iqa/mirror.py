"""Generate the Starlight docs mirror from generator-agnostic question Markdown.

This is the one place that turns authored ``content/`` into what the site renders.
Per ``meta/site.md`` and ``meta/questions.md``, it is responsible for everything the
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
  implementation of the lifecycle table in ``meta/questions.md`` section 8 - with
  an explicit ``--preview`` mode that also includes ``draft``/``review``.

Uses ``tools/iqa/model.py`` to parse content; nothing here re-parses Markdown with
ad-hoc regex beyond substituting inline ``qid:`` and citation tokens inside
already-parsed section text.
"""

from __future__ import annotations

import argparse
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import stat
import time
import tempfile
from typing import Any, NamedTuple

import yaml

from .lifecycle import PageMode, lifecycle_for
from .taxonomy import ordered_tracks_and_sections
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


def completeness_label(vocabulary: dict[str, Any], completeness: str, language: Language) -> str:
    return _label(vocabulary.get("completeness_labels") or {}, completeness, language, what="completeness")


# Sidebar badge variant per completeness (meta/plan.md step 6, item 3: "the reader must be
# able to see at a glance which entries in an index are thin"). `complete` gets no
# badge at all - see mirror_question - so it is not listed here.
COMPLETENESS_BADGE_VARIANT: dict[str, str] = {
    "empty": "danger",
    "stub": "caution",
    "partial": "note",
}


class MirroredPage(NamedTuple):
    """One question page the mirror actually wrote, as the navigation needs it.

    `mirror_question` used to hand back `(language, id, title)`, which was
    enough for a flat list of links and nothing else. Track, section and
    completeness are what turn that list into the taxonomy navigation.
    """

    language: str
    question_id: str
    title: str
    track: str
    section: str
    route_slug: str
    completeness: str


class NavigationPage(NamedTuple):
    """One generated page in the per-language reading order."""

    source_path: Path
    href: str
    label: str


INLINE_CODE_RE = re.compile(r"`([^`\r\n]+)`")


def title_text(title: str) -> str:
    """The title with the inline-code markers removed.

    A `title` may carry Markdown inline code - 475 of the 802 files do. Starlight
    puts `title` into places that are plain text and cannot hold markup: the
    browser `<title>`, `og:title`, the sidebar. Left as they are, the backticks
    show up literally there, which is what this strips.
    """
    return INLINE_CODE_RE.sub(lambda match: match.group(1), title)


def title_markup(title: str) -> str:
    """The title with inline code as real `<code>`, for the rendered heading.

    The page heading is the one place that *can* hold markup, and the section
    index already renders the same titles with `<code>` because there they pass
    through Markdown as link text. Rendering the heading as plain text was the
    inconsistency: one title, formatted in the list and raw on its own page.
    """
    parts: list[str] = []
    position = 0
    for match in INLINE_CODE_RE.finditer(title):
        parts.append(escape(title[position : match.start()]))
        parts.append(f"<code>{escape(match.group(1))}</code>")
        position = match.end()
    parts.append(escape(title[position:]))
    return "".join(parts)


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
    frontmatter only, per meta/anki.md's "Рендер Sources" - and per site.md's rule
    that templates carry no bare English/Ukrainian string, only vocabulary keys.
    Adding those fields here would mean inventing new UI strings with no entry in
    meta/vocabulary.yml to localise them.
    """
    if not sources:
        return ""
    items = [
        f'<li id="{source_anchor(source.source_id)}">'
        f'<a href="{escape(str(source.url), quote=True)}">{escape(source.title)}</a></li>'
        for source in sources
    ]
    return '<ol class="iqa-sources">\n' + "\n".join(items) + "\n</ol>"


def source_anchor(source_id: str) -> str:
    """The id a citation superscript links to, inside the `Sources` list."""
    return f"source-{source_id}"


def replace_citations(text: str, order: dict[str, int]) -> str:
    """`[^source-id]` -> a superscript link into the `Sources` list.

    This replaces Markdown footnotes. Emitting footnote definitions made the
    renderer append its own footnote block *below* the `Sources` section, so
    every cited source appeared twice on the page - and the two lists were not
    even the same, because a footnote block can only show sources that happen to
    be cited. One list that is both the provenance list and the citation target
    shows each source once and still shows the uncited ones.

    The number is the source's position in the question's own `sources`, so it
    matches the list a reader scrolls to and stays the same on both language
    pages, `sources` being parity-checked.
    """

    def replace(match: re.Match[str]) -> str:
        source_id = match.group(1)
        number = order.get(source_id)
        if number is None:
            raise ValueError(f"citation `[^{source_id}]` has no matching source")
        return f'<sup class="iqa-cite"><a href="#{source_anchor(source_id)}">{number}</a></sup>'

    return CITATION_RE.sub(replace, text)


def is_unwritten(content: str) -> bool:
    """Whether a section body is the `TODO` placeholder rather than written text."""
    return content.strip() == "TODO"


def render_section(
    section: ParsedSection,
    language: Language,
    vocabulary: dict[str, Any],
    known_ids: set[str],
    base: str,
    citations: dict[str, int],
) -> str:
    heading = section_label(vocabulary, section.heading, language)

    def body(text: str) -> str:
        return replace_citations(replace_qids(text, known_ids, base, language), citations)

    if section.subsections:
        parts = [f"## {heading}"]
        for subsection in section.subsections:
            sub_heading = subsection_label(vocabulary, subsection.heading, language)
            parts.append(f"### {sub_heading}\n\n{body(subsection.content)}")
        return "\n\n".join(parts)
    return f"## {heading}\n\n{body(section.content)}"


def render_body(question: Question, vocabulary: dict[str, Any], known_ids: set[str], base: str) -> str:
    citations = {
        source.source_id: number
        for number, source in enumerate(question.frontmatter.sources, 1)
    }
    rendered_sections: list[str] = []
    for section in question.body.sections:
        # An unwritten section is not rendered at all. The skeleton keeps the
        # heading in `content/` because the contract requires it, but a reader
        # gains nothing from four identical "not written yet" notices on one page
        # - 224 of 401 pages carried four or more. The gaps are reported as data,
        # in `dist/export/progress.{json,csv}` and on `/status/`, not as noise on
        # every page.
        if is_unwritten(section.content) and not section.subsections:
            continue
        if section.heading == SectionName.SOURCES.value:
            heading = section_label(vocabulary, section.heading, question.language)
            sources_markdown = render_sources(question.frontmatter.sources)
            rendered_sections.append(f"## {heading}\n\n{sources_markdown}".rstrip())
        else:
            rendered_sections.append(
                render_section(
                    section, question.language, vocabulary, known_ids, base, citations
                )
            )
    return "\n\n".join(rendered_sections).strip() + "\n"


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

    completeness = decision.completeness.value
    computed: dict[str, Any] = {
        "title": title_text(question.frontmatter.title),
        "title_html": title_markup(question.frontmatter.title),
        "slug": route_slug,
        "canonical": canonical,
        "source_path": source_label,
        "question_id": question_id,
        "language": language.value,
        "completeness": completeness,
    }
    variant = COMPLETENESS_BADGE_VARIANT.get(completeness)
    if page_mode is PageMode.PAGE and variant is not None:
        computed["sidebar"] = {
            "badge": {
                "text": completeness_label(vocabulary, completeness, language),
                "variant": variant,
            }
        }
    rendered = f"---\n{_frontmatter_yaml(question, computed)}\n---\n\n{body_markdown}"

    destination = output_root / language.value / "q" / question_id / f"{file_slug}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8", newline="\n")
    return MirroredPage(
        language=language.value,
        question_id=question_id,
        title=question.frontmatter.title,
        track=question.frontmatter.track,
        section=question.frontmatter.section,
        route_slug=route_slug,
        completeness=completeness,
    )


def remove_tree(path: Path) -> None:
    """Delete a generated tree, retrying past the transient locks Windows hands out.

    On Windows an indexer, an editor or an antivirus scanner can hold a handle on a
    file inside the freshly written mirror, and `shutil.rmtree` then fails with
    WinError 5 even though the same delete succeeds a moment later. That aborts the
    build for a reason that has nothing to do with the content, and it happened on
    three separate occasions here. Clearing the read-only bit and retrying a few
    times turns it back into what it is: noise.
    """
    def on_error(func, target, _exc):
        os.chmod(target, stat.S_IWRITE)
        func(target)

    for attempt in range(5):
        try:
            shutil.rmtree(path, onexc=on_error)
            return
        except OSError:
            if attempt == 4:
                raise
            time.sleep(0.3)


def swap_tree(temporary: Path, output: Path) -> None:
    """Move the freshly written tree into place, retrying past the same Windows locks.

    `remove_tree` above already survives a handle held on the mirror being deleted.
    The rename that follows it needs the same treatment and did not have it: a watcher
    that opened one of the 800-odd files this run just wrote makes `os.replace` fail
    with WinError 5 on the directory itself, with an empty destination and nothing
    wrong with the content. Measured here, not assumed - it is reproducible on this
    machine and it aborted the build twice in a row.
    """
    for attempt in range(5):
        try:
            os.replace(temporary, output)
            return
        except OSError:
            if attempt == 4:
                raise
            time.sleep(0.3)


def _nav_label(vocabulary: dict[str, Any], table: str, key: str, language: Language) -> str:
    return _label(vocabulary.get(table) or {}, key, language, what=table.rstrip("s"))


def site_label(vocabulary: dict[str, Any], key: str, language: Language) -> str:
    return _label(vocabulary.get("site_labels") or {}, key, language, what="site label")


def _index_page(title: str, links: list[str], empty_notice: str) -> str:
    """An index page: frontmatter title plus a link list, or an honest notice."""
    body = links or [empty_notice]
    return "\n".join(
        [
            "---",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            "---",
            "",
            *body,
            "",
        ]
    )


def navigation_pages(
    output_root: Path,
    pages: list[MirroredPage],
    base: str,
    vocabulary: dict[str, Any],
    taxonomy: list[tuple[str, list[str]]],
) -> list[list[NavigationPage]]:
    """Return complete, locale-isolated reading orders for footer pagination."""
    languages = sorted({page.language for page in pages})
    by_key: dict[tuple[str, str, str], list[MirroredPage]] = {}
    for page in pages:
        by_key.setdefault((page.language, page.track, page.section), []).append(page)

    orders: list[list[NavigationPage]] = []
    for language in languages:
        lang = Language(language)
        order = [
            NavigationPage(
                output_root / language / "index.md",
                f"{base}/{language}/",
                site_label(vocabulary, "home_title", lang),
            )
        ]
        for track, sections in taxonomy:
            populated = [
                section for section in sections if by_key.get((language, track, section))
            ]
            if not populated:
                continue
            order.append(
                NavigationPage(
                    output_root / language / track / "index.md",
                    f"{base}/{language}/{track}/",
                    _nav_label(vocabulary, "track_labels", track, lang),
                )
            )
            for section in populated:
                section_label_text = _nav_label(
                    vocabulary, "section_labels_nav", f"{track}/{section}", lang
                )
                order.append(
                    NavigationPage(
                        output_root / language / track / section / "index.md",
                        f"{base}/{language}/{track}/{section}/",
                        section_label_text,
                    )
                )
                for page in sorted(
                    by_key[(language, track, section)], key=lambda item: item.title
                ):
                    order.append(
                        NavigationPage(
                            output_root / f"{page.route_slug}.md",
                            f"{base}/{page.route_slug}/",
                            title_text(page.title),
                        )
                    )
        orders.append(order)
    return orders


def add_pagination(orders: list[list[NavigationPage]]) -> None:
    """Write explicit prev/next links because question pages stay out of the sidebar."""
    for order in orders:
        for index, page in enumerate(order):
            previous = order[index - 1] if index else None
            following = order[index + 1] if index + 1 < len(order) else None
            lines: list[str] = []
            if previous:
                lines.extend(
                    [
                        "prev:",
                        f"  label: {json.dumps(previous.label, ensure_ascii=False)}",
                        f"  link: {json.dumps(previous.href, ensure_ascii=False)}",
                    ]
                )
            if following:
                lines.extend(
                    [
                        "next:",
                        f"  label: {json.dumps(following.label, ensure_ascii=False)}",
                        f"  link: {json.dumps(following.href, ensure_ascii=False)}",
                    ]
                )
            text = page.source_path.read_text(encoding="utf-8")
            frontmatter_end = text.find("\n---\n", 4)
            if frontmatter_end < 0:
                raise ValueError(f"generated page has no closing frontmatter: {page.source_path}")
            insertion = "\n".join(lines)
            if insertion:
                insertion = "\n" + insertion
            page.source_path.write_text(
                text[:frontmatter_end] + insertion + text[frontmatter_end:],
                encoding="utf-8",
                newline="\n",
            )


def write_navigation(
    output_root: Path,
    pages: list[MirroredPage],
    base: str,
    vocabulary: dict[str, Any],
    taxonomy: list[tuple[str, list[str]]],
) -> list[dict[str, Any]]:
    """Write the home, track and section index pages; return the sidebar tree.

    Replaces the flat "every question as one bullet" locale index. That page was
    the whole of the site's navigation, and Starlight, given no `sidebar` of its
    own, autogenerated a menu from the mirror's directory layout - which is
    `{lang}/q/{id}/{slug}`, so the menu read `q` -> `cs-algo-0001` -> title.

    The shape here is the taxonomy instead: track, then section, then the
    questions listed on the section's own page. Order is `meta/taxonomy.md`'s
    document order, never alphabetical, because that file is where the intended
    reading order is declared.
    """
    languages = sorted({page.language for page in pages})
    by_key: dict[tuple[str, str, str], list[MirroredPage]] = {}
    for page in pages:
        by_key.setdefault((page.language, page.track, page.section), []).append(page)

    sidebar: list[dict[str, Any]] = []
    for track, sections in taxonomy:
        live_sections = [
            section
            for section in sections
            if any((language, track, section) in by_key for language in languages)
        ]
        if not live_sections:
            continue

        items: list[dict[str, Any]] = [{"slug": track}]
        for section in live_sections:
            items.append({"slug": f"{track}/{section}"})
        sidebar.append(
            {
                "label": _nav_label(vocabulary, "track_labels", track, Language.EN),
                "translations": {
                    language: _nav_label(vocabulary, "track_labels", track, Language(language))
                    for language in languages
                    if language != Language.EN.value
                },
                "collapsed": True,
                "items": items,
            }
        )

        for language in languages:
            lang = Language(language)
            empty = site_label(vocabulary, "index_no_questions", lang)

            section_links: list[str] = []
            for section in live_sections:
                entries = sorted(
                    by_key.get((language, track, section), ()), key=lambda page: page.title
                )
                if not entries:
                    continue
                label = _nav_label(
                    vocabulary, "section_labels_nav", f"{track}/{section}", lang
                )
                section_links.append(f"- [{label}]({base}/{language}/{track}/{section}/)")
                question_links = [
                    f"- [{page.title}]({base}/{language}/q/{page.question_id}/)"
                    for page in entries
                ]
                destination = output_root / language / track / section / "index.md"
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(
                    _index_page(label, question_links, empty), encoding="utf-8", newline="\n"
                )

            track_label = _nav_label(vocabulary, "track_labels", track, lang)
            destination = output_root / language / track / "index.md"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(
                _index_page(track_label, section_links, empty), encoding="utf-8", newline="\n"
            )

    for language in languages:
        lang = Language(language)
        track_links = [
            f"- [{_nav_label(vocabulary, 'track_labels', group['items'][0]['slug'], lang)}]"
            f"({base}/{language}/{group['items'][0]['slug']}/)"
            for group in sidebar
        ]
        home = "\n".join(
            [
                "---",
                f"title: {json.dumps(site_label(vocabulary, 'home_title', lang), ensure_ascii=False)}",
                "description: "
                f"{json.dumps(site_label(vocabulary, 'home_description', lang), ensure_ascii=False)}",
                "home_page: true",
                "---",
                "",
                f"## {site_label(vocabulary, 'home_heading', lang)}",
                "",
                site_label(vocabulary, "home_description", lang),
                "",
                f"{site_label(vocabulary, 'home_repository', lang)}: "
                "[GitHub](https://github.com/bogdan-kovalchuk/interview-qa)",
                "",
                f"### {site_label(vocabulary, 'home_contents', lang)}",
                "",
                *(track_links or [site_label(vocabulary, "index_no_questions", lang)]),
                "",
            ]
        )
        destination = output_root / language / "index.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(home, encoding="utf-8", newline="\n")

    return sidebar


def generate(
    source: Path,
    output: Path,
    base: str,
    *,
    preview: bool = False,
    root: Path | None = None,
    sidebar_out: Path | None = None,
) -> int:
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
        mirrored: list[MirroredPage] = []
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
        taxonomy = ordered_tracks_and_sections(root / "meta" / "taxonomy.md")
        sidebar = write_navigation(temporary, mirrored, base, vocabulary, taxonomy)
        add_pagination(navigation_pages(temporary, mirrored, base, vocabulary, taxonomy))
        if output.exists():
            remove_tree(output)
        swap_tree(temporary, output)
    finally:
        if temporary.exists():
            remove_tree(temporary)

    if sidebar_out is not None:
        # Written after the swap, and outside the docs tree: it is configuration
        # for astro.config.mjs, not content, and it must not exist unless the
        # mirror it describes was actually put in place.
        sidebar_out.parent.mkdir(parents=True, exist_ok=True)
        sidebar_out.write_text(
            json.dumps(sidebar, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    return len(mirrored)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("content"))
    parser.add_argument("--out", type=Path, default=Path("site/src/content/docs"))
    parser.add_argument("--base", default="/interview-qa")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--sidebar-out",
        type=Path,
        default=None,
        help="where to write the generated Starlight sidebar "
        "(default: <root>/site/src/generated/sidebar.json)",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="include draft/review questions, per the lifecycle table's preview column",
    )
    args = parser.parse_args()

    try:
        sidebar_out = args.sidebar_out or (
            args.root / "site" / "src" / "generated" / "sidebar.json"
        )
        count = generate(
            args.source,
            args.out,
            args.base,
            preview=args.preview,
            root=args.root,
            sidebar_out=sidebar_out,
        )
    except (OSError, ValueError) as error:
        parser.error(str(error))
    mode = "preview" if args.preview else "production"
    print(f"Mirrored {count} question pages ({mode}) into {args.out.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
