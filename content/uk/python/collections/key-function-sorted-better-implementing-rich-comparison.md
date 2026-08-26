---
id: py-coll-0021
title: "Коли key function у `sorted()` краща за реалізацію rich comparison methods у domain class?"
description: "Key function краща, коли порядок сортування залежить від контексту або зовнішніх даних, а не від природного порядку самого класу."
track: python
section: collections
level: senior
type: comparison
tags: [sorted]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Key function краща, коли порядок сортування залежить від контексту або зовнішніх даних, а не від природного порядку самого класу.**[^py314-library-stdtypes] Rich comparison methods (наприклад, `__lt__`) визначають єдиний канонічний порядок класу; key function дозволяє сортувати за будь-яким похідним ключем без зміни класу. Наприклад, `sorted(users, key=lambda u: scores[u.id])` сортує за зовнішнім словником, що неможливо виразити через `__lt__`.

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
