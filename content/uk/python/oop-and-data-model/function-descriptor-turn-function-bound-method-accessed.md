---
id: py-oop-0015
title: "Як function descriptor перетворює function у bound method при доступі через instance, але не при доступі через class?"
description: "function.__get__(obj, objtype) перевіряє перший аргумент: якщо obj is None (доступ через клас), повертає саму функцію; інакше повертає MethodType(func, obj)."
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L1047-L1124
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`function.__get__(obj, objtype)` перевіряє перший аргумент: якщо `obj is None` (доступ через клас), повертає саму функцію; інакше повертає `MethodType(func, obj)`.**[^py314-reference-datamodel] Це означає, що `MyClass.method` дає «сиру» функцію (без прив'язки до instance), а `instance.method` – bound method із вже зафіксованим `__self__`. Така поведінка закладена в `func_descr_get()` CPython і є частиною descriptor protocol для всіх user-defined functions.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
