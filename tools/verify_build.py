"""Verify a production Astro build against the model, not against itself.

The previous version of this script derived its expectations from whatever
HTML happened to be sitting in ``site/dist`` - it could (and did) PASS against
a stale build made from content that no longer existed. This version reads
``content/`` through the same canonical model and lifecycle table the mirror
and the exporter use (``tools/iqa/model.py``, ``tools/iqa/lifecycle.py``), computes
the page set a correct production build must contain, and asserts the emitted
set matches it exactly - nothing missing, nothing left over from a previous run.

Run this after ``npm run build`` (``site/scripts/build.mjs``) - or invoke the
whole pipeline with ``python -m iqa build``, which runs this last.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

from iqa.export import canonical_path, group_by_id, read_all_questions, resolver_path
from iqa.lifecycle import PageMode, lifecycle_for


SOURCE_COMMENT = "generated from frontmatter"
RAW_CITATION_RE = re.compile(r"\[\^[a-zA-Z0-9][a-zA-Z0-9-]*\]")


@dataclass
class Document:
    path: Path
    attributes: list[tuple[str, str, str]] = field(default_factory=list)
    canonicals: list[str] = field(default_factory=list)
    alternates: dict[str, str] = field(default_factory=dict)  # hreflang -> href
    anchors: list[str] = field(default_factory=list)
    headings: list[str] = field(default_factory=list)
    has_language_switcher: bool = False
    text: str = ""


class DocumentParser(HTMLParser):
    def __init__(self, document: Document) -> None:
        super().__init__(convert_charrefs=True)
        self.document = document
        self._heading_depth = 0
        self._heading_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        for attribute in ("href", "src"):
            if attribute in values:
                self.document.attributes.append((tag, attribute, values[attribute]))
        if tag == "a" and "href" in values:
            self.document.anchors.append(values["href"])
        if tag == "link":
            rel_tokens = values.get("rel", "").lower().split()
            if "canonical" in rel_tokens:
                self.document.canonicals.append(values.get("href", ""))
            if "alternate" in rel_tokens and values.get("hreflang"):
                self.document.alternates[values["hreflang"]] = values.get("href", "")
        if tag == "starlight-lang-select":
            self.document.has_language_switcher = True
        if re.fullmatch(r"h[1-6]", tag):
            self._heading_depth += 1
            self._heading_buffer.append("")

    def handle_endtag(self, tag: str) -> None:
        if re.fullmatch(r"h[1-6]", tag) and self._heading_depth:
            self.document.headings.append(self._heading_buffer.pop().strip())
            self._heading_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._heading_depth:
            self._heading_buffer[-1] += data


def human_bytes(size: int) -> str:
    units = ("B", "KiB", "MiB", "GiB")
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}"
        value /= 1024
    raise AssertionError("unreachable")


def emitted_target(dist: Path, path: str, base_prefix: str) -> Path | None:
    if not path.startswith(base_prefix):
        return None
    relative = unquote(path[len(base_prefix) :]).lstrip("/")
    if not relative:
        return dist / "index.html"
    candidate = dist / Path(relative)
    if path.endswith("/"):
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    if candidate.is_file():
        return candidate
    return candidate / "index.html"


def internal_path(url: str, site_host: str) -> tuple[bool, str | None]:
    if not url or url.startswith("#"):
        return False, None
    split = urlsplit(url)
    if split.scheme in {"mailto", "tel", "data", "javascript"}:
        return False, None
    if split.scheme and split.scheme not in {"http", "https"}:
        return False, None
    if split.netloc and split.netloc != site_host:
        return False, None
    return True, split.path


def parse_documents(dist: Path) -> dict[Path, Document]:
    documents: dict[Path, Document] = {}
    for path in sorted(dist.rglob("*.html")):
        document = Document(path=path, text=path.read_text(encoding="utf-8"))
        DocumentParser(document).feed(document.text)
        documents[path] = document
    return documents


def expected_pages(
    content_root: Path, base: str
) -> tuple[dict[tuple[str, str], str], dict[tuple[str, str], str]]:
    """Return (canonical_paths, resolver_paths) keyed by (language, question_id).

    Only entries whose ``production_page`` lifecycle decision is ``page`` or
    ``tombstone`` are included - those are exactly the (language, id) pairs the
    mirror writes a file for and the site must therefore emit a page for.
    """
    questions = read_all_questions(content_root)
    grouped = group_by_id(questions)
    canonical: dict[tuple[str, str], str] = {}
    resolver: dict[tuple[str, str], str] = {}
    for question_id, by_language in grouped.items():
        for language, question in by_language.items():
            decision = lifecycle_for(question, language)
            if decision.production_page is PageMode.ABSENT:
                continue
            key = (language.value, question_id)
            canonical[key] = canonical_path(base, language, question_id, question.slug)
            resolver[key] = resolver_path(base, language, question_id)
    return canonical, resolver


def section_heading_leaks(vocabulary_path: Path) -> dict[str, str]:
    """English section-heading text that must never render on a `/uk/` page.

    Skips any section whose English and Ukrainian labels happen to be equal
    (none currently are, but a future one should not become a false positive).
    """
    import yaml

    vocabulary = yaml.safe_load(vocabulary_path.read_text(encoding="utf-8")) or {}
    leaks: dict[str, str] = {}
    for table_name in ("section_labels", "subsection_labels"):
        for _key, labels in (vocabulary.get(table_name) or {}).items():
            if not isinstance(labels, dict):
                continue
            en_label, uk_label = labels.get("en"), labels.get("uk")
            if en_label and uk_label and en_label != uk_label:
                leaks[en_label] = uk_label
    return leaks


def main() -> int:
    # Diagnostics can quote Ukrainian heading text; a Windows console defaults to
    # a codepage that cannot encode it, which must not crash the check itself.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--dist", type=Path, default=None)
    parser.add_argument("--base", default="/interview-qa")
    parser.add_argument("--site-host", default="bogdan-kovalchuk.github.io")
    parser.add_argument("--locales", nargs="+", default=["en", "uk"])
    parser.add_argument("--metrics", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    dist = (args.dist if args.dist is not None else root / "site" / "dist").resolve()
    metrics_path = (args.metrics if args.metrics is not None else root / "site" / ".build-metrics.json").resolve()
    base_prefix = "/" + args.base.strip("/") + "/"
    failures: list[str] = []
    if not dist.is_dir():
        print(f"FAIL: build output does not exist: {dist}")
        return 1

    documents = parse_documents(dist)
    all_files = [path for path in dist.rglob("*") if path.is_file()]
    total_size = sum(path.stat().st_size for path in all_files)
    peak_file = max(all_files, key=lambda path: path.stat().st_size)
    peak_size = peak_file.stat().st_size

    # --- expected page set, computed from the model, not from dist itself ---
    expected_canonical, expected_resolver = expected_pages(root / "content", args.base)

    resolver_pattern = re.compile(r"^(?P<lang>[^/]+)/q/(?P<id>[^/]+)/index\.html$")
    canonical_pattern = re.compile(r"^(?P<lang>[^/]+)/q/(?P<id>[^/]+)/(?P<slug>[^/]+)/index\.html$")
    resolvers: dict[tuple[str, str], Document] = {}
    canonicals: dict[tuple[str, str], tuple[str, Document]] = {}
    for path, document in documents.items():
        relative = path.relative_to(dist).as_posix()
        if match := resolver_pattern.match(relative):
            resolvers[(match.group("lang"), match.group("id"))] = document
        elif match := canonical_pattern.match(relative):
            canonicals[(match.group("lang"), match.group("id"))] = (match.group("slug"), document)

    actual_canonical_keys = set(canonicals)
    actual_resolver_keys = set(resolvers)
    expected_canonical_keys = set(expected_canonical)
    expected_resolver_keys = set(expected_resolver)

    for key in sorted(expected_canonical_keys - actual_canonical_keys):
        failures.append(f"expected canonical page for {key[0]}/{key[1]} was not emitted")
    for key in sorted(actual_canonical_keys - expected_canonical_keys):
        failures.append(
            f"emitted canonical page for {key[0]}/{key[1]} is not in the model's production set "
            "(stale mirror or dist?)"
        )
    for key in sorted(expected_resolver_keys - actual_resolver_keys):
        failures.append(f"expected resolver page for {key[0]}/{key[1]} was not emitted")
    for key in sorted(actual_resolver_keys - expected_resolver_keys):
        failures.append(
            f"emitted resolver page for {key[0]}/{key[1]} is not in the model's production set "
            "(stale mirror or dist?)"
        )

    for key, expected_url in expected_canonical.items():
        if key not in canonicals:
            continue
        slug, document = canonicals[key]
        actual_url = f"{base_prefix}{key[0]}/q/{key[1]}/{slug}/"
        if actual_url != expected_url:
            failures.append(
                f"canonical path for {key[0]}/{key[1]} is `{actual_url}`, model expects `{expected_url}`"
            )

    # --- link integrity (unchanged: base prefix, and every internal href/src resolves) ---
    checked_links = 0
    missing_targets: list[tuple[Path, str]] = []
    bad_base_links: list[tuple[Path, str]] = []
    for document in documents.values():
        for _tag, _attribute, url in document.attributes:
            is_internal, path = internal_path(url, args.site_host)
            if not is_internal or path is None:
                continue
            checked_links += 1
            if not path.startswith(base_prefix):
                bad_base_links.append((document.path, url))
                continue
            target = emitted_target(dist, path, base_prefix)
            if target is None or not target.exists():
                missing_targets.append((document.path, url))

    if bad_base_links:
        failures.extend(
            f"internal URL lacks {base_prefix}: {source.relative_to(dist)} -> {url}"
            for source, url in bad_base_links
        )
    if missing_targets:
        failures.extend(
            f"internal URL has no emitted target: {source.relative_to(dist)} -> {url}"
            for source, url in missing_targets
        )

    locale_page_counts = {
        locale: sum(1 for path in documents if path.relative_to(dist).parts[0] == locale)
        for locale in args.locales
    }
    for locale, count in locale_page_counts.items():
        if count == 0:
            failures.append(f"locale emitted no HTML pages: {locale}")

    switcher_pages = [path for path, doc in documents.items() if doc.has_language_switcher]
    if not switcher_pages:
        failures.append("no Starlight language switcher found")

    for key in expected_canonical_keys & actual_canonical_keys:
        document = resolvers.get(key)
        if document is None:
            continue
        expected_path = expected_canonical[key]
        canonical_hrefs = [urlsplit(url).path for url in document.canonicals]
        if canonical_hrefs != [expected_path]:
            failures.append(f"resolver canonical mismatch for {key[0]}/{key[1]}: {canonical_hrefs!r}")
        if expected_path not in document.anchors:
            failures.append(f"resolver has no visible fallback link for {key[0]}/{key[1]}")
        if "window.location.replace" not in document.text:
            failures.append(f"resolver has no immediate client navigation for {key[0]}/{key[1]}")

    qid_crosslinks = 0
    qid_crosslinks_by_locale: Counter[str] = Counter()
    for (language, source_id), (_slug, document) in canonicals.items():
        for href in document.anchors:
            path = urlsplit(href).path
            match = re.fullmatch(
                re.escape(base_prefix) + rf"{re.escape(language)}/q/(?P<id>[^/]+)/", path
            )
            if match and match.group("id") != source_id:
                qid_crosslinks += 1
                qid_crosslinks_by_locale[language] += 1
    for locale in args.locales:
        if qid_crosslinks_by_locale[locale] == 0:
            failures.append(f"no resolved qid cross-link found in canonical {locale} pages")

    # --- new checks: raw citation tokens and the un-rendered Sources placeholder ---
    for path, document in documents.items():
        if RAW_CITATION_RE.search(document.text):
            failures.append(f"raw citation token `[^...]` leaked into HTML: {path.relative_to(dist)}")
        if SOURCE_COMMENT in document.text:
            failures.append(f"un-rendered Sources placeholder leaked into HTML: {path.relative_to(dist)}")

    # --- new check: no English section heading text on a /uk/ page ---
    leak_labels = section_heading_leaks(root / "meta" / "vocabulary.yml")
    for path, document in documents.items():
        relative = path.relative_to(dist).as_posix()
        if not relative.startswith("uk/"):
            continue
        for heading in document.headings:
            if heading in leak_labels:
                failures.append(
                    f"English heading `{heading}` (expected `{leak_labels[heading]}`) "
                    f"on Ukrainian page: {relative}"
                )

    # --- new check: hreflang alternates on every question page ---
    languages_by_id: dict[str, set[str]] = {}
    for language, question_id in expected_canonical_keys & actual_canonical_keys:
        languages_by_id.setdefault(question_id, set()).add(language)
    for (language, question_id), (_slug, document) in canonicals.items():
        if question_id not in languages_by_id:
            continue
        for other_language in languages_by_id[question_id]:
            if other_language not in document.alternates:
                failures.append(
                    f"canonical page {language}/{question_id} is missing hreflang=\"{other_language}\""
                )
                continue
            other_slug = canonicals.get((other_language, question_id), (None, None))[0]
            if other_slug is None:
                continue
            expected_href = f"https://{args.site_host}{base_prefix}{other_language}/q/{question_id}/{other_slug}/"
            if document.alternates[other_language] != expected_href:
                failures.append(
                    f"canonical page {language}/{question_id} hreflang=\"{other_language}\" "
                    f"points to `{document.alternates[other_language]}`, expected `{expected_href}`"
                )

    # --- new checks: site root, robots.txt, sitemap ---
    root_index = dist / "index.html"
    if not root_index.is_file():
        failures.append("site root index.html was not emitted")
    else:
        root_document = documents.get(root_index)
        if root_document is None:
            root_document = Document(path=root_index, text=root_index.read_text(encoding="utf-8"))
            DocumentParser(root_document).feed(root_document.text)
        target = f"{base_prefix}en/"
        if "window.location.replace" not in root_document.text:
            failures.append("site root has no immediate client navigation to the default locale")
        if target not in root_document.anchors:
            failures.append(f"site root has no visible fallback link to `{target}`")
        root_canonicals = [urlsplit(url).path for url in root_document.canonicals]
        if root_canonicals != [target]:
            failures.append(f"site root canonical mismatch: {root_canonicals!r}, expected [{target!r}]")

    robots_path = dist / "robots.txt"
    if not robots_path.is_file():
        failures.append("robots.txt was not emitted")

    sitemap_candidates = [dist / "sitemap.xml", dist / "sitemap-index.xml"]
    if not any(candidate.is_file() for candidate in sitemap_candidates):
        failures.append("no sitemap.xml or sitemap-index.xml was emitted")

    build_time = None
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        build_time = metrics.get("build_seconds")
        if metrics.get("exit_code") != 0:
            failures.append(f"recorded build exit code is {metrics.get('exit_code')}")

    print("Production build verification")
    print(f"Build time: {build_time:.3f} s" if isinstance(build_time, (int, float)) else "Build time: unavailable")
    print(f"Page count: {len(documents)}")
    print("Locale pages: " + ", ".join(f"{key}={value}" for key, value in locale_page_counts.items()))
    print(f"Output files: {len(all_files)}")
    print(f"Total output size: {human_bytes(total_size)} ({total_size} bytes)")
    print(
        f"Peak output file: {peak_file.relative_to(dist).as_posix()} "
        f"at {human_bytes(peak_size)} ({peak_size} bytes)"
    )
    print(f"Internal href/src checked: {checked_links}")
    print(f"Expected canonical pages (from the model): {len(expected_canonical_keys)}")
    print(f"Resolver pages: {len(resolvers)}")
    print(f"Canonical question pages: {len(canonicals)}")
    print(f"Resolved qid cross-links: {qid_crosslinks}")
    print(f"Language-switcher pages: {len(switcher_pages)}")
    print(f"Failures: {len(failures)}")
    for failure in failures:
        print(f"FAIL: {failure}")

    if failures:
        return 1
    print("PASS: all production build checks succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
