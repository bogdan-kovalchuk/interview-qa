---
id: py-decor-0003
title: "Які проблеми з metadata, introspection і debugging виникають, якщо wrapper не використовує `functools.wraps`?"
description: "Без functools.wraps декорована функція втрачає __name__, __doc__, __qualname__ та __annotations__ – замість них підставляються атрибути wrapper-функції."
track: python
section: decorators
level: middle
type: pitfall
tags: [functools-wraps]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L247-L278
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Без `functools.wraps` декорована функція втрачає `__name__`, `__doc__`, `__qualname__` та `__annotations__` – замість них підставляються атрибути wrapper-функції.**[^py314-glossary-term-decorator] Наприклад, `example.__name__` стане `'wrapper'`, а `__doc__` – `None`. Це ламає `help()`, stack traces показують неправильне ім'я, а інструменти на кшталт Sphinx генерують хибну документацію. Рішення – викликати `@functools.wraps(func)` на wrapper.

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
