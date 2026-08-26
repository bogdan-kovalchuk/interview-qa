---
id: py-objtypes-0021
title: "Коли `isinstance()` є доречним runtime check, а коли protocol або duck typing робить код менш зв’язаним із concrete classes?"
description: "isinstance() доречний на межі API для швидких guards, у dispatch-логіці (наприклад серіалізація) та з ABC для virtual subclasses."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [isinstance]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L587-L609
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`isinstance()` доречний на межі API для швидких guards, у dispatch-логіці (наприклад серіалізація) та з ABC для virtual subclasses.**[^py314-reference-datamodel] Проте перевірка щодо конкретного класу tightly couple до ієрархії успадкування. `typing.Protocol` з `@runtime_checkable` та duck typing перевіряють поведінку (наявність методів/атрибутів) без вимоги конкретних класів. Duck typing ловить `AttributeError` під час виконання, а `@runtime_checkable` Protocol перевіряє лише наявність атрибутів, не сигнатури методів.

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
