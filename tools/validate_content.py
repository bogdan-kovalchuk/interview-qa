"""Check every question file against meta/QUESTIONS.md.

A first, dependency-free version of the content gates: it covers section order and
heading levels, the level rules, language parity, byte-identical code blocks, token
and source parity, the registry and section prefixes, vocabulary and typography.

It is deliberately plain: no pydantic, no YAML parser, no package layout. Step 1 of
PLAN.md folds it into tools/iqa/validate.py once the canonical model exists.

Run:  python tools/validate_content.py
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ORDER = {
    "concept": ["Short answer", "Detailed explanation", "Evaluation guide", "Follow-up", "Sources"],
    "mechanism": ["Short answer", "Detailed explanation", "Evaluation guide", "Follow-up", "Sources"],
    "comparison": ["Short answer", "Detailed explanation", "Comparison", "When to choose which",
                   "Evaluation guide", "Follow-up", "Sources"],
    "pitfall": ["Short answer", "Detailed explanation", "Symptom", "Why it happens", "How to avoid",
                "Evaluation guide", "Follow-up", "Sources"],
    "coding": ["Task", "Constraints", "Short answer", "Detailed explanation", "Examples", "Solution",
               "Complexity", "Edge cases", "Tests", "Evaluation guide", "Follow-up", "Sources"],
    "debugging": ["Short answer", "Detailed explanation", "Symptom", "Observations", "Reproduction",
                  "Hypotheses", "Diagnosis", "Fix", "Prevention", "Evaluation guide", "Follow-up",
                  "Sources"],
    "system-design": ["Scale prompt", "Short answer", "Detailed explanation", "Requirements",
                      "Scale assumptions", "Architecture", "Alternatives", "Trade-offs",
                      "Failure modes", "Evaluation guide", "Follow-up", "Sources"],
    "behavioral": ["Short answer", "Detailed explanation", "Competency assessed",
                   "STAR outline or illustrative example", "Follow-up prompts", "Evaluation guide",
                   "Sources"],
    "practical": ["Short answer", "Detailed explanation", "Environment", "Deliverable",
                  "Acceptance criteria", "Evaluation guide", "Follow-up", "Sources"],
}
OPTIONAL = {"Follow-up", "Reproduction"}
SUBBLOCKS = ["Expected signals", "Red flags", "Level-up follow-up"]
REQUIRED_FM = ["id", "title", "description", "track", "section", "level", "type", "status",
               "updated", "content_revision", "reconciled_with", "sources"]
LEVELS = {"junior", "middle", "senior"}
STATUSES = {"draft", "review", "published", "withdrawn"}
BAD_CHARS = {"—": "em dash U+2014", "←": "arrow U+2190", "→": "arrow U+2192"}

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def split_file(path: pathlib.Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        fail(f"{path.as_posix()}: no frontmatter")
        return "", "", text
    return match.group(1), match.group(2), text


def scalar(header: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{key}:\s*(.*)$", header)
    return match.group(1).strip() if match else None


def sections_of(body: str) -> list[str]:
    return [line[3:].strip() for line in re.findall(r"(?m)^## .+$", body)]


def load_vocabulary() -> dict[str, set[str]]:
    """Minimal reader for the few blocks we validate against. Not a YAML parser."""
    text = (ROOT / "meta" / "vocabulary.yml").read_text(encoding="utf-8")
    out: dict[str, set[str]] = {}
    for block in ("frameworks", "section_prefixes"):
        chunk = text.split(f"\n{block}:\n", 1)[1].split("\n\n", 1)[0]
        out[block] = {
            line.split(":")[0].strip()
            for line in chunk.splitlines()
            if line.startswith("  ") and ":" in line and not line.strip().startswith("#")
        }
    labels = text.split("\nsection_labels:\n", 1)[1].split("\n\n", 1)[0]
    out["section_labels"] = set(re.findall(r"(?m)^  (.+?):", labels))
    return out


def check_frontmatter(rel: str, header: str, path: pathlib.Path) -> None:
    for key in REQUIRED_FM:
        if not re.search(rf"(?m)^{key}:", header):
            fail(f"{rel}: missing required frontmatter `{key}`")
    if scalar(header, "level") not in LEVELS:
        fail(f"{rel}: level `{scalar(header, 'level')}` not in the enum")
    if scalar(header, "status") not in STATUSES:
        fail(f"{rel}: status `{scalar(header, 'status')}` not in the enum")
    if scalar(header, "type") not in ORDER:
        fail(f"{rel}: type `{scalar(header, 'type')}` not in the enum")
    if "legacy_card_id" in header:
        fail(f"{rel}: legacy_card_id does not exist any more")
    if re.search(r"(?m)^roles:", header):
        fail(f"{rel}: roles are derived from programs, not written in frontmatter")
    if track := scalar(header, "track"):
        # `section` is the whole path under the track, so nested sections such as
        # cpp/frameworks/qt are comparable: parts[3:-1] joined, not a single segment.
        section = "/".join(path.parts[3:-1])
        if path.parts[2] != track or section != scalar(header, "section"):
            fail(f"{rel}: path does not match track `{track}` / section `{section}`")

    block = re.search(r"(?m)^execution:\n((?:  .*\n|    .*\n)*)", header)
    if block:
        body = block.group(1)
        for key in ("language:", "standard:", "toolchain:", "flags:", "    name:", "    version:"):
            if key not in body:
                fail(f"{rel}: execution is missing `{key.strip()}`")
        if re.search(r"(?m)^  version:", body):
            fail(f"{rel}: execution has a top-level `version`; it belongs in toolchain")


def check_body(rel: str, body: str, kind: str, level: str) -> None:
    canon = ORDER[kind]
    got = sections_of(body)
    unknown = [name for name in got if name not in canon]
    if unknown:
        fail(f"{rel}: unknown section(s) {unknown}")
        return
    expected = [name for name in canon if name in got]
    if got != expected:
        fail(f"{rel}: section order {got} != canonical {expected}")
    for name in canon:
        if name in OPTIONAL or name in got:
            continue
        if name == "Evaluation guide" and level == "junior":
            continue
        fail(f"{rel}: missing required section `{name}`")

    if "Evaluation guide" in got and level == "junior":
        fail(f"{rel}: junior must not carry an Evaluation guide")
    if "Evaluation guide" not in got and level in {"middle", "senior"}:
        fail(f"{rel}: {level} must carry an Evaluation guide")
    if "Follow-up" in got:
        if level != "junior":
            fail(f"{rel}: the optional Follow-up is junior-only, level is {level}")
        if kind == "behavioral":
            fail(f"{rel}: the optional Follow-up is forbidden for behavioral")

    blocks = re.split(r"(?m)^(## .+)$", body)
    for i in range(1, len(blocks), 2):
        name, chunk = blocks[i][3:].strip(), blocks[i + 1]
        subs = [line[4:].strip() for line in re.findall(r"(?m)^### .+$", chunk)]
        if name == "Evaluation guide":
            if subs != SUBBLOCKS:
                fail(f"{rel}: Evaluation guide subblocks {subs} != {SUBBLOCKS}")
        elif subs:
            fail(f"{rel}: `###` outside the Evaluation guide, in `{name}`: {subs}")
        if re.search(r"(?m)^#{4,} ", chunk):
            fail(f"{rel}: heading deeper than `###` in `{name}`")
    if re.search(r"(?m)^# ", body):
        fail(f"{rel}: a top-level `#` heading in the body")

    tail = re.search(r"(?m)^## Sources$\n(.*)$", body, re.S)
    if tail and tail.group(1).strip() != "<!-- generated from frontmatter -->":
        fail(f"{rel}: Sources must hold only the generated comment")


def check_parity(qid: str, langs: dict[str, tuple[str, str]]) -> None:
    if set(langs) != {"en", "uk"}:
        fail(f"{qid}: languages {sorted(langs)} != en+uk")
        return
    (en_header, en_body), (uk_header, uk_body) = langs["en"], langs["uk"]
    if sections_of(en_body) != sections_of(uk_body):
        fail(f"{qid}: section parity broken")
    if re.findall(r"(?ms)^```.*?^```", en_body) != re.findall(r"(?ms)^```.*?^```", uk_body):
        fail(f"{qid}: code blocks differ between languages")
    for pattern, what in ((r"\[\^([a-z0-9-]+)\]", "citation tokens"),
                          (r"qid:([a-z0-9-]+)", "qid tokens")):
        if sorted(re.findall(pattern, en_body)) != sorted(re.findall(pattern, uk_body)):
            fail(f"{qid}: {what} differ between languages")
    ids = r"(?m)^    source_id: (\S+)"
    if sorted(re.findall(ids, en_header)) != sorted(re.findall(ids, uk_header)):
        fail(f"{qid}: source_id sets differ between languages")
    for lang, header in (("en", en_header), ("uk", uk_header)):
        other = "uk" if lang == "en" else "en"
        if not re.search(rf"(?m)^  {other}: \d+$", header):
            fail(f"{qid}/{lang}: reconciled_with does not name `{other}`")
        if re.search(rf"(?m)^  {lang}: \d+$", header):
            fail(f"{qid}/{lang}: reconciled_with names its own language")


def main() -> int:
    vocabulary = load_vocabulary()
    registry = {}
    for line in (ROOT / "meta" / "id-registry.csv").read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            qid, _created, status, path = line.split(",")
            registry[qid] = (status, path)

    files = sorted(ROOT.glob("content/*/*/**/*.md"))
    by_id: dict[str, dict[str, tuple[str, str]]] = {}

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        relative = path.relative_to(ROOT)
        header, body, text = split_file(path)
        if not header:
            continue
        qid, kind, level = scalar(header, "id"), scalar(header, "type"), scalar(header, "level")

        check_frontmatter(rel, header, relative)
        if kind in ORDER:
            check_body(rel, body, kind, level)

        if qid not in registry:
            fail(f"{rel}: {qid} is not in meta/id-registry.csv")
        else:
            status, registered = registry[qid]
            if status != scalar(header, "status"):
                fail(f"{rel}: registry status `{status}` != frontmatter")
            if registered != "/".join(relative.parts[2:]):
                fail(f"{rel}: registry current_path does not match the file")
            if registered.startswith(("en/", "uk/")):
                fail(f"{rel}: registry current_path carries a language segment")

        key = f"{scalar(header, 'track')}/{scalar(header, 'section')}"
        if key not in vocabulary["section_prefixes"]:
            fail(f"{rel}: section `{key}` has no prefix in meta/vocabulary.yml")
        if frameworks := scalar(header, "frameworks"):
            for name in re.findall(r"[a-z0-9-]+", frameworks):
                if name not in vocabulary["frameworks"]:
                    fail(f"{rel}: framework `{name}` is not in meta/vocabulary.yml")

        for char, what in BAD_CHARS.items():
            if char in text:
                fail(f"{rel}: contains {what}")

        by_id.setdefault(qid, {})[relative.parts[1]] = (header, body)

    for qid, langs in by_id.items():
        check_parity(qid, langs)

    for path in files:
        _, body, _ = split_file(path)
        for target in re.findall(r"qid:([a-z0-9-]+)", body):
            if target not in by_id:
                fail(f"{path.relative_to(ROOT).as_posix()}: qid:{target} does not resolve")

    for name in {s for names in ORDER.values() for s in names} | set(SUBBLOCKS):
        if name not in vocabulary["section_labels"] and name not in SUBBLOCKS:
            fail(f"meta/vocabulary.yml: no visible label for section `{name}`")

    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(("site/node_modules", "site/dist", "site/src/content/docs")):
            continue
        if "migration/legacy" in rel or "venv" in rel:
            continue
        if "—" in path.read_text(encoding="utf-8"):
            fail(f"{rel}: contains an em dash U+2014")

    print(f"checked {len(files)} question files, {len(by_id)} questions")
    if failures:
        print(f"\n{len(failures)} failures:")
        for message in failures:
            print("  -", message)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
