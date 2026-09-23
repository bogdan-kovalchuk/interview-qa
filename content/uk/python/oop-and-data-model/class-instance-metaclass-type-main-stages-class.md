---
id: py-oop-0029
title: "Чому class є instance метакласу `type` і які основні етапи проходить class statement до створення class object?"
description: "Class є instance метакласу type (default metaclass), тому що type визначає як поводить себе class, так само як class визначає як поводить себе instance."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [type]
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

**Class є instance метакласу `type` (default metaclass), тому що `type` визначає як поводить себе class, так само як class визначає як поводить себе instance.**[^py314-reference-datamodel] Етапи створення: (1) визначення appropriate metaclass, (2) виклик `__prepare__` для створення namespace, (3) виконання class body в цьому namespace, (4) виклик `metaclass(name, bases, namespace)` для створення class object через `__new__` та `__init__`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
