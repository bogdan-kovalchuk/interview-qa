---
id: py-compfn-0002
title: "У якому порядку обчислюються clauses у comprehension з кількома `for` та `if`?"
description: "Clauses обчислюються зліва направо, як вкладені цикли: кожен for – новий рівень вкладеності, а if фільтрує на поточному рівні."
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

**Clauses обчислюються зліва направо, як вкладені цикли: кожен `for` – новий рівень вкладеності, а `if` фільтрує на поточному рівні.**[^py314-howto-functional] Результат еквівалентний вкладеним `for`/`if` блокам зліва направо, де вираз-результат обчислюється щоразу на найглибшому рівні. Наприклад, `[(i,j) for i in range(3) for j in range(2) if (i+j) % 2 == 0]` дає `[(0, 0), (1, 1), (2, 0)]`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
