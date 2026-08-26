---
id: py-oop-0007
title: "Чому property зазвичай не можна затінити однойменним значенням в `instance.__dict__`?"
description: "property реалізований як data descriptor (визначає __get__, __set__, __delete__), тому за правилами attribute lookup він має пріоритет над instance __dict__."
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: [instance-dict]
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

**`property` реалізований як data descriptor (визначає `__get__`, `__set__`, `__delete__`), тому за правилами attribute lookup він має пріоритет над instance `__dict__`.**[^py314-reference-datamodel] Навіть якщо вручну записати `obj.__dict__['x'] = value`, звернення `obj.x` викличе getter property, а не поверне значення з словника. <span class="warn">Обхід можливий лише через клас: `ClassName.x.__set__(obj, value)` або заміну самого descriptor у класі.</span>

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
