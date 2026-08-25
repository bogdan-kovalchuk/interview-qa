"""Verify the production Astro output for base-path, i18n, and permalink integrity."""

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


@dataclass
class Document:
    path: Path
    attributes: list[tuple[str, str, str]] = field(default_factory=list)
    canonicals: list[str] = field(default_factory=list)
    anchors: list[str] = field(default_factory=list)
    has_language_switcher: bool = False
    text: str = ""


class DocumentParser(HTMLParser):
    def __init__(self, document: Document) -> None:
        super().__init__(convert_charrefs=True)
        self.document = document

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        for attribute in ("href", "src"):
            if attribute in values:
                self.document.attributes.append((tag, attribute, values[attribute]))
        if tag == "a" and "href" in values:
            self.document.anchors.append(values["href"])
        if tag == "link" and "canonical" in values.get("rel", "").lower().split():
            self.document.canonicals.append(values.get("href", ""))
        if tag == "starlight-lang-select":
            self.document.has_language_switcher = True


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=Path("site/dist"))
    parser.add_argument("--base", default="/interview-qa/")
    parser.add_argument("--site-host", default="bogdan-kovalchuk.github.io")
    parser.add_argument("--locales", nargs="+", default=["en", "uk"])
    parser.add_argument("--metrics", type=Path, default=Path("site/.build-metrics.json"))
    args = parser.parse_args()

    dist = args.dist.resolve()
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

    question_ids = {question_id for _language, question_id in canonicals}
    for language in args.locales:
        for question_id in question_ids:
            key = (language, question_id)
            if key not in resolvers:
                failures.append(f"missing resolver page for {language}/{question_id}")
                continue
            if key not in canonicals:
                failures.append(f"missing canonical page for {language}/{question_id}")
                continue
            slug, _canonical_document = canonicals[key]
            expected_path = f"{base_prefix}{language}/q/{question_id}/{slug}/"
            resolver = resolvers[key]
            canonical_paths = [urlsplit(url).path for url in resolver.canonicals]
            if canonical_paths != [expected_path]:
                failures.append(
                    f"resolver canonical mismatch for {language}/{question_id}: {canonical_paths!r}"
                )
            if expected_path not in resolver.anchors:
                failures.append(f"resolver has no visible fallback link for {language}/{question_id}")
            if "window.location.replace" not in resolver.text:
                failures.append(f"resolver has no immediate client navigation for {language}/{question_id}")

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

    build_time = None
    if args.metrics.exists():
        metrics = json.loads(args.metrics.read_text(encoding="utf-8"))
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
