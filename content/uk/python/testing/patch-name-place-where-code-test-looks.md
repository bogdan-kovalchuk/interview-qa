---
id: py-testing-0011
title: "Чому під час `patch()` треба замінювати name там, де його lookup робить code under test?"
description: "patch() змінює об'єкт, на який посилається ім'я в конкретному namespace, тому патчити треба те місце, звідки code under test це ім'я бере."
track: python
section: testing
level: middle
type: pitfall
tags: [patch]
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

**`patch()` змінює об'єкт, на який посилається ім'я в конкретному namespace, тому патчити треба те місце, звідки code under test це ім'я бере.**[^py314-library-unittest] Якщо модуль `b` робить `from a import SomeClass`, то `b` вже має власне посилання на клас, і `patch('a.SomeClass')` не вплине на код у `b`. Правильний патч – `patch('b.SomeClass')`.

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
