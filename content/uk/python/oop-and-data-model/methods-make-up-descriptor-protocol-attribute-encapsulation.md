---
id: py-oop-0010
title: "Які методи утворюють descriptor protocol і яку проблему інкапсуляції атрибутів він вирішує?"
description: "Descriptor protocol – це __get__, __set__ та __delete__; він дозволяє винести логіку доступу до атрибута (валідацію, обчислення, логування) в окремий об'єкт, зберігаючи звичайний dot-синтаксис."
track: python
section: oop-and-data-model
level: middle
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

**Descriptor protocol – це `__get__`, `__set__` та `__delete__`; він дозволяє винести логіку доступу до атрибута (валідацію, обчислення, логування) в окремий об'єкт, зберігаючи звичайний dot-синтаксис.**[^py314-reference-datamodel] Замість того щоб вимагати від користувача викликати `get_x()` / `set_x()`, descriptor перехоплює `obj.x` на рівні протоколу. Це забезпечує інкапсуляцію без порушення API: внутрішнє зберігання можна змінити, а публічний інтерфейс залишається незмінним.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
