---
id: py-funcs-0003
title: "Як без втрати позиційних та keyword arguments передати отримані `*args` і `**kwargs` іншій функції, і яку помилку легко зробити під час такого forwarding?"
description: "Потрібно розпаковувати їх при виклику: target(*args,"
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [args, kwargs]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L35-L56
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Потрібно розпаковувати їх при виклику: `target(*args, **kwargs)`, а не передавати як звичайні аргументи.**[^py314-reference-expressions-calls] Поширена помилка – написати `target(args, kwargs)`: тоді `args` (tuple) піде як один позиційний аргумент, а `kwargs` (dict) – як один keyword, що зазвичай дає `TypeError` у цільовій функції. Розпакування через `*` і `**` відновлює початкову структуру позиційних та keyword аргументів.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
