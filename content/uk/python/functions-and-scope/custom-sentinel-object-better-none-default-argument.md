---
id: py-funcs-0008
title: "Коли власний sentinel object кращий за `None` як default argument у публічному API?"
description: "Sentinel потрібен, коли None є валідним значенням параметра і його треба відрізняти від «аргумент не передано»."
track: python
section: functions-and-scope
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Sentinel потрібен, коли `None` є валідним значенням параметра і його треба відрізняти від «аргумент не передано».**[^py314-reference-compound-stmts-function-definitions] Наприклад, у функції `def find(key, default=_SENTINEL)` користувач може явно передати `default=None`, і функція має повернути `None`, а не шукати ключ. Sentinel – це унікальний об'єкт (зазвичай `object()`), який порівнюється за ідентичністю (`is`), тому ніяке валідне значення не може випадково збігтися з ним.

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
