---
id: py-funcs-0002
title: "Коли й чому виклик `f(1, a=2)` для `def f(a): ...` завершується помилкою: до входу в тіло функції чи під час його виконання?"
description: "Помилка TypeError: f() got multiple values for keyword argument 'a' виникає до входу в тіло функції, на етапі binding аргументів."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [f-1-a-2, def-f-a]
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
---

## Short answer

**Помилка `TypeError: f() got multiple values for keyword argument 'a'` виникає до входу в тіло функції, на етапі binding аргументів.**[^py314-reference-expressions-calls] Позиційний аргумент `1` заповнює слот параметра `a`, а keyword `a=2` намагається заповнити той самий слот. Інтерпретатор перевіряє конфлікти під час побудови фрейму виклику, тому тіло функції не виконується взагалі.

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
