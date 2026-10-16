"""Canonical question model and Markdown parser.

This module owns the frontmatter shape and the body section sequence. Consumers
must import those definitions instead of copying them.
"""

from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
import json
from pathlib import Path
import re
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, field_validator
import yaml


KEBAB_CASE = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
SECTION_PATH = r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*$"
QUESTION_ID = (
    r"^(?:py|emb)-"
    r"[a-z0-9]{3,8}-[0-9]{4}$"
)

QuestionIdValue = Annotated[str, StringConstraints(pattern=QUESTION_ID)]


class Language(str, Enum):
    EN = "en"
    UK = "uk"


class SectionName(str, Enum):
    QUESTION_CODE = "Question code"
    SHORT_ANSWER = "Short answer"
    DETAILED_EXPLANATION = "Detailed explanation"


# The whole body: an optional code block that belongs to the question, then the
# two answers. Nothing about the sequence depends on the question.
SECTION_SEQUENCE: tuple[SectionName, ...] = tuple(SectionName)
REQUIRED_SECTIONS: tuple[SectionName, ...] = (
    SectionName.SHORT_ANSWER,
    SectionName.DETAILED_EXPLANATION,
)
OPTIONAL_SECTIONS = frozenset({SectionName.QUESTION_CODE})


class CanonicalModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Source(CanonicalModel):
    source_id: str = Field(pattern=KEBAB_CASE)
    title: str = Field(min_length=1)
    url: HttpUrl


class QuestionFrontmatter(CanonicalModel):
    id: QuestionIdValue
    title: str = Field(min_length=1)
    track: str = Field(pattern=KEBAB_CASE)
    section: str = Field(pattern=SECTION_PATH)
    sources: tuple[Source, ...] = ()

    @field_validator("sources")
    @classmethod
    def source_ids_are_unique(cls, value: tuple[Source, ...]) -> tuple[Source, ...]:
        source_ids = [source.source_id for source in value]
        if len(source_ids) != len(set(source_ids)):
            raise ValueError("source_id must be unique within a question")
        return value


class ParsedSubsection(CanonicalModel):
    heading: str
    content: str


class ParsedSection(CanonicalModel):
    heading: str
    content: str
    subsections: tuple[ParsedSubsection, ...] = ()


class ParsedBody(CanonicalModel):
    raw: str
    preamble: str
    sections: tuple[ParsedSection, ...]


class Question(CanonicalModel):
    language: Language
    slug: str = Field(pattern=KEBAB_CASE)
    source_path: str
    frontmatter: QuestionFrontmatter
    body: ParsedBody

    def section(self, name: SectionName | str) -> ParsedSection | None:
        wanted = name.value if isinstance(name, SectionName) else name
        return next((section for section in self.body.sections if section.heading == wanted), None)


class DuplicateKeyError(ValueError):
    """Raised when YAML contains a mapping key more than once."""


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise DuplicateKeyError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)

FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<header>.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL
)
SECTION_RE = re.compile(r"(?m)^## (?P<heading>[^\r\n]+)\r?\n")
SUBSECTION_RE = re.compile(r"(?m)^### (?P<heading>[^\r\n]+)\r?\n")
CODE_FENCE_RE = re.compile(r"(?ms)^```[^\r\n]*\r?\n.*?^```[ \t]*$")


def code_spans(text: str) -> list[tuple[int, int]]:
    """(start, end) of every fenced code block, so a `#` line inside one is code.

    A Markdown heading and a shell or Python comment are the same characters at
    the start of a line. Without this, `# note` inside a fence reads as a level-1
    heading, and - worse - `## note` inside a fence becomes a whole phantom
    section in the parsed document. Both were real: the second silently changed
    the section sequence a question is validated and rendered against.
    """
    return [(match.start(), match.end()) for match in CODE_FENCE_RE.finditer(text)]


def outside_code(position: int, spans: list[tuple[int, int]]) -> bool:
    return not any(start <= position < end for start, end in spans)


def load_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    loaded = yaml.load(match.group("header"), Loader=UniqueKeyLoader)
    if not isinstance(loaded, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return loaded, text[match.end() :]


def parse_body(body: str) -> ParsedBody:
    spans = code_spans(body)
    matches = [match for match in SECTION_RE.finditer(body) if outside_code(match.start(), spans)]
    preamble = body[: matches[0].start()] if matches else body
    sections: list[ParsedSection] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        content = body[match.end() : end].rstrip("\r\n")
        content_spans = code_spans(content)
        subsection_matches = [
            sub
            for sub in SUBSECTION_RE.finditer(content)
            if outside_code(sub.start(), content_spans)
        ]
        subsections: list[ParsedSubsection] = []
        for sub_index, sub_match in enumerate(subsection_matches):
            sub_end = (
                subsection_matches[sub_index + 1].start()
                if sub_index + 1 < len(subsection_matches)
                else len(content)
            )
            subsections.append(
                ParsedSubsection(
                    heading=sub_match.group("heading").strip(),
                    content=content[sub_match.end() : sub_end].strip(),
                )
            )
        sections.append(
            ParsedSection(
                heading=match.group("heading").strip(),
                content=content.strip(),
                subsections=tuple(subsections),
            )
        )
    return ParsedBody(raw=body, preamble=preamble.strip(), sections=tuple(sections))


def parse_question_text(text: str, *, language: str, slug: str, source_path: str) -> Question:
    frontmatter, body = load_frontmatter(text)
    return Question.model_validate(
        {
            "language": language,
            "slug": slug,
            "source_path": source_path,
            "frontmatter": frontmatter,
            "body": parse_body(body),
        }
    )


def parse_question_file(path: Path, *, content_root: Path) -> Question:
    relative = path.relative_to(content_root)
    if len(relative.parts) < 4:
        raise ValueError("question path must be content/{lang}/{track}/.../{slug}.md")
    return parse_question_text(
        path.read_text(encoding="utf-8"),
        language=relative.parts[0],
        slug=path.stem,
        source_path=relative.as_posix(),
    )


def expected_sections(present_optional: Iterable[SectionName] = ()) -> tuple[SectionName, ...]:
    present = frozenset(present_optional)
    return tuple(
        section
        for section in SECTION_SEQUENCE
        if section not in OPTIONAL_SECTIONS or section in present
    )


def is_written(question: Question, name: SectionName) -> bool:
    """Whether a section holds real text rather than the `TODO` placeholder."""
    section = question.section(name)
    return section is not None and section.content.strip() != "TODO"


def question_schema() -> dict[str, Any]:
    schema = Question.model_json_schema()
    schema["$id"] = "https://interview-qa.invalid/schema/question.schema.json"
    schema["title"] = "Interview QA question"
    return schema


def schema_json() -> str:
    return json.dumps(question_schema(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def export_question_schema(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(schema_json(), encoding="utf-8", newline="\n")
