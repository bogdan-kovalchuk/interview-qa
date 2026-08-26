---
id: py-prac-0007
title: "Реалізуйте palindrome check: застосуйте Unicode NFKC, `casefold()`, відкиньте non-alphanumeric characters і не створюйте reversed copy normalized string."
description: "Нормалізувати через unicodedata.normalize(\"NFKC\", s).casefold(), потім two-pointer scan з обох кінців, пропускаючи non-alphanumeric символи."
track: python
section: practical-coding
level: middle
type: coding
tags: [casefold]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: false
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L105-L114
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Task

TODO

## Constraints

TODO

## Short answer

**Нормалізувати через `unicodedata.normalize("NFKC", s).casefold()`, потім two-pointer scan з обох кінців, пропускаючи non-alphanumeric символи.**

```python
import unicodedata

def is_palindrome(s: str) -> bool:
    normalized = unicodedata.normalize("NFKC", s).casefold()
    lo, hi = 0, len(normalized) - 1
    while lo < hi:
        while lo < hi and not normalized[lo].isalnum():
            lo += 1
        while lo < hi and not normalized[hi].isalnum():
            hi -= 1
        if normalized[lo] != normalized[hi]:
            return False
        lo += 1
        hi -= 1
    return True
```

NFKC згортає сумісні символи (наприклад, повноширинні літери), `casefold()` дає case-insensitive порівняння, а two-pointer уникає створення фільтрованої копії рядка.

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
