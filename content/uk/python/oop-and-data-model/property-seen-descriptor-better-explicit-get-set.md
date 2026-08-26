---
id: py-oop-0011
title: "Чому `property` можна розглядати як descriptor і коли він кращий за явні `get_*`/`set_*` methods?"
description: "property – це вбудований data descriptor, який реалізує __get__, __set__ і __delete__, тому повністю підпорядковується descriptor protocol."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [property, get, set]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L961-L1046
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`property` – це вбудований data descriptor, який реалізує `__get__`, `__set__` і `__delete__`, тому повністю підпорядковується descriptor protocol.**[^py314-reference-datamodel] Він кращий за явні `get_*`/`set_*` методи, коли потрібно додати логіку (валідацію, обчислення, логування) до вже існуючого attribute access, не змінюючи публічний API: клієнти продовжують писати `obj.attr`, а не `obj.get_attr()`. Завдяки тому що `property` є data descriptor, він має пріоритет над `instance.__dict__`, що гарантує виклик getter/setter навіть якщо instance спробує перезаписати атрибут.

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
