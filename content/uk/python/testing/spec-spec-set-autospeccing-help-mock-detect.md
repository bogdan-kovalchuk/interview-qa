---
id: py-testing-0012
title: "Як `spec`, `spec_set` та autospeccing допомагають mock виявляти drift від real interface?"
description: "spec обмежує доступ лише атрибутами реального об'єкта, spec_set додатково забороняє встановлювати неіснуючі атрибути, а autospeccing рекурсивно копіює інтерфейс і сигнатури."
track: python
section: testing
level: middle
type: mechanism
tags: [spec, spec-set]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/testing.md#L190-L211
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`spec` обмежує доступ лише атрибутами реального об'єкта, `spec_set` додатково забороняє встановлювати неіснуючі атрибути, а autospeccing рекурсивно копіює інтерфейс і сигнатури.**[^py314-library-unittest] Завдяки цьому звернення до видаленого/перейменованого методу чи виклик із неправильною кількістю аргументів підніме `AttributeError` / `TypeError` у тесті, а не пройде непомічено.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
