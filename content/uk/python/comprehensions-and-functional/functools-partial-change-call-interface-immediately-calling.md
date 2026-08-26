---
id: py-compfn-0009
title: "Як `functools.partial` змінює call interface без негайного виклику wrapped callable?"
description: "functools.partial повертає новий callable-об'єкт, у якому частину positional або keyword arguments «заморожено», але оригінальна функція не викликається до виклику partial-об'єкта."
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: [functools-partial]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L65-L117
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`functools.partial` повертає новий callable-об'єкт, у якому частину positional або keyword arguments «заморожено», але оригінальна функція не викликається до виклику partial-об'єкта.**[^py314-howto-functional] Додаткові arguments при виклику доповнюють заморожені; нові keyword arguments мають пріоритет над попередньо заданими. Наприклад, `functools.partial(pow, 2)` створює функцію обчислення квадрата: `f(10)` -> `1024`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
