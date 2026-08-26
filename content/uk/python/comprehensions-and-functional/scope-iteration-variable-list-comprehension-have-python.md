---
id: py-compfn-0001
title: "Яку scope має iteration variable у list comprehension на Python 3 і чи замінює вона однойменний outer variable?"
description: "Iteration variable у list comprehension виконується в окремій неявній вкладеній scope і не витікає в enclosing scope."
track: python
section: comprehensions-and-functional
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

**Iteration variable у list comprehension виконується в окремій неявній вкладеній scope і не витікає в enclosing scope.**[^py314-howto-functional] Тому однойменна зовнішня змінна зберігає своє значення: після `x = 99; result = [x for x in range(3)]` змінна `x` дорівнює `99`, а не `2`. Це відрізняє comprehension від звичайного циклу `for`, де iteration variable залишається в поточній scope.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
