---
id: py-oop-0028
title: "Які trade-offs щодо пам'яті та успадкування має `__slots__` і чому це не універсальна performance-оптимізація?"
description: "__slots__ запобігає створенню __dict__ для кожного instance, економлячи пам'ять при багатьох instances з невеликою кількістю атрибутів, але вимагає, щоб усі parent classes також мали __slots__, інакше instances..."
track: python
section: oop-and-data-model
level: senior
type: practical
tags: [slots]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L540-L585
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`__slots__` запобігає створенню `__dict__` для кожного instance, економлячи пам'ять при багатьох instances з невеликою кількістю атрибутів, але вимагає, щоб усі parent classes також мали `__slots__`, інакше instances отримають `__dict__`.**[^py314-reference-datamodel] <span class="warn">Subclass без власного `__slots__` матиме `__dict__`, скасовуючи економію.</span> Множинне успадкування з кількома slotted parent classes обмежене: лише один parent може мати non-empty slots. Динамічне додавання атрибутів неможливе, що ускладнює деякі патерни.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
