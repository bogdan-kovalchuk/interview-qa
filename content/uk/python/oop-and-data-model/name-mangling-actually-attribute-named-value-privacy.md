---
id: py-oop-0006
title: "Що реально робить name mangling для атрибута `__value` і чому це не є security-механізмом приватності?"
description: "Name mangling автоматично перейменовує __value у _ClassName__value, щоб уникнути випадкових колізій імен у підкласах."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [value]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L714-L769
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Name mangling автоматично перейменовує `__value` у `_ClassName__value`, щоб уникнути випадкових колізій імен у підкласах.**[^py314-reference-datamodel] Трансформація відбувається на етапі компіляції: будь-який ідентифікатор `__name` (два або більше leading `_`, без trailing `__`) у визначенні класу `Foo` стає `_Foo__name`. Це не блокує доступ – до мангленого імені можна звернутися напряму, тому механізм захищає від випадкових конфліктів, а не від навмисного доступу.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
