"""Content-only validation for Interview QA questions."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
import csv
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
import shutil
import sys
from typing import Any

from jsonschema import Draft202012Validator
from pydantic import ValidationError
import yaml

from .taxonomy import ordered_paths
from .model import (
    code_spans,
    outside_code,
    EVALUATION_SUBSECTIONS,
    OPTIONAL_SECTIONS,
    EvaluationSubsection,
    Language,
    Level,
    Question,
    QuestionType,
    SectionName,
    SourceKind,
    Status,
    expected_sections,
    load_frontmatter,
    parse_body,
    schema_json,
)


CITATION_RE = re.compile(r"\[\^([a-z0-9]+(?:-[a-z0-9]+)*)\]")
QID_RE = re.compile(r"(?<![a-z0-9-])qid:([a-z0-9][a-z0-9-]*)", re.IGNORECASE)
CODE_BLOCK_RE = re.compile(r"(?ms)^```[^\r\n]*\r?\n.*?^```[ \t]*(?=\r?$)")
INLINE_CODE_RE = re.compile(r"`[^`\r\n]+`")
READY_URL_RE = re.compile(r"https?://|(?<![\w])/(?:en|uk)/q/", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\r\n]+\]\([^)\r\n]+\)")
MARKDOWN_LINK_TARGET_RE = re.compile(
    r"(?<!!)\[[^\]\r\n]+\]\((?P<target>[^)\r\n]+)\)"
)
SOURCE_COMMENT = "<!-- generated from frontmatter -->"
FORBIDDEN_CONTENT_CHARACTERS = {
    "\u2014": "em dash U+2014",
    "\u2190": "arrow U+2190",
    "\u2192": "arrow U+2192",
}


@dataclass(frozen=True)
class Diagnostic:
    gate: str
    severity: str
    message: str
    path: str | None = None


@dataclass
class ValidationReport:
    files_checked: int = 0
    questions_checked: int = 0
    diagnostics: list[Diagnostic] = field(default_factory=list)

    @property
    def errors(self) -> list[Diagnostic]:
        return [item for item in self.diagnostics if item.severity == "error"]

    @property
    def warnings(self) -> list[Diagnostic]:
        return [item for item in self.diagnostics if item.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add(
        self,
        gate: str,
        message: str,
        *,
        path: str | None = None,
        severity: str = "error",
    ) -> None:
        diagnostic = Diagnostic(gate, severity, message, path)
        if diagnostic not in self.diagnostics:
            self.diagnostics.append(diagnostic)


@dataclass
class FileRecord:
    path: Path
    relative: Path
    text: str
    raw_frontmatter: dict[str, Any] | None = None
    raw_body: str = ""
    question: Question | None = None

    @property
    def label(self) -> str:
        return self.relative.as_posix()


@dataclass(frozen=True)
class RegistryEntry:
    id: str
    status: str
    current_path: str


def _load_registry(path: Path, report: ValidationReport) -> dict[str, RegistryEntry]:
    entries: dict[str, RegistryEntry] = {}
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            required = {"id", "created", "status", "current_path"}
            if set(reader.fieldnames or ()) != required:
                report.add(
                    "id-immutable",
                    f"registry columns must be {sorted(required)}",
                    path=path.as_posix(),
                )
                return entries
            for row in reader:
                qid = row["id"].strip()
                if qid in entries:
                    report.add(
                        "id-unique", f"duplicate registry id `{qid}`", path=path.as_posix()
                    )
                    continue
                entries[qid] = RegistryEntry(
                    id=qid,
                    status=row["status"].strip(),
                    current_path=row["current_path"].strip().replace("\\", "/"),
                )
    except (OSError, csv.Error) as error:
        report.add("id-immutable", f"cannot read registry: {error}", path=path.as_posix())
    return entries


def _load_vocabulary(path: Path, report: ValidationReport) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        report.add("facets-vocabulary", f"cannot read vocabulary: {error}", path=path.as_posix())
        return {}
    if not isinstance(value, dict):
        report.add("facets-vocabulary", "vocabulary must be a mapping", path=path.as_posix())
        return {}
    return value


def _taxonomy_paths(path: Path, report: ValidationReport) -> set[str]:
    # The parse itself lives in tools/iqa/taxonomy.py: the mirror needs the same
    # tree in document order to build the site navigation, and one file must not
    # be read by two different parsers.
    try:
        return set(ordered_paths(path))
    except OSError as error:
        report.add("taxonomy", f"cannot read taxonomy: {error}", path=path.as_posix())
        return set()


def _schema_gate(
    records: list[FileRecord], schema_path: Path, report: ValidationReport
) -> dict[str, Any] | None:
    expected = schema_json()
    try:
        actual = schema_path.read_text(encoding="utf-8")
    except OSError as error:
        report.add("schema", f"cannot read generated schema: {error}", path=schema_path.as_posix())
        return None
    if actual != expected:
        report.add(
            "schema",
            "generated schema is stale; regenerate it from iqa.model",
            path=schema_path.as_posix(),
        )
    try:
        schema = json.loads(actual)
        Draft202012Validator.check_schema(schema)
    except Exception as error:
        report.add("schema", f"generated schema is invalid: {error}", path=schema_path.as_posix())
        return None

    validator = Draft202012Validator(schema)
    for record in records:
        if record.question is None:
            continue
        payload = record.question.model_dump(mode="json")
        for error in validator.iter_errors(payload):
            report.add(
                "schema",
                f"JSON Schema mismatch at {'/'.join(map(str, error.path))}: {error.message}",
                path=record.label,
            )
    return schema


def _read_records(content_root: Path, report: ValidationReport) -> list[FileRecord]:
    records: list[FileRecord] = []
    for path in sorted(content_root.rglob("*.md")):
        relative = path.relative_to(content_root)
        record = FileRecord(path=path, relative=relative, text=path.read_text(encoding="utf-8"))
        records.append(record)
        if len(relative.parts) < 4:
            report.add(
                "taxonomy",
                "question path must be {lang}/{track}/.../{slug}.md",
                path=record.label,
            )
        try:
            frontmatter, body = load_frontmatter(record.text)
            record.raw_frontmatter = frontmatter
            record.raw_body = body
        except (ValueError, yaml.YAMLError) as error:
            report.add("schema", str(error), path=record.label)
            continue

        language = relative.parts[0] if relative.parts else ""
        try:
            record.question = Question.model_validate(
                {
                    "language": language,
                    "slug": path.stem,
                    "source_path": relative.as_posix(),
                    "frontmatter": frontmatter,
                    "body": parse_body(body),
                }
            )
        except ValidationError as error:
            details = "; ".join(
                f"{'/'.join(map(str, item['loc']))}: {item['msg']}" for item in error.errors()
            )
            report.add("schema", details, path=record.label)
            locations = {tuple(item["loc"]) for item in error.errors()}
            if any("execution" in location for location in locations):
                report.add("example-executed", "execution is not well-formed", path=record.label)
            if any("sources" in location for location in locations):
                report.add("source-applicability", "source metadata is not well-formed", path=record.label)
            if any(
                set(location) & {"level", "type", "status", "frameworks"}
                for location in locations
            ):
                report.add("facets-vocabulary", "a closed facet is invalid", path=record.label)
    report.files_checked = len(records)
    return records


def _raw_content_gates(record: FileRecord, report: ValidationReport) -> None:
    frontmatter = record.raw_frontmatter
    if frontmatter is None:
        return

    sources = frontmatter.get("sources")
    source_list = sources if isinstance(sources, list) else []
    source_error = not source_list
    if source_list and all(
        isinstance(source, dict) and source.get("kind") == SourceKind.COMMUNITY.value
        for source in source_list
    ):
        source_error = True
    if source_error:
        message = "at least one non-community source is required"
        report.add("sources", message, path=record.label)
        report.add("source-present", message, path=record.label)

    for index, source in enumerate(source_list):
        if not isinstance(source, dict):
            report.add(
                "source-applicability", f"source {index + 1} must be a mapping", path=record.label
            )
            continue
        missing = [
            key
            for key in ("accessed", "version", "applicability")
            if key not in source
        ]
        if missing or source.get("accessed") is None or not str(
            source.get("applicability", "")
        ).strip():
            report.add(
                "source-applicability",
                f"source {index + 1} lacks explicit version, accessed date, or applicability",
                path=record.label,
            )

    for character, label in FORBIDDEN_CONTENT_CHARACTERS.items():
        if character in record.text:
            report.add("schema", f"contains forbidden {label}", path=record.label)


def _facets_gate(record: FileRecord, vocabulary: dict[str, Any], report: ValidationReport) -> None:
    frontmatter = record.raw_frontmatter
    if frontmatter is None:
        return
    for field_name, enum_type in (
        ("level", Level),
        ("type", QuestionType),
        ("status", Status),
    ):
        try:
            enum_type(frontmatter.get(field_name))
        except (TypeError, ValueError):
            report.add(
                "facets-vocabulary",
                f"`{field_name}` is not in its closed vocabulary",
                path=record.label,
            )
    allowed_frameworks = set((vocabulary.get("frameworks") or {}).keys())
    frameworks = frontmatter.get("frameworks", [])
    if not isinstance(frameworks, list):
        report.add("facets-vocabulary", "`frameworks` must be a list", path=record.label)
    else:
        for framework in frameworks:
            if framework not in allowed_frameworks:
                report.add(
                    "facets-vocabulary",
                    f"framework `{framework}` is not in meta/vocabulary.yml",
                    path=record.label,
                )
    question = record.question
    if question is not None:
        track = question.frontmatter.track
        section_path = f"{track}/{question.frontmatter.section}"
        if track not in (vocabulary.get("track_labels") or {}):
            report.add(
                "facets-vocabulary",
                f"track `{track}` has no visible label",
                path=record.label,
            )
        if section_path not in (vocabulary.get("section_labels_nav") or {}):
            report.add(
                "facets-vocabulary",
                f"section `{section_path}` has no visible navigation label",
                path=record.label,
            )
        if section_path not in (vocabulary.get("section_prefixes") or {}):
            report.add(
                "facets-vocabulary",
                f"section `{section_path}` has no immutable ID prefix",
                path=record.label,
            )


def _vocabulary_contract_gate(vocabulary: dict[str, Any], report: ValidationReport) -> None:
    section_labels = vocabulary.get("section_labels") or {}
    subsection_labels = vocabulary.get("subsection_labels") or {}
    for section in SectionName:
        labels = section_labels.get(section.value)
        if not isinstance(labels, dict) or set(labels) != {"en", "uk"}:
            report.add(
                "facets-vocabulary",
                f"section `{section.value}` needs en and uk labels",
                path="meta/vocabulary.yml",
            )
    for subsection in EvaluationSubsection:
        labels = subsection_labels.get(subsection.value)
        if not isinstance(labels, dict) or set(labels) != {"en", "uk"}:
            report.add(
                "facets-vocabulary",
                f"subsection `{subsection.value}` needs en and uk labels",
                path="meta/vocabulary.yml",
            )
    for section_path, prefix in (vocabulary.get("section_prefixes") or {}).items():
        if not re.fullmatch(r"[a-z]{3,8}", str(prefix)):
            report.add(
                "facets-vocabulary",
                f"section prefix for `{section_path}` must be 3 to 8 lowercase letters",
                path="meta/vocabulary.yml",
            )


def _sections_gates(record: FileRecord, report: ValidationReport) -> None:
    question = record.question
    if question is None:
        return
    headings = [section.heading for section in question.body.sections]
    known_names = {section.value for section in SectionName}
    unknown = [heading for heading in headings if heading not in known_names]
    if unknown:
        report.add("sections", f"unknown section(s): {unknown}", path=record.label)

    present_optional = {
        SectionName(heading)
        for heading in headings
        if heading in known_names and SectionName(heading) in OPTIONAL_SECTIONS
    }
    expected = [
        section.value
        for section in expected_sections(
            question.frontmatter.type, question.frontmatter.level, present_optional
        )
    ]
    if headings != expected:
        report.add(
            "sections",
            f"section order {headings} does not match {expected}",
            path=record.label,
        )

    if question.body.preamble:
        report.add("sections", "body content appears before the first section", path=record.label)
    # Fenced code is skipped: `# note` at the start of a line inside a Python or
    # shell example is a comment, not a level-1 heading, and the house style for
    # `Detailed explanation` puts exactly such comments in its examples.
    spans = code_spans(question.body.raw)
    for marker in re.finditer(r"(?m)^(#{1,6})[ \t]+", question.body.raw):
        if not outside_code(marker.start(), spans):
            continue
        level = len(marker.group(1))
        if level not in {2, 3}:
            report.add("sections", f"heading level {level} is forbidden", path=record.label)

    for section in question.body.sections:
        if not section.content:
            report.add("sections", f"section `{section.heading}` is empty", path=record.label)
        if section.heading == SectionName.SOURCES.value:
            if section.content != SOURCE_COMMENT:
                report.add(
                    "sections",
                    "Sources must contain only the generated comment",
                    path=record.label,
                )
        elif section.heading == SectionName.EVALUATION_GUIDE.value:
            subsection_names = [subsection.heading for subsection in section.subsections]
            expected_subsections = [item.value for item in EVALUATION_SUBSECTIONS]
            if section.content == "TODO":
                if subsection_names:
                    report.add(
                        "sections",
                        "a TODO Evaluation guide must not contain subblocks",
                        path=record.label,
                    )
            elif subsection_names != expected_subsections:
                report.add(
                    "sections",
                    f"Evaluation guide subblocks {subsection_names} do not match {expected_subsections}",
                    path=record.label,
                )
            for subsection in section.subsections:
                if not subsection.content:
                    report.add(
                        "sections",
                        f"Evaluation guide subblock `{subsection.heading}` is empty",
                        path=record.label,
                    )
        elif section.heading == SectionName.QUESTION_CODE.value:
            # The snippet the question is about, and nothing else: the question's
            # own wording is the title, and the section is optional - a question
            # with no code omits it instead of filling it with `TODO`.
            blocks = len(CODE_BLOCK_RE.findall(section.content))
            if section.content.strip() == "TODO":
                report.add(
                    "sections",
                    "Question code is optional: omit the section rather than mark it TODO",
                    path=record.label,
                )
            elif blocks != 1 or _without_code(section.content).strip():
                report.add(
                    "sections",
                    f"Question code must hold exactly one code block and no other text (found {blocks})",
                    path=record.label,
                )
        elif section.subsections:
            report.add(
                "sections", f"`###` is forbidden in `{section.heading}`", path=record.label
            )

    evaluation_present = SectionName.EVALUATION_GUIDE.value in headings
    if question.frontmatter.level is Level.JUNIOR and evaluation_present:
        report.add(
            "sections-by-level", "junior questions must not have Evaluation guide", path=record.label
        )
    if question.frontmatter.level in {Level.MIDDLE, Level.SENIOR} and not evaluation_present:
        report.add(
            "sections-by-level",
            f"{question.frontmatter.level.value} questions require Evaluation guide",
            path=record.label,
        )
    if SectionName.FOLLOW_UP.value in headings:
        if question.frontmatter.level is not Level.JUNIOR:
            report.add(
                "sections-by-level", "Follow-up is allowed only for junior", path=record.label
            )
        if question.frontmatter.type is QuestionType.BEHAVIORAL:
            report.add(
                "sections-by-level", "Follow-up is forbidden for behavioral", path=record.label
            )


def _without_code(text: str) -> str:
    return CODE_BLOCK_RE.sub("", text)


def _without_any_code(text: str) -> str:
    """Fenced blocks *and* inline spans removed.

    Only the link and URL checks use this. They look for `[text](target)` and
    a bare `http://`, and C writes both by accident: `table[opcode](ctx, frame)`
    inside backticks is an array of function pointers, not a Markdown link, and
    `_without_code` leaves inline spans in place. Sentence and word counts
    deliberately keep using `_without_code`, because a term in backticks is
    still a word the reader reads.
    """
    return INLINE_CODE_RE.sub("", _without_code(text))


def _sentence_count(text: str) -> int:
    cleaned = _without_code(text)
    cleaned = CITATION_RE.sub("", cleaned)
    # Inline code or highlighting can legitimately start the next sentence
    # with a lowercase identifier, for example `<code>mutex</code>`.
    cleaned = re.sub(
        r"(?<=[.!?])(\s+)<(?=(?:code|span)\b)", r"\1X<", cleaned, flags=re.IGNORECASE
    )
    # Preserve a word boundary where legacy/imported answers use HTML line
    # breaks. Removing the tag directly would join `sentence.<br>Next` into
    # `sentence.Next` and undercount otherwise valid prose.
    cleaned = re.sub(r"<br\s*/?>", " ", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    cleaned = re.sub(r"[*_`]", "", cleaned)
    cleaned = re.sub(r"(?m)^\s*(?:[-+*]|\d+[.)])\s+", "", cleaned)
    cleaned = " ".join(cleaned.split())
    if not cleaned:
        return 0
    boundaries = re.findall(
        r"[.!?](?:[\"')\]]+)?(?=\s+(?:[A-ZА-ЯІЇЄҐ0-9*_<\[])|$)", cleaned
    )
    return len(boundaries)


def _short_answer_gate(record: FileRecord, report: ValidationReport) -> None:
    question = record.question
    if question is None:
        return
    short = question.section(SectionName.SHORT_ANSWER)
    if short is None or short.content == "TODO":
        return
    count = _sentence_count(short.content)
    if not 2 <= count <= 5:
        report.add(
            "short-answer-limits",
            f"Short answer has {count} sentences; expected 2 to 5",
            path=record.label,
        )
    code_blocks = CODE_BLOCK_RE.findall(short.content)
    if len(code_blocks) > 1:
        report.add(
            "short-answer-limits", "Short answer has more than one code block", path=record.label
        )
    outside_code = _without_code(short.content)
    if re.search(r"(?m)^\s{2,}(?:[-+*]|\d+[.)])\s+", outside_code):
        report.add(
            "short-answer-limits", "Short answer has a nested list", path=record.label
        )
    if re.search(r"(?m)^#{1,6}[ \t]+", outside_code):
        report.add("short-answer-limits", "Short answer contains a heading", path=record.label)
    outside_any_code = _without_any_code(short.content)
    if MARKDOWN_LINK_RE.search(outside_any_code) or READY_URL_RE.search(outside_any_code):
        report.add(
            "short-answer-limits", "Short answer contains a ready URL", path=record.label
        )
    if re.search(
        r"\A\s*\*\*(?:(?!\*\*).)*<span[ \t]+class=[\"']warn[\"']",
        outside_code,
        re.IGNORECASE | re.DOTALL,
    ):
        report.add(
            "short-answer-limits", ".warn must not be nested in bold key text", path=record.label
        )
    words = re.findall(r"(?u)\b[\w'+-]+\b", CITATION_RE.sub("", _without_code(short.content)))
    if len(words) > 90:
        report.add(
            "short-answer-limits",
            f"Short answer has {len(words)} words; more than 90 is a warning",
            path=record.label,
            severity="warning",
        )

    for section in question.body.sections:
        if section.heading != SectionName.SHORT_ANSWER.value and re.search(
            r"<span[ \t]+class=[\"']warn[\"']", section.content, re.IGNORECASE
        ):
            report.add(
                "short-answer-limits", ".warn is allowed only in Short answer", path=record.label
            )


def _xref_gate(record: FileRecord, known_ids: set[str], report: ValidationReport) -> None:
    question = record.question
    if question is None:
        return
    body_without_code = _without_any_code(question.body.raw)
    ready_markdown_link = any(
        not match.group("target").strip().lower().startswith("qid:")
        for match in MARKDOWN_LINK_TARGET_RE.finditer(body_without_code)
    )
    if ready_markdown_link or READY_URL_RE.search(body_without_code):
        report.add("xref", "ready URLs are forbidden in content", path=record.label)
    for target in QID_RE.findall(question.body.raw):
        if target not in known_ids:
            report.add("xref", f"qid:{target} does not resolve", path=record.label)
    for target in (*question.frontmatter.see_also, *question.frontmatter.prerequisites):
        if target not in known_ids:
            report.add("xref", f"frontmatter reference `{target}` does not resolve", path=record.label)


def _taxonomy_gate(
    record: FileRecord, taxonomy_paths: set[str], report: ValidationReport
) -> None:
    question = record.question
    if question is None:
        return
    expected_path = f"{question.frontmatter.track}/{question.frontmatter.section}"
    if expected_path not in taxonomy_paths:
        report.add("taxonomy", f"`{expected_path}` is not in meta/taxonomy.md", path=record.label)
    parts = record.relative.parts
    actual_track = parts[1] if len(parts) > 1 else ""
    actual_section = "/".join(parts[2:-1]) if len(parts) > 3 else ""
    if actual_track != question.frontmatter.track or actual_section != question.frontmatter.section:
        report.add(
            "taxonomy",
            f"path is `{actual_track}/{actual_section}`, frontmatter is `{expected_path}`",
            path=record.label,
        )


def _id_gates(
    records: list[FileRecord], registry: dict[str, RegistryEntry], report: ValidationReport
) -> None:
    per_language: dict[tuple[str, str], list[FileRecord]] = defaultdict(list)
    paths_per_id: dict[str, set[str]] = defaultdict(set)
    for record in records:
        question = record.question
        if question is None:
            continue
        qid = question.frontmatter.id
        language = question.language.value
        per_language[(language, qid)].append(record)
        paths_per_id[qid].add("/".join(record.relative.parts[1:]))

        entry = registry.get(qid)
        if entry is None:
            report.add("id-immutable", f"`{qid}` is absent from id-registry.csv", path=record.label)
            continue
        canonical_path = "/".join(record.relative.parts[1:])
        if entry.current_path != canonical_path:
            report.add(
                "id-immutable",
                f"registry path `{entry.current_path}` does not match `{canonical_path}`",
                path=record.label,
            )
        if entry.status != question.frontmatter.status.value:
            report.add(
                "id-immutable",
                f"registry status `{entry.status}` does not match `{question.frontmatter.status.value}`",
                path=record.label,
            )
        if entry.current_path.startswith(("en/", "uk/")):
            report.add(
                "id-immutable", "registry current_path must not contain a language", path=record.label
            )

    for (language, qid), duplicates in per_language.items():
        if len(duplicates) > 1:
            report.add(
                "id-unique",
                f"`{qid}` appears {len(duplicates)} times in {language}",
                path=duplicates[0].label,
            )
    for qid, paths in paths_per_id.items():
        if len(paths) > 1:
            report.add(
                "id-unique", f"`{qid}` maps to multiple paths: {sorted(paths)}"
            )


def _claim_gate(record: FileRecord, report: ValidationReport) -> None:
    question = record.question
    if question is None:
        return
    source_ids = {source.source_id for source in question.frontmatter.sources}
    citations = CITATION_RE.findall(question.body.raw)
    for source_id in citations:
        if source_id not in source_ids:
            report.add(
                "claim-linked", f"citation `{source_id}` has no matching source", path=record.label
            )
    if re.search(r"(?m)^\[\^[^]]+\]:", question.body.raw):
        report.add(
            "claim-linked", "manual footnote definitions are forbidden", path=record.label
        )

    if question.frontmatter.type is QuestionType.CODING:
        evidence_sections = (SectionName.COMPLEXITY,)
    elif question.frontmatter.type is QuestionType.BEHAVIORAL:
        evidence_sections = (SectionName.COMPETENCY_ASSESSED,)
    else:
        evidence_sections = (
            SectionName.SHORT_ANSWER,
            SectionName.DETAILED_EXPLANATION,
        )
    for section_name in evidence_sections:
        section = question.section(section_name)
        if section is None or section.content == "TODO":
            continue
        if not CITATION_RE.search(section.content):
            report.add(
                "claim-linked",
                f"written `{section_name.value}` has no citation token",
                path=record.label,
            )


def _toolchain_exists(name: str) -> bool:
    if name == "cpython":
        return bool(sys.executable and Path(sys.executable).exists())
    return shutil.which(name) is not None


def _execution_gate(record: FileRecord, report: ValidationReport) -> None:
    question = record.question
    if question is None or question.frontmatter.execution is None:
        return
    name = question.frontmatter.execution.toolchain.name
    if not _toolchain_exists(name):
        report.add(
            "example-executed",
            f"declared toolchain `{name}` is not available",
            path=record.label,
        )


def _language_gates(
    records: list[FileRecord], vocabulary: dict[str, Any], report: ValidationReport
) -> None:
    grouped: dict[str, dict[Language, FileRecord]] = defaultdict(dict)
    for record in records:
        if record.question is not None:
            grouped[record.question.frontmatter.id][record.question.language] = record
    report.questions_checked = len(grouped)

    glossary = vocabulary.get("glossary") or []
    for qid, languages in grouped.items():
        if set(languages) != {Language.EN, Language.UK}:
            report.add(
                "lang-files-exist",
                f"`{qid}` has languages {[lang.value for lang in sorted(languages, key=lambda x: x.value)]}",
            )
            continue
        en_record = languages[Language.EN]
        uk_record = languages[Language.UK]
        en = en_record.question
        uk = uk_record.question
        assert en is not None and uk is not None

        en_canonical = "/".join(en_record.relative.parts[1:])
        uk_canonical = "/".join(uk_record.relative.parts[1:])
        if en_canonical != uk_canonical:
            report.add(
                "lang-files-exist",
                f"`{qid}` language slugs or paths differ: `{en_canonical}` vs `{uk_canonical}`",
            )

        en_headings = [section.heading for section in en.body.sections]
        uk_headings = [section.heading for section in uk.body.sections]
        if en_headings != uk_headings:
            report.add(
                "lang-structure-parity",
                f"`{qid}` section sequences differ",
            )

        # Both gates below compare *written* text between languages. Per
        # meta/quality-gates.md's framing rule, a `TODO` placeholder is
        # exempt from having text at all - it carries no code and no
        # citation/qid tokens to be identical or parallel to anything, so a
        # section that is `TODO` on either side is excluded from both
        # comparisons rather than compared against an empty section on the
        # other side. A section written in both languages is still compared
        # in full - this only stops the gate from treating "not written yet"
        # as a mismatch.
        en_by_heading = {section.heading: section for section in en.body.sections}
        uk_by_heading = {section.heading: section for section in uk.body.sections}
        written_headings = [
            heading
            for heading in en_by_heading
            if heading in uk_by_heading
            and en_by_heading[heading].content.strip() != "TODO"
            and uk_by_heading[heading].content.strip() != "TODO"
        ]
        en_written_raw = "\n".join(en_by_heading[h].content for h in written_headings)
        uk_written_raw = "\n".join(uk_by_heading[h].content for h in written_headings)

        if CODE_BLOCK_RE.findall(en_written_raw) != CODE_BLOCK_RE.findall(uk_written_raw):
            report.add("lang-code-identical", f"`{qid}` code blocks differ")

        en_links = {
            "sources": {source.source_id for source in en.frontmatter.sources},
            "citations": set(CITATION_RE.findall(en_written_raw)),
            "qids": set(QID_RE.findall(en_written_raw)),
        }
        uk_links = {
            "sources": {source.source_id for source in uk.frontmatter.sources},
            "citations": set(CITATION_RE.findall(uk_written_raw)),
            "qids": set(QID_RE.findall(uk_written_raw)),
        }
        if en_links != uk_links:
            report.add("lang-links-parity", f"`{qid}` sources or link tokens differ")

        for entry in glossary:
            if not isinstance(entry, dict) or not entry.get("en") or not entry.get("uk"):
                continue
            english = str(entry["en"])
            ukrainian = str(entry["uk"])
            term_pattern = re.compile(
                rf"(?<![\w-]){re.escape(english)}(?![\w-])", re.IGNORECASE
            )
            expected_pattern = re.compile(
                rf"(?<![\w-]){re.escape(ukrainian)}(?![\w-])", re.IGNORECASE
            )
            if term_pattern.search(en_record.text) and not expected_pattern.search(uk_record.text):
                report.add(
                    "lang-glossary",
                    f"`{qid}` uses `{english}` in English but not canonical `{ukrainian}` in Ukrainian",
                    path=uk_record.label,
                )

        en_revision = en.frontmatter.content_revision
        uk_revision = uk.frontmatter.content_revision
        if uk.frontmatter.reconciled_with.get(Language.EN, 0) < en_revision:
            report.add(
                "lang-reconciliation",
                f"`{qid}` Ukrainian revision marker trails English revision {en_revision}",
                severity="warning",
            )
        if en.frontmatter.reconciled_with.get(Language.UK, 0) < uk_revision:
            report.add(
                "lang-reconciliation",
                f"`{qid}` English revision marker trails Ukrainian revision {uk_revision}",
                severity="warning",
            )


def _duplicate_report(records: list[FileRecord], report: ValidationReport) -> None:
    english = [
        record.question
        for record in records
        if record.question is not None and record.question.language is Language.EN
    ]
    for index, left in enumerate(english):
        assert left is not None
        left_title = " ".join(re.findall(r"[a-z0-9]+", left.frontmatter.title.lower()))
        for right in english[index + 1 :]:
            assert right is not None
            shared_tags = set(left.frontmatter.tags) & set(right.frontmatter.tags)
            if not shared_tags:
                continue
            right_title = " ".join(re.findall(r"[a-z0-9]+", right.frontmatter.title.lower()))
            similarity = SequenceMatcher(None, left_title, right_title).ratio()
            if similarity >= 0.88:
                report.add(
                    "no-duplicates",
                    f"possible duplicate `{left.frontmatter.id}` and `{right.frontmatter.id}` "
                    f"(title similarity {similarity:.2f}, tags {sorted(shared_tags)})",
                    severity="warning",
                )


def validate_repository(root: Path) -> ValidationReport:
    root = root.resolve()
    report = ValidationReport()
    content_root = root / "content"
    records = _read_records(content_root, report)
    vocabulary = _load_vocabulary(root / "meta" / "vocabulary.yml", report)
    taxonomy_paths = _taxonomy_paths(root / "meta" / "taxonomy.md", report)
    registry = _load_registry(root / "meta" / "id-registry.csv", report)
    _schema_gate(records, root / "meta" / "question.schema.json", report)
    _vocabulary_contract_gate(vocabulary, report)

    for record in records:
        _raw_content_gates(record, report)
        _facets_gate(record, vocabulary, report)
        _sections_gates(record, report)
        _short_answer_gate(record, report)
        _taxonomy_gate(record, taxonomy_paths, report)
        _claim_gate(record, report)
        _execution_gate(record, report)

    _id_gates(records, registry, report)
    known_ids = {
        record.question.frontmatter.id for record in records if record.question is not None
    }
    for record in records:
        _xref_gate(record, known_ids, report)
    _language_gates(records, vocabulary, report)
    _duplicate_report(records, report)
    report.diagnostics.sort(key=lambda item: (item.severity, item.gate, item.path or "", item.message))
    return report


def print_report(report: ValidationReport) -> None:
    print(
        f"checked {report.files_checked} question files, "
        f"{report.questions_checked} questions"
    )
    for diagnostic in report.diagnostics:
        location = f"{diagnostic.path}: " if diagnostic.path else ""
        print(f"{diagnostic.severity.upper()} [{diagnostic.gate}] {location}{diagnostic.message}")
    if report.ok:
        print(f"all blocking checks passed ({len(report.warnings)} warning(s))")
    else:
        print(f"{len(report.errors)} blocking failure(s), {len(report.warnings)} warning(s)")
