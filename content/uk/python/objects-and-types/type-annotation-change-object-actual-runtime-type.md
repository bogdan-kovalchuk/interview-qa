---
id: py-objtypes-0020
title: "Чи змінює type annotation фактичний runtime type об’єкта або автоматично забороняє присвоєння значення іншого типу?"
description: "Ні, type annotation не змінює runtime type об'єкта і не забороняє присвоєння значення іншого типу – Python runtime ігнорує анотації при виконанні."
track: python
section: objects-and-types
level: middle
type: pitfall
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L610-L648
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ні, type annotation не змінює runtime type об'єкта і не забороняє присвоєння значення іншого типу – Python runtime ігнорує анотації при виконанні.**[^py314-reference-datamodel] Анотації зберігаються в `__annotations__` і доступні через `typing.get_type_hints()`, але інтерпретатор не перевіряє їх. Перевірку виконують зовнішні інструменти: статичні type checkers (mypy, pyright), IDE та linters. <span class="warn">Написати `x: int = 'hello'` – цілком валідний Python-код без помилок runtime.</span>

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
