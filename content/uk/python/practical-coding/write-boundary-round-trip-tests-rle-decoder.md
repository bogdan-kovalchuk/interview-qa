---
id: py-prac-0025
title: "Складіть boundary та round-trip tests для RLE decoder з grammar `count:character|count:character`: count є positive decimal, а character не може бути `:` чи `|`; malformed input викликає `ValueError`."
description: "Boundary: мінімальний count=1, round-trip decode(encode(s)) == s; malformed -> ValueError для заборонених символів, нульового count і порушення grammar."
track: python
section: practical-coding
level: middle
type: practical
tags: [count-character-count-character, valueerror]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L800-L827
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Boundary: мінімальний `count=1`, round-trip `decode(encode(s)) == s`; malformed -> `ValueError` для заборонених символів, нульового count і порушення grammar.**[^py314-tutorial] Валідні: `"3:a|2:b|1:c" -> "aaabbc"`; `"1:x" -> "x"`; `"12:ab" -> "ab" * 12`. Round-trip: `decode(encode("aabbc")) == "aabbc"`. Malformed -> `ValueError`: `""` (порожній), `":a"` (немає count), `"0:a"` (count ≠ positive), `"-1:a"` (не decimal), `"1::"` (character=`:`), `"1:|"` (character=`|`), `"3:a|"` (trailing `|`), `"a:b"` (non-digit count).

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
