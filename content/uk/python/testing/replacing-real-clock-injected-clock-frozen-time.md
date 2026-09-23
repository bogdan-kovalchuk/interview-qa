---
id: py-testing-0015
title: "Як заміна real clock на injected clock або frozen time робить timeout і expiry tests детермінованими?"
description: "Замість time.sleep() і реального очікування тест керує абстракцією годинника, тому timeout, TTL та expiry перевіряються миттєво й без flakiness."
track: python
section: testing
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

**Замість `time.sleep()` і реального очікування тест керує абстракцією годинника, тому timeout, TTL та expiry перевіряються миттєво й без flakiness.**[^py314-library-unittest] Код приймає clock-об'єкт (або використовується `freezegun` / `time_machine` для замороження `datetime.now()`), і тест переводить час на потрібну точку. Це усуває race conditions і залежність від завантаженості CI.

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
