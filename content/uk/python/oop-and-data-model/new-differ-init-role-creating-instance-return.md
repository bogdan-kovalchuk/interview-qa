---
id: py-oop-0001
title: "Чим `__new__` відрізняється від `__init__` за роллю у створенні instance та за return value?"
description: "__new__ створює та повертає новий instance, тоді як __init__ лише ініціалізує вже створений instance і не повинен повертати значення."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [new, init]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`__new__` створює та повертає новий instance, тоді як `__init__` лише ініціалізує вже створений instance і не повинен повертати значення.**[^py314-reference-datamodel] Сам `__new__` – неявний staticmethod, який отримує `cls` і повертає об'єкт (зазвичай instance `cls`). А `__init__` отримує готовий `self`, налаштовує його атрибути і має повертати `None`.

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
