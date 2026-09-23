---
id: py-testing-0017
title: "Чому 100% line coverage не доводить, що всі important behaviors та assertions перевірені?"
description: "Line coverage показує лише рядки, які виконались, але не перевіряє, чи assertions дійсно валідують правильну поведінку."
track: python
section: testing
level: middle
type: pitfall
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

**Line coverage показує лише рядки, які виконались, але не перевіряє, чи assertions дійсно валідують правильну поведінку.**[^py314-library-unittest] Тест може пройти всі гілки коду з порожнім тілом або хибним `assert True`, і coverage буде 100%, але жодна помилка не буде виявлена. Потрібно перевіряти branch coverage, mutation testing та якість самих assertions.

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
