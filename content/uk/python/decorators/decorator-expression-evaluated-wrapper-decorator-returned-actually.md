---
id: py-decor-0001
title: "Коли обчислюється decorator expression і коли викликається wrapper, який decorator повернув?"
description: "Decorator expression обчислюється один раз під час визначення функції, а wrapper викликається при кожному виклику декорованої функції."
track: python
section: decorators
level: middle
type: mechanism
tags: []
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
---

## Short answer

**Decorator expression обчислюється один раз під час визначення функції, а wrapper викликається при кожному виклику декорованої функції.**[^py314-glossary-term-decorator] Тобто `@dec` виконує `dec(func)` immediately в scope, де визначена функція, і повертає wrapper-об'єкт. Сам wrapper запускається лише тоді, коли хтось викликає декороване ім'я. Це означає, що важка логіка ініціалізації (наприклад, відкриття файлу) потрапляє в decoration time, а per-call логіка – у wrapper.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
