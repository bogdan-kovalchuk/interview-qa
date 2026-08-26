---
id: py-oop-0002
title: "Чому для налаштування immutable subclass на кшталт custom `tuple` потрібний `__new__`, а зміни лише в `__init__` запізнюються?"
description: "Immutable типи (tuple, str, int) фіксують своє значення під час алокації в __new__; до моменту виклику __init__ об'єкт уже створений і незмінний."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [tuple, new, init]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L78-L98
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Immutable типи (`tuple`, `str`, `int`) фіксують своє значення під час алокації в `__new__`; до моменту виклику `__init__` об'єкт уже створений і незмінний.**[^py314-reference-datamodel] Тому будь-яка кастомізація вмісту мутабельного контейнера має відбутися в `__new__`, бо `__init__` не може змінити вже заморожені дані.

```python
class Doubled(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, (x * 2 for x in args))
```

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
