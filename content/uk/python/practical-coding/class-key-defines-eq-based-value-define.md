---
id: py-prac-0005
title: "Клас `Key` визначає `__eq__` за `value`, але не визначає `__hash__`: що станеться при `{Key(1): \"x\"}` і як виправити contract для immutable key?"
description: "Піднімається TypeError: unhashable type: 'Key'."
track: python
section: practical-coding
level: senior
type: pitfall
tags: [key, eq, value, hash, key-1-x]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Піднімається `TypeError: unhashable type: 'Key'`.**[^py314-tutorial] Коли клас визначає `__eq__`, CPython автоматично встановлює `__hash__ = None`, роблячи об'єкти unhashable. Для immutable key потрібно явно визначити `__hash__`, узгоджений з `__eq__`: хешувати ті самі поля, що порівнюються в `__eq__`. Наприклад, `def __hash__(self): return hash(self.value)`.

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
