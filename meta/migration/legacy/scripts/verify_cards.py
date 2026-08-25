#!/usr/bin/env python3
"""Validate Anki TSV files used by this project."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


EXPECTED_HEADER = [
    "#separator:tab",
    "#html:true",
    "#deck:Python Interview Questions",
    "#notetype:Python Interview Basic",
    "#tags column:3",
]

ALLOWED = {
    "type::": {"Definition", "Mechanism", "Contrast", "Code", "Trap", "Scenario"},
    "level::": {"Junior", "Middle", "Senior"},
    "scope::": {"Core", "Overview"},
    "runtime::": {"CPython"},
    "version::": {"Py3_12", "Py3_13", "Py3_14", "Py3_15_preview"},
    "source::": {"PythonDocs", "PEP", "Community", "OfficialDocs"},
    "review::": {"NeedsFactCheck"},
    "stage::": {"FrontOnly"},
    "gil::": {"Enabled", "FreeThreaded"},
}

REQUIRED_PREFIXES = ("topic::", "type::", "level::", "scope::")
KNOWN_NAMESPACES = {
    "topic",
    "type",
    "level",
    "scope",
    "runtime",
    "version",
    "source",
    "review",
    "stage",
    "card",
    "ref",
    "gil",
}
SINGLE_VALUE_NAMESPACES = {
    "topic",
    "type",
    "level",
    "scope",
    "runtime",
    "version",
    "review",
    "stage",
    "card",
    "ref",
    "gil",
}
TAG_RE = re.compile(r"^[A-Za-z0-9_]+(?:::[A-Za-z0-9_]+)*$")
FRONT_CARD_ID_RE = re.compile(r"^card::PYI_[0-9]{2}_[0-9]{3}$")
HTML_TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")
CODE_FRAGMENT_RE = re.compile(r"<code(?:\s[^>]*)?>(.*?)</code>", re.IGNORECASE | re.DOTALL)
RAW_AMPERSAND_RE = re.compile(
    r"&(?!#\d+;|#x[0-9A-Fa-f]+;|amp;|lt;|gt;|quot;|apos;|nbsp;)"
)
SOURCE_LINK_RE = re.compile(
    r'<div\s+class=["\']source["\'][^>]*>.*?'
    r'<a\s+href=["\']https://[^"\']+["\'][^>]*>',
    re.IGNORECASE | re.DOTALL,
)
ALLOWED_HTML_TAGS = {"code", "pre", "span", "br", "div", "a"}
VOID_HTML_TAGS = {"br"}
ALLOWED_ENTITIES = {"amp", "lt", "gt", "quot", "apos", "nbsp"}


def load_topic_specs(project_root: Path) -> dict[str, dict[str, str]]:
    manifest = project_root / "authoring" / "manifest.json"
    if not manifest.exists():
        raise FileNotFoundError(f"Project manifest not found: {manifest}")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return {
        f"{item['id']}_{item['slug']}.txt": {
            "id": item["id"],
            "topic_tag": f"topic::{item['id']}_{item['slug']}",
            "scope_tag": f"scope::{item['scope']}",
        }
        for item in data["topics"]
    }


class StrictHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in ALLOWED_HTML_TAGS:
            self.errors.append(f"unsupported HTML tag <{tag}>")
            return
        attr_map = dict(attrs)
        allowed_attrs = {
            "code": set(),
            "pre": {"class"},
            "span": {"class"},
            "br": set(),
            "div": {"class"},
            "a": {"href"},
        }[tag]
        unexpected = sorted(set(attr_map) - allowed_attrs)
        if unexpected:
            self.errors.append(f"unsupported attributes on <{tag}>: {', '.join(unexpected)}")
        if tag == "pre" and attr_map.get("class") != "code-block":
            self.errors.append('<pre> requires class="code-block"')
        if tag == "span" and attr_map.get("class") not in {"key", "warn"}:
            self.errors.append('<span> class must be "key" or "warn"')
        if tag == "div" and attr_map.get("class") != "source":
            self.errors.append('<div> requires class="source"')
        if tag == "a":
            href = attr_map.get("href") or ""
            parsed = urlparse(href)
            if parsed.scheme != "https" or not parsed.netloc:
                self.errors.append("<a> href must be an absolute HTTPS URL")
        if tag not in VOID_HTML_TAGS:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_HTML_TAGS and self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_HTML_TAGS:
            self.errors.append(f"void HTML tag </{tag}> must not be closed")
        elif not self.stack or self.stack[-1] != tag:
            expected = self.stack[-1] if self.stack else "none"
            self.errors.append(f"mismatched </{tag}>; expected </{expected}>")
        else:
            self.stack.pop()

    def handle_entityref(self, name: str) -> None:
        if name not in ALLOWED_ENTITIES:
            self.errors.append(f"unsupported HTML entity &{name};")

    def close(self) -> None:
        super().close()
        if self.stack:
            self.errors.append(f"unclosed HTML tags: {', '.join(self.stack)}")


def validate_html_fragment(value: str) -> list[str]:
    parser = StrictHTMLParser()
    parser.feed(value)
    parser.close()
    errors = list(parser.errors)
    if RAW_AMPERSAND_RE.search(value):
        errors.append("raw ampersand must be escaped")
    for fragment in CODE_FRAGMENT_RE.findall(value):
        code_text = re.sub(r"<br\s*/?>", "", fragment, flags=re.IGNORECASE)
        code_text = re.sub(r"&(?:#\d+|#x[0-9A-Fa-f]+|amp|lt|gt|quot|apos|nbsp);", "", code_text)
        if "<" in code_text or ">" in code_text:
            errors.append("raw < or > inside <code> must be escaped")
    return errors


def normalized_front(front: str) -> str:
    text = HTML_TAG_RE.sub(" ", front)
    text = html.unescape(text)
    return SPACE_RE.sub(" ", text).strip().casefold()


def collect_files(targets: list[Path]) -> list[Path]:
    result: set[Path] = set()
    for target in targets:
        if target.is_file() and target.suffix.lower() == ".txt":
            result.add(target.resolve())
        elif target.is_dir():
            result.update(path.resolve() for path in target.rglob("*.txt"))
    return sorted(result)


def validate_file(
    path: Path,
    topic_specs: dict[str, dict[str, str]],
    seen_fronts: dict[str, tuple[Path, int]],
    front_only: bool = False,
) -> tuple[int, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        warnings.append(f"{path}: UTF-8 BOM detected; plain UTF-8 is preferred")

    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return 0, [f"{path}: not valid UTF-8: {exc}"], warnings

    lines = text.splitlines()
    if lines[:5] != EXPECTED_HEADER:
        errors.append(f"{path}: first five lines do not match the required header")
        return 0, errors, warnings

    expected = topic_specs.get(path.name)
    project_card_file = path.parent.name.casefold() == "cards"
    if project_card_file and expected is None:
        errors.append(f"{path}: filename is not declared in authoring/manifest.json")

    cards = 0
    for line_number, line in enumerate(lines[5:], start=6):
        if not line.strip():
            warnings.append(f"{path}:{line_number}: blank line ignored")
            continue

        if line.count("\t") != 2:
            errors.append(
                f"{path}:{line_number}: expected exactly 2 TABs, found {line.count(chr(9))}"
            )
            continue

        front, back, tags_field = line.split("\t")
        cards += 1
        if not front.strip() or not tags_field.strip():
            errors.append(f"{path}:{line_number}: Front and Tags must be non-empty")
            continue
        if front_only:
            if back.strip():
                errors.append(
                    f"{path}:{line_number}: Back must be empty in front-only mode"
                )
        elif not back.strip():
            errors.append(f"{path}:{line_number}: Back must be non-empty")
        elif "stage::FrontOnly" in tags_field.split():
            errors.append(
                f"{path}:{line_number}: stage::FrontOnly is not allowed once "
                "Back is filled"
            )

        for field_name, value in (("Front", front), ("Back", back)):
            for html_error in validate_html_fragment(value):
                errors.append(f"{path}:{line_number}: {field_name}: {html_error}")

        tags = tags_field.split()
        invalid_tags = [tag for tag in tags if not TAG_RE.fullmatch(tag)]
        if invalid_tags:
            errors.append(f"{path}:{line_number}: invalid tags: {', '.join(invalid_tags)}")
        unknown_namespaces = sorted(
            {
                tag.split("::", 1)[0]
                for tag in tags
                if "::" in tag and tag.split("::", 1)[0] not in KNOWN_NAMESPACES
            }
        )
        if unknown_namespaces:
            errors.append(
                f"{path}:{line_number}: unsupported tag namespaces: "
                f"{', '.join(unknown_namespaces)}"
            )
        for namespace in SINGLE_VALUE_NAMESPACES:
            matches = [tag for tag in tags if tag.startswith(f"{namespace}::")]
            if len(matches) > 1:
                errors.append(
                    f"{path}:{line_number}: expected at most one {namespace}:: tag, "
                    f"found {len(matches)}"
                )

        for prefix in REQUIRED_PREFIXES:
            matches = [tag for tag in tags if tag.startswith(prefix)]
            if len(matches) != 1:
                errors.append(
                    f"{path}:{line_number}: expected one {prefix} tag, found {len(matches)}"
                )

        if front_only:
            if tags.count("stage::FrontOnly") != 1:
                errors.append(
                    f"{path}:{line_number}: front-only card requires one stage::FrontOnly tag"
                )
            if "level::Junior" in tags:
                errors.append(
                    f"{path}:{line_number}: front-only interview bank must be Middle or Senior"
                )
            card_ids = [tag for tag in tags if tag.startswith("card::")]
            if len(card_ids) != 1 or not FRONT_CARD_ID_RE.fullmatch(card_ids[0]):
                errors.append(
                    f"{path}:{line_number}: expected one card::PYI_NN_NNN identifier"
                )

        for prefix, values in ALLOWED.items():
            for tag in (tag for tag in tags if tag.startswith(prefix)):
                value = tag[len(prefix) :]
                if value not in values:
                    errors.append(
                        f"{path}:{line_number}: unsupported {prefix} value {value!r}"
                    )

        topic_matches = [tag for tag in tags if tag.startswith("topic::")]
        known_topic_tags = {item["topic_tag"] for item in topic_specs.values()}
        if topic_matches and topic_specs and topic_matches[0] not in known_topic_tags:
            errors.append(f"{path}:{line_number}: unknown topic tag {topic_matches[0]!r}")
        if expected and topic_matches and topic_matches[0] != expected["topic_tag"]:
            errors.append(
                f"{path}:{line_number}: topic tag must be {expected['topic_tag']!r} "
                f"for this filename"
            )
        scope_matches = [tag for tag in tags if tag.startswith("scope::")]
        if expected and scope_matches and scope_matches[0] != expected["scope_tag"]:
            errors.append(
                f"{path}:{line_number}: scope tag must be {expected['scope_tag']!r} "
                f"for this topic"
            )
        card_ids = [tag for tag in tags if tag.startswith("card::")]
        if expected and card_ids and FRONT_CARD_ID_RE.fullmatch(card_ids[0]):
            if card_ids[0].split("_", 2)[1] != expected["id"]:
                errors.append(
                    f"{path}:{line_number}: card ID topic number must be {expected['id']}"
                )

        sensitive = any(
            tag.startswith(("runtime::", "version::", "gil::")) for tag in tags
        )
        if sensitive and not any(tag.startswith("source::") for tag in tags):
            errors.append(
                f"{path}:{line_number}: version/runtime-sensitive card requires source::*"
            )
        if sensitive and not front_only and not SOURCE_LINK_RE.search(back):
            errors.append(
                f"{path}:{line_number}: version/runtime-sensitive Back requires an "
                "HTTPS source link"
            )

        if project_card_file and "review::NeedsFactCheck" in tags:
            errors.append(f"{path}:{line_number}: package-source card still needs fact checking")

        norm = normalized_front(front)
        if norm in seen_fronts:
            other_path, other_line = seen_fronts[norm]
            errors.append(
                f"{path}:{line_number}: duplicate Front; first seen at {other_path}:{other_line}"
            )
        else:
            seen_fronts[norm] = (path, line_number)

        if len(normalized_front(front)) > 500:
            warnings.append(f"{path}:{line_number}: unusually long Front")
        if len(normalized_front(back)) > 2000:
            warnings.append(f"{path}:{line_number}: unusually long Back")

    if cards == 0:
        warnings.append(f"{path}: header-only file (0 cards)")
    return cards, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "targets",
        nargs="*",
        type=Path,
        default=[Path("cards")],
        help="TSV files or directories to scan (default: cards)",
    )
    parser.add_argument(
        "--front-only",
        action="store_true",
        help="require empty Back fields and stage::FrontOnly on Middle/Senior fronts",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    topic_specs = load_topic_specs(project_root)
    files = collect_files(args.targets)
    if not files:
        print("ERROR: no .txt files found", file=sys.stderr)
        return 2

    total_cards = 0
    all_errors: list[str] = []
    all_warnings: list[str] = []
    seen_fronts: dict[str, tuple[Path, int]] = {}
    for path in files:
        count, errors, warnings = validate_file(
            path, topic_specs, seen_fronts, front_only=args.front_only
        )
        total_cards += count
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    for warning in all_warnings:
        print(f"WARN: {warning}")
    for error in all_errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(
        f"Checked {len(files)} file(s), {total_cards} card(s), "
        f"{len(all_errors)} error(s), {len(all_warnings)} warning(s)."
    )
    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
