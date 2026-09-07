---
id: emb-structs-0032
title: "Що таке flexible array member?"
description: "Flexible array member – останнє поле структури з неповним розміром, наприклад uint8_t data[];."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 2
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

**Flexible array member** – останнє поле структури з неповним розміром, наприклад `uint8_t data[];`.

Воно дозволяє виділити один memory block: header + variable-length payload. `sizeof(struct Packet)` не включає bytes payload, лише header і можливий padding перед flexible array.

Правило: flexible array member має бути останнім полем і структура має мати принаймні ще одне named поле.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
