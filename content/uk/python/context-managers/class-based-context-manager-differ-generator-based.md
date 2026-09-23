---
id: py-ctxmgr-0004
title: "Чим class-based context manager відрізняється від generator-based manager через `@contextmanager`?"
description: "Class-based визначає __enter__ і __exit__ як окремі методи та легко зберігає стан у self; generator-based використовує одну функцію з yield, де код до yield – це enter, а після – exit."
track: python
section: context-managers
level: middle
type: comparison
tags: [contextmanager]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Class-based визначає `__enter__` і `__exit__` як окремі методи та легко зберігає стан у `self`; generator-based використовує одну функцію з `yield`, де код до yield – це enter, а після – exit.**[^py314-reference-datamodel-with-statement-context-managers] `@contextmanager` скорочує boilerplate для простих менеджерів, але створює "one-shot" об'єкт – повторне використання того самого instance викличе `RuntimeError`. Class-based підхід кращий, коли потрібна reuse, reentrancy або складна ініціалізація.

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
