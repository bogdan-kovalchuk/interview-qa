---
id: py-itergen-0004
title: "Як реалізувати re-iterable collection так, щоб дві вкладені ітерації не ділили один cursor?"
description: "Розділити iterable та iterator: __iter__() колекції має щоразу повертати новий iterator."
track: python
section: iterators-and-generators
level: senior
type: practical
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L19-L104
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Розділити iterable та iterator: `__iter__()` колекції має щоразу повертати новий iterator.**[^py314-library-stdtypes-iterator-types] Типовий підхід – зберігати дані в колекції, а `__iter__()` реалізовувати як generator function або повертати окремий клас-iterator. Тоді кожна вкладена ітерація отримає власний незалежний cursor і не конфліктуватиме з іншими.

```python
class MyCollection:
    def __init__(self, data):
        self._data = data
    def __iter__(self):
        for item in self._data:
            yield item
```

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
