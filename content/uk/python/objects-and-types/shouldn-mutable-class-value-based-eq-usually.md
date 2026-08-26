---
id: py-objtypes-0012
title: "Чому mutable class із value-based `__eq__` зазвичай не повинна успадковувати identity-based hash від `object`?"
description: "Контракт Python вимагає: якщо два об'єкти рівні за __eq__, вони повинні мати однаковий hash; identity-based hash від object використовує унікальний id(), тому рівні за значенням об'єкти потраплять у різні hash-корзини..."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [eq, object]
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
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L206-L242
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Контракт Python вимагає: якщо два об'єкти рівні за `__eq__`, вони повинні мати однаковий hash; identity-based hash від `object` використовує унікальний `id()`, тому рівні за значенням об'єкти потраплять у різні hash-корзини dict/set і стануть «невидимими» при пошуку.**[^py314-reference-datamodel] Для mutable класу з value-based `__eq__` правильне рішення – або зробити клас unhashable (`__hash__ = None`), або визначити `__hash__` на основі тих самих полів, що й `__eq__`, і гарантувати їх незмінність після додавання в dict/set. <span class="warn">У CPython `object.__hash__` базується на `id()`, тобто на адресі об'єкта в пам'яті.</span>

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
