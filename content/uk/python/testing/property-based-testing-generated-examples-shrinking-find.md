---
id: py-testing-0016
title: "Коли property-based testing з generated examples і shrinking дає кращий пошук edge cases, ніж лише hand-picked examples?"
description: "Property-based testing ефективний, коли простір вхідних даних великий, а граничні випадки неочевидні: бібліотека генерує сотні випадкових прикладів і згортає (shrinking) найменший контрприклад."
track: python
section: testing
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
---

## Short answer

**Property-based testing ефективний, коли простір вхідних даних великий, а граничні випадки неочевидні: бібліотека генерує сотні випадкових прикладів і згортає (shrinking) найменший контрприклад.**[^py314-library-unittest] Наприклад, Hypothesis для тесту інваріанту «сортування зберігає довжину» автоматично знайде порожній список або список з одного елемента як мінімальний failing case, тоді як hand-picked приклади можуть пропустити такий edge case.

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
