---
id: py-oop-0024
title: "Як перевизначення `__eq__` впливає на успадкований `__hash__` і використання instance у set або dict?"
description: "Якщо клас перевизначає __eq__ без визначення __hash__, то __hash__ неявно встановлюється в None, і instances стають unhashable – використання в set або dict викличе TypeError."
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: [eq, hash]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L166-L201
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Якщо клас перевизначає `__eq__` без визначення `__hash__`, то `__hash__` неявно встановлюється в `None`, і instances стають unhashable – використання в `set` або `dict` викличе `TypeError`.**[^py314-reference-datamodel] Це гарантує invariant: об'єкти, що порівнюються як рівні, мають однаковий hash. Щоб зберегти батьківський `__hash__`, потрібно явно вказати `__hash__ = ParentClass.__hash__`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
