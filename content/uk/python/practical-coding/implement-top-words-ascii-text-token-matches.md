---
id: py-prac-0012
title: "Реалізуйте top-3 words для ASCII text: token матчить `[A-Za-z]+`, comparison є case-insensitive, а ties сортуються lexicographically."
description: "Використовуємо re.findall(r'[A-Za-z]+', text) для токенізації, Counter з .lower() для підрахунку, та sorted з ключем (-count, word) для lexicographic tie-breaking."
track: python
section: practical-coding
level: middle
type: coding
tags: [a-za-z]
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
---

## Task

TODO

## Constraints

TODO

## Short answer

**Використовуємо `re.findall(r'[A-Za-z]+', text)` для токенізації, `Counter` з `.lower()` для підрахунку, та `sorted` з ключем `(-count, word)` для lexicographic tie-breaking.** `Counter.most_common()` не гарантує порядку для ties, тому явно сортуємо за спаданням частоти та зростанням слова.

```python
import re
from collections import Counter

def top3_words(text):
    words = re.findall(r'[A-Za-z]+', text)
    counts = Counter(w.lower() for w in words)
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return [w for w, _ in sorted_items[:3]]

top3_words('Hello world hello World foo bar foo bar baz')  # ['bar', 'foo', 'hello']
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
