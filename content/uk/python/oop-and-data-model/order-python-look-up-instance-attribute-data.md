---
id: py-oop-0004
title: "У якому порядку Python шукає атрибут instance за наявності data descriptor, instance dictionary, non-data descriptor і class attribute?"
description: "Порядок: data descriptor -> instance __dict__ -> non-data descriptor / class attribute -> __getattr__."
track: python
section: oop-and-data-model
level: senior
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

**Порядок: data descriptor -> instance `__dict__` -> non-data descriptor / class attribute -> `__getattr__`.**[^py314-reference-datamodel] Data descriptor (який визначає `__set__` або `__delete__`) завжди перемагає instance `__dict__`. Non-data descriptor (лише `__get__`) поступається запису в instance `__dict__`. Якщо нічого не знайдено і визначено `__getattr__`, викликається він; інакше – `AttributeError`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
