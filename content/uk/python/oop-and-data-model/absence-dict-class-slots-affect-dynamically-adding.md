---
id: py-oop-0008
title: "Як відсутність `__dict__` у класі з `__slots__` впливає на динамічне додавання атрибутів?"
description: "Instance класу з __slots__ не має __dict__, тому спроба додати атрибут, не перелічений у __slots__, піднімає AttributeError."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [dict, slots]
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

**Instance класу з `__slots__` не має `__dict__`, тому спроба додати атрибут, не перелічений у `__slots__`, піднімає `AttributeError`.**[^py314-reference-datamodel] Замість словника атрибути зберігаються у фіксованих слотах (дескрипторах рівня класу). Це економить пам'ять на великих наборах instance, але обмежує гнучкість. <span class="warn">Якщо до `__slots__` додати `'__dict__'`, instance знову отримає словник і зможе приймати довільні атрибути.</span>

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
