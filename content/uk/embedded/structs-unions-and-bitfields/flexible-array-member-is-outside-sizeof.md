---
id: emb-structs-0052
title: "Чому `sizeof(struct with flexible array)` не дорівнює повному packet size?"
description: "Бо flexible array member не має compile-time розміру і не входить у sizeof."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

**Бо flexible array member не має compile-time розміру і не входить у `sizeof`.**

`sizeof(struct Packet)` повертає лише розмір header-а до payload, можливо з padding перед `data[]`. Реальний packet size треба рахувати як `sizeof(struct Packet) + payload_len`.

Правило: flexible array member описує layout prefix, а не володіє storage автоматично.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
