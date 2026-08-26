---
id: py-compfn-0004
title: "Чому groups, які повертає `itertools.groupby()`, потрібно спожити або матеріалізувати до переходу до наступної group?"
description: "Кожна group – це iterator, який shares the underlying iterable з groupby(); при переході до наступної групи попередній iterator стає порожнім."
track: python
section: comprehensions-and-functional
level: middle
type: pitfall
tags: [itertools-groupby]
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
---

## Short answer

**Кожна group – це iterator, який shares the underlying iterable з `groupby()`; при переході до наступної групи попередній iterator стає порожнім.**[^py314-howto-functional] Тому збереження об'єкта group без матеріалізації (наприклад, у `list`) призведе до порожнього результату при подальшому споживанні. <span class="warn">Типова помилка: `groups = [(k, g) for k, g in groupby(data, key)]`, після якої всі `g` вже вичерпані.</span>

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
