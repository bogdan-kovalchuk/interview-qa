---
id: py-funcs-0014
title: "Як Python шукатиме ім’я `len` усередині функції, якщо локального binding немає, але модуль визначив власний `len`?"
description: "Python шукає ім'я в порядку: local -> enclosing -> global (модуль) -> builtins; тому модульний len буде знайдено раніше за вбудований len."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [len]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L99-L132
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Python шукає ім'я в порядку: local -> enclosing -> global (модуль) -> builtins; тому модульний `len` буде знайдено раніше за вбудований `len`.**[^py314-reference-executionmodel-resolution-of-names] Оскільки локального binding немає і enclosing scope (якщо функція не вкладена) теж не містить `len`, пошук дійде до глобального namespace модуля і знайде визначений там `len`, не дійшовши до `builtins`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
