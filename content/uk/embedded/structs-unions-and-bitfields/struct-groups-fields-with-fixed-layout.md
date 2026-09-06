---
id: emb-structs-0001
title: "Що таке `struct` у C і для чого вона потрібна в embedded?"
description: "struct групує кілька полів різних типів в один об'єкт із фіксованим порядком оголошення полів."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

**`struct`** групує кілька полів різних типів в один об'єкт із фіксованим порядком оголошення полів.

У embedded структури використовують для peripheral register maps, protocol frames, driver state, configuration blocks і DMA descriptors. Важливо: структура має не лише логічні поля, а й фізичний layout у пам'яті: offsets, padding, alignment.

Правило: коли структура перетинає межу з hardware, binary protocol або Flash layout, її розмір і offsets треба перевіряти явно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
