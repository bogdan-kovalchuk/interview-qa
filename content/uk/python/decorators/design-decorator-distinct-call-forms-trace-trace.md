---
id: py-decor-0006
title: "Як спроєктувати decorator з двома чіткими call forms, `@trace` і `@trace(level=2)`, не переплутавши decorated callable з configuration arguments?"
description: "Треба перевірити, чи перший аргумент є callable: якщо func is not None – це bare @trace, інакше повернути partial-декоратор з конфігурацією."
track: python
section: decorators
level: senior
type: practical
tags: [trace, trace-level-2]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L191-L246
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Треба перевірити, чи перший аргумент є callable: якщо `func is not None` – це bare `@trace`, інакше повернути partial-декоратор з конфігурацією.**[^py314-glossary-term-decorator] Типовий патерн: outer-функція приймає `func=None, *, level=1`. Якщо `func` – callable, застосувати wrapper одразу; якщо `None` – повернути decorator, який замкне `level`. Альтернатива – `functools.partial` або окремий factory. Головне – не намагатися відрізнити callable від конфігурації за типом аргументу, бо callable може бути будь-яким об'єктом з `__call__`.

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
