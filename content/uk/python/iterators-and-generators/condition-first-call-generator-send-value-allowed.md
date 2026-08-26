---
id: py-itergen-0011
title: "За якої умови перший виклик `generator.send(value)` допустимий і чому зазвичай спочатку надсилають `None`?"
description: "Перший виклик send() допускає лише None, бо на момент старту generator ще не дійшов до жодного yield, яким міг би прийняти значення."
track: python
section: iterators-and-generators
level: middle
type: pitfall
tags: [generator-send-value]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L338-L429
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Перший виклик `send()` допускає лише `None`, бо на момент старту generator ще не дійшов до жодного `yield`, яким міг би прийняти значення.**[^py314-library-stdtypes-iterator-types] Коли generator ще не запущено, немає виразу `yield`, що міг би отримати надіслане значення, тому будь-яке значення, відмінне від `None`, спричинить `TypeError`. Альтернатива – викликати `next(gen)`, що еквівалентно `gen.send(None)`.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
