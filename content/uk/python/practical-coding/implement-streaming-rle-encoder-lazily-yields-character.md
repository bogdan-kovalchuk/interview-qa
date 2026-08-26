---
id: py-prac-0014
title: "Реалізуйте streaming RLE encoder, який з iterable characters ліниво видає tuples `(character, positive_count)` з O(1) auxiliary memory; empty input не видає нічого."
description: "Generator зберігає лише current character та count, yield при зміні character; empty input обробляється через StopIteration на next(it)."
track: python
section: practical-coding
level: middle
type: coding
tags: [character-positive-count]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L800-L827
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

**Generator зберігає лише `current` character та `count`, yield при зміні character; empty input обробляється через `StopIteration` на `next(it)`.** O(1) memory досягається тим, що generator не матеріалізує input, а обробляє потік по одному елементу. <span class="warn">Не використовуйте `itertools.groupby` без розуміння, що він потребує попереднього сортування для не-суміжних дублікатів.</span>

```python
def rle_encode(iterable):
    it = iter(iterable)
    try:
        current = next(it)
    except StopIteration:
        return
    count = 1
    for ch in it:
        if ch == current:
            count += 1
        else:
            yield (current, count)
            current = ch
            count = 1
    yield (current, count)

list(rle_encode('aaabbc'))  # [('a', 3), ('b', 2), ('c', 1)]
list(rle_encode(''))  # []
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
