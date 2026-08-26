---
id: py-objtypes-0016
title: "Як numeric equality між `1`, `1.0` і `True` впливає на їх використання як keys одного словника?"
description: "1, 1.0 і True мають однаковий hash і порівнюються як рівні (1 == 1.0 == True), тому в dict вони займають одну й ту ж комірку – перемагає останнє присвоєння."
track: python
section: objects-and-types
level: senior
type: pitfall
tags: [1-0]
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
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L104-L117
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`1`, `1.0` і `True` мають однаковий hash і порівнюються як рівні (`1 == 1.0 == True`), тому в dict вони займають одну й ту ж комірку – перемагає останнє присвоєння.**[^py314-reference-datamodel]

```text
d = {1: 'a', 1.0: 'b', True: 'c'}
print(d)        # {1: 'c'}
print(len(d))   # 1
```

Це наслідок числової ієрархії Python: `bool` є підтипом `int`, тому `True == 1`, а `float` і `int` порівнюються за числовим значенням. <span class="warn">Аналогічна колапсія відбувається у `set`: `{1, 1.0, True}` містить лише один елемент.</span>

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
