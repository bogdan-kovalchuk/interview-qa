---
id: py-testing-0008
title: "Коли parametrization краща за копіювання одного test body для кількох cases?"
description: "Parametrization краща, коли тестова логіка ідентична, а відрізняються лише вхідні дані та очікуваний результат."
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

**Parametrization краща, коли тестова логіка ідентична, а відрізняються лише вхідні дані та очікуваний результат.**[^py314-library-unittest] `@pytest.mark.parametrize` генерує окремий test item для кожного набору з інформативним ID у звіті (наприклад, `test_parse[empty_input]`), що полегшує локалізацію. Копіювання body дублює логіку, ускладнює maintenance і не дає окремих test IDs. <span class="warn">Якщо тестова логіка різна для різних cases – копіювання (або окремі тест-функції) чесніше, бо parametrization змушує підганяти body під спільний знаменник.</span>

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
