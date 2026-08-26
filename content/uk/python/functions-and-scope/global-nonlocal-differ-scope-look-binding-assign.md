---
id: py-funcs-0013
title: "Чим відрізняються `global` і `nonlocal` за тим, у якому scope вони шукають binding для присвоєння?"
description: "global прив'язує ім'я до namespace модуля (top-level), а nonlocal – до найближчого enclosing function scope, не включаючи модуль."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [global, nonlocal]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-simple-stmts-the-global-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-global-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L133-L189
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`global` прив'язує ім'я до namespace модуля (top-level), а `nonlocal` – до найближчого enclosing function scope, не включаючи модуль.**[^py314-reference-simple-stmts-the-global-statement] При цьому `nonlocal` шукає binding лише у функціях-обгортках; якщо такого binding немає, виникає `SyntaxError`. Натомість `global` завжди посилається на модульний рівень, навіть якщо ім'я визначено у вкладеній функції.

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
