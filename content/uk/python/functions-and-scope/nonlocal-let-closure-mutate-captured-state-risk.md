---
id: py-funcs-0018
title: "Як `nonlocal` дозволяє closure змінювати captured state, і який ризик це створює при конкурентних викликах?"
description: "nonlocal дозволяє closure перезаписувати змінну в enclosing function scope, перетворюючи її на спільний мутабельний стан між усіма викликами closure."
track: python
section: functions-and-scope
level: senior
type: practical
tags: [nonlocal]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython with GIL"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L422-L516
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`nonlocal` дозволяє closure перезаписувати змінну в enclosing function scope, перетворюючи її на спільний мутабельний стан між усіма викликами closure.**[^py314-reference-simple-stmts-the-nonlocal-statement] У однопотоковому коді це стандартний патерн stateful closure (лічильник, кеш). <span class="warn">У багатопотоковому середовищі з GIL-enabled CPython операції на спільному стані не є атомарними: read-modify-write може бути перервано між потоками, що призводить до race condition.</span> Для безпеки потрібні примітиви синхронізації (`threading.Lock`).

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
