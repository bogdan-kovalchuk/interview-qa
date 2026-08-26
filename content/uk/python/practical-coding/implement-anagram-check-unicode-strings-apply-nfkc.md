---
id: py-prac-0013
title: "Реалізуйте anagram check для Unicode strings: застосуйте NFKC та `casefold()`, ігноруйте whitespace, а інші code points враховуйте."
description: "Застосовуємо unicodedata.normalize('NFKC', s), потім .casefold() для case-insensitive порівняння, фільтруємо .isspace() code points та порівнюємо sorted() списки символів."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L828-L849
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

**Застосовуємо `unicodedata.normalize('NFKC', s)`, потім `.casefold()` для case-insensitive порівняння, фільтруємо `.isspace()` code points та порівнюємо `sorted()` списки символів.** NFKC нормалізує compatibility variants (наприклад, é vs é), `casefold()` агресивніший за `.lower()` для Unicode (наприклад, німецьке ß -> ss).

```python
import unicodedata

def is_anagram(s1, s2):
    def normalize(s):
        nfkc = unicodedata.normalize('NFKC', s)
        folded = nfkc.casefold()
        return sorted(ch for ch in folded if not ch.isspace())
    return normalize(s1) == normalize(s2)

is_anagram('Listen', 'Silent')  # True
is_anagram('\u00e9', 'e\u0301')  # True
```

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
