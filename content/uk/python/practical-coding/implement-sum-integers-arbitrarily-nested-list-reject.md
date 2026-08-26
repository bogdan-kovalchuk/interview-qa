---
id: py-prac-0008
title: "Реалізуйте суму integers у довільно вкладених lists: `bool` відхиляти, інші types мають викликати `TypeError`, а cycle у lists – `ValueError`."
description: "Рекурсивний обхід з перевіркою isinstance(obj, bool) перед isinstance(obj, int) (бо bool – підклас int) та множиною id() для виявлення циклів."
track: python
section: practical-coding
level: middle
type: coding
tags: [bool, typeerror, valueerror]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L275-L293
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

**Рекурсивний обхід з перевіркою `isinstance(obj, bool)` перед `isinstance(obj, int)` (бо `bool` – підклас `int`) та множиною `id()` для виявлення циклів.**

```python
def nested_sum(data):
    def _sum(obj, seen):
        if isinstance(obj, bool):
            raise TypeError("bool is not allowed")
        if isinstance(obj, int):
            return obj
        if isinstance(obj, list):
            oid = id(obj)
            if oid in seen:
                raise ValueError("cycle detected")
            seen = seen | {oid}
            return sum(_sum(item, seen) for item in obj)
        raise TypeError(
            f"unsupported type: {type(obj).__name__}"
        )
    return _sum(data, set())
```

<span class="warn">Порядок `isinstance` критичний: `bool` перевіряється першим, інакше `True`/`False` пройде як `int`.</span>

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
