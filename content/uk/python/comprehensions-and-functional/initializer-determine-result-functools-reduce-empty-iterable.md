---
id: py-compfn-0012
title: "Як initializer визначає result `functools.reduce()` для empty iterable і як left-to-right grouping змінює result неасоціативної operation?"
description: "Без initializer порожнє iterable дає TypeError; з initializer – результатом стає сам initializer, навіть якщо iterable порожній."
track: python
section: comprehensions-and-functional
level: senior
type: mechanism
tags: [functools-reduce]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L118-L132
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Без initializer порожнє iterable дає `TypeError`; з initializer – результатом стає сам initializer, навіть якщо iterable порожній.**[^py314-howto-functional] `reduce()` застосовує функцію зліва направо: `reduce(sub, [1, 2, 3])` обчислює `((1-2)-3) = -4`, а не `1-(2-3) = 2`. Для неасоціативних операцій (віднімання, ділення) порядок групування визначає результат, тому `reduce` завжди фіксує left-fold семантику. Додавання initializer зсуває стартовий акумулятор: `reduce(sub, [1, 2, 3], 0)` -> `(((0-1)-2)-3) = -6`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
