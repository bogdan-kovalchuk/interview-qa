---
id: py-itergen-0007
title: "Чому generator pipeline може зменшити peak memory, але не обов’язково total execution time?"
description: "Кожен stage pipeline обробляє один елемент за раз, тому в пам’яті одночасно перебуває лише O(1) елементів замість усієї послідовності."
track: python
section: iterators-and-generators
level: middle
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
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Кожен stage pipeline обробляє один елемент за раз, тому в пам’яті одночасно перебуває лише O(1) елементів замість усієї послідовності.**[^py314-library-stdtypes-iterator-types] Загальний час виконання не зменшується, бо кожен елемент проходить усі stage, а overhead на створення/відновлення generator frames може навіть уповільнити виконання порівняно з eager list construction. Trade-off: менше пам’яті – потенційно більше часу.

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
