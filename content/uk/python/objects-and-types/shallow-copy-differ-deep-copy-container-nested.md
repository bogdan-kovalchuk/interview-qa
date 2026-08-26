---
id: py-objtypes-0009
title: "Чим shallow copy відрізняється від deep copy для контейнера з вкладеними mutable objects?"
description: "Shallow copy створює новий зовнішній контейнер, але внутрішні об'єкти залишаються спільними посиланнями; deep copy рекурсивно копіює все до кінця."
track: python
section: objects-and-types
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Shallow copy створює новий зовнішній контейнер, але внутрішні об'єкти залишаються спільними посиланнями; deep copy рекурсивно копіює все до кінця.**[^py314-reference-datamodel] Для `a = [[1, 2]]`: після `s = copy.copy(a)` вираз `s[0] is a[0]` – `True`, і mutation `s[0]` змінює `a[0]`. Після `d = copy.deepcopy(a)` вираз `d[0] is a[0]` – `False`, і mutation `d[0]` не впливає на `a[0]`.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
