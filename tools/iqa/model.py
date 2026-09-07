"""Canonical question model and Markdown parser.

This module owns every closed frontmatter vocabulary and every body section
sequence. Consumers must import those definitions instead of copying them.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from datetime import date
from enum import Enum
import json
from pathlib import Path
import re
from types import MappingProxyType
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, StringConstraints, field_validator, model_validator
import yaml


KEBAB_CASE = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
SECTION_PATH = r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*$"
QUESTION_ID = (
    r"^(?:py|cpp|cs|sys|db|eng|sd|bhv|emb|ds|ml|de|be|ops|qa)-"
    r"[a-z0-9]{3,8}-[0-9]{4}$"
)

KebabValue = Annotated[str, StringConstraints(pattern=KEBAB_CASE)]
QuestionIdValue = Annotated[str, StringConstraints(pattern=QUESTION_ID)]
RevisionValue = Annotated[int, Field(ge=1)]


class Language(str, Enum):
    EN = "en"
    UK = "uk"


class Level(str, Enum):
    JUNIOR = "junior"
    MIDDLE = "middle"
    SENIOR = "senior"


class QuestionType(str, Enum):
    CONCEPT = "concept"
    MECHANISM = "mechanism"
    COMPARISON = "comparison"
    PITFALL = "pitfall"
    PRACTICAL = "practical"
    CODING = "coding"
    DEBUGGING = "debugging"
    SYSTEM_DESIGN = "system-design"
    BEHAVIORAL = "behavioral"


class Status(str, Enum):
    DRAFT = "draft"
    REVIEW = "review"
    PUBLISHED = "published"
    WITHDRAWN = "withdrawn"


class SourceKind(str, Enum):
    OFFICIAL = "official"
    SPEC = "spec"
    BOOK = "book"
    COMMUNITY = "community"


class SectionName(str, Enum):
    QUESTION_CODE = "Question code"
    SHORT_ANSWER = "Short answer"
    DETAILED_EXPLANATION = "Detailed explanation"
    COMPARISON = "Comparison"
    WHEN_TO_CHOOSE_WHICH = "When to choose which"
    SYMPTOM = "Symptom"
    WHY_IT_HAPPENS = "Why it happens"
    HOW_TO_AVOID = "How to avoid"
    TASK = "Task"
    CONSTRAINTS = "Constraints"
    EXAMPLES = "Examples"
    SOLUTION = "Solution"
    COMPLEXITY = "Complexity"
    EDGE_CASES = "Edge cases"
    TESTS = "Tests"
    OBSERVATIONS = "Observations"
    REPRODUCTION = "Reproduction"
    HYPOTHESES = "Hypotheses"
    DIAGNOSIS = "Diagnosis"
    FIX = "Fix"
    PREVENTION = "Prevention"
    SCALE_PROMPT = "Scale prompt"
    REQUIREMENTS = "Requirements"
    SCALE_ASSUMPTIONS = "Scale assumptions"
    ARCHITECTURE = "Architecture"
    ALTERNATIVES = "Alternatives"
    TRADE_OFFS = "Trade-offs"
    FAILURE_MODES = "Failure modes"
    COMPETENCY_ASSESSED = "Competency assessed"
    STAR_OUTLINE = "STAR outline or illustrative example"
    FOLLOW_UP_PROMPTS = "Follow-up prompts"
    ENVIRONMENT = "Environment"
    DELIVERABLE = "Deliverable"
    ACCEPTANCE_CRITERIA = "Acceptance criteria"
    EVALUATION_GUIDE = "Evaluation guide"
    FOLLOW_UP = "Follow-up"
    SOURCES = "Sources"


class EvaluationSubsection(str, Enum):
    EXPECTED_SIGNALS = "Expected signals"
    RED_FLAGS = "Red flags"
    LEVEL_UP_FOLLOW_UP = "Level-up follow-up"


SECTION_SEQUENCES: Mapping[QuestionType, tuple[SectionName, ...]] = MappingProxyType(
    {
        QuestionType.CONCEPT: (
            SectionName.QUESTION_CODE,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.MECHANISM: (
            SectionName.QUESTION_CODE,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.COMPARISON: (
            SectionName.QUESTION_CODE,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.COMPARISON,
            SectionName.WHEN_TO_CHOOSE_WHICH,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.PITFALL: (
            SectionName.QUESTION_CODE,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.SYMPTOM,
            SectionName.WHY_IT_HAPPENS,
            SectionName.HOW_TO_AVOID,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.CODING: (
            SectionName.TASK,
            SectionName.CONSTRAINTS,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.EXAMPLES,
            SectionName.SOLUTION,
            SectionName.COMPLEXITY,
            SectionName.EDGE_CASES,
            SectionName.TESTS,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.DEBUGGING: (
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.SYMPTOM,
            SectionName.OBSERVATIONS,
            SectionName.REPRODUCTION,
            SectionName.HYPOTHESES,
            SectionName.DIAGNOSIS,
            SectionName.FIX,
            SectionName.PREVENTION,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.SYSTEM_DESIGN: (
            SectionName.SCALE_PROMPT,
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.REQUIREMENTS,
            SectionName.SCALE_ASSUMPTIONS,
            SectionName.ARCHITECTURE,
            SectionName.ALTERNATIVES,
            SectionName.TRADE_OFFS,
            SectionName.FAILURE_MODES,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
        QuestionType.BEHAVIORAL: (
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.COMPETENCY_ASSESSED,
            SectionName.STAR_OUTLINE,
            SectionName.FOLLOW_UP_PROMPTS,
            SectionName.EVALUATION_GUIDE,
            SectionName.SOURCES,
        ),
        QuestionType.PRACTICAL: (
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
            SectionName.ENVIRONMENT,
            SectionName.DELIVERABLE,
            SectionName.ACCEPTANCE_CRITERIA,
            SectionName.EVALUATION_GUIDE,
            SectionName.FOLLOW_UP,
            SectionName.SOURCES,
        ),
    }
)

EVALUATION_SUBSECTIONS: tuple[EvaluationSubsection, ...] = tuple(EvaluationSubsection)
OPTIONAL_SECTIONS = frozenset(
    {SectionName.QUESTION_CODE, SectionName.FOLLOW_UP, SectionName.REPRODUCTION}
)


class CanonicalModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Toolchain(CanonicalModel):
    name: str = Field(min_length=1, pattern=KEBAB_CASE)
    version: str = Field(min_length=1)


class Execution(CanonicalModel):
    language: str = Field(min_length=1, pattern=KEBAB_CASE)
    standard: str | None
    toolchain: Toolchain
    flags: tuple[str, ...]


class Applicability(CanonicalModel):
    product: str = Field(min_length=1)
    version: str | None


class AnkiSettings(CanonicalModel):
    export: bool = True


class Source(CanonicalModel):
    source_id: str = Field(pattern=KEBAB_CASE)
    title: str = Field(min_length=1)
    url: HttpUrl
    accessed: date
    kind: SourceKind
    version: str | None
    applicability: str = Field(min_length=1)


class QuestionFrontmatter(CanonicalModel):
    id: QuestionIdValue
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    track: str = Field(pattern=KEBAB_CASE)
    section: str = Field(pattern=SECTION_PATH)
    level: Level
    type: QuestionType
    status: Status
    updated: date
    content_revision: int = Field(ge=1)
    reconciled_with: dict[Language, RevisionValue]
    sources: tuple[Source, ...] = Field(min_length=1)
    tags: tuple[KebabValue, ...] = ()
    frameworks: tuple[KebabValue, ...] = ()
    execution: Execution | None = None
    applies_to: tuple[Applicability, ...] = ()
    see_also: tuple[QuestionIdValue, ...] = ()
    prerequisites: tuple[QuestionIdValue, ...] = ()
    anki: AnkiSettings = AnkiSettings()

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

    @model_validator(mode="after")
    def reconciliation_names_the_other_language(self) -> "Question":
        expected = {language for language in Language if language is not self.language}
        actual = set(self.frontmatter.reconciled_with)
        if actual != expected:
            raise ValueError(
                "reconciled_with must name every other language and not its own language"
            )
        return self

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


def expected_sections(
    question_type: QuestionType,
    level: Level,
    present_optional: Iterable[SectionName] = (),
) -> tuple[SectionName, ...]:
    present = frozenset(present_optional)
    result: list[SectionName] = []
    for section in SECTION_SEQUENCES[question_type]:
        if section is SectionName.EVALUATION_GUIDE and level is Level.JUNIOR:
            continue
        if section is SectionName.FOLLOW_UP and not (
            level is Level.JUNIOR and section in present
        ):
            continue
        if section is SectionName.REPRODUCTION and section not in present:
            continue
        if section is SectionName.QUESTION_CODE and section not in present:
            continue
        result.append(section)
    return tuple(result)


def required_text_sections(
    question_type: QuestionType, level: Level
) -> tuple[SectionName, ...]:
    return tuple(
        section
        for section in expected_sections(question_type, level)
        if section not in (SectionName.SOURCES, SectionName.QUESTION_CODE)
    )


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
