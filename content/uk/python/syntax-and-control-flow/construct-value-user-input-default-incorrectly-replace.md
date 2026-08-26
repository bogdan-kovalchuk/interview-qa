---
id: py-syntax-0003
title: "Чому конструкція `value = user_input or default` може помилково замінити коректне значення `0` або порожній рядок?"
description: "or повертає перший truthy operand, тому будь-яке falsy значення (0, \"\", [], None) буде замінено на default."
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [value-user-input-or-default]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`or` повертає перший truthy operand, тому будь-яке falsy значення (`0`, `""`, `[]`, `None`) буде замінено на `default`.**[^py314-reference-expressions] Якщо `0` або `""` є валідними вхідними даними, ця конструкція не розрізняє «відсутнє значення» та «коректне falsy значення». Для точної перевірки треба явно порівнювати з `None`: `value = default if user_input is None else user_input`.

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
