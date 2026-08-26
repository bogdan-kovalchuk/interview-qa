---
id: py-testing-0019
title: "Що означає surviving mutant після штучної зміни behavior коду і як це виявляє слабкі assertions чи missing cases?"
description: "Surviving mutant – мутація (заміна оператора, літералу, контролю потоку), після якої жоден тест не впав; це означає, що тестовий suite не перевіряє змінену поведінку."
track: python
section: testing
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

**Surviving mutant – мутація (заміна оператора, літералу, контролю потоку), після якої жоден тест не впав; це означає, що тестовий suite не перевіряє змінену поведінку.**[^py314-library-unittest] Наприклад, якщо заміна `<` на `<=` не ламає жодного тесту – відсутній тест на граничне значення. Mutation testing (mutmut) автоматизує цей пошук: кожен survivor вказує на конкретний пропуск у assertions або missing test case.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
