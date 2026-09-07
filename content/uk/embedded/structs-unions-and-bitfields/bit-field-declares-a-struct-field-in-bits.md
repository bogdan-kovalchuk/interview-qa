---
id: emb-structs-0020
title: "Що таке bit-field у C struct?"
description: "Bit-field дозволяє оголосити поле структури з кількістю бітів, наприклад unsigned mode : 3;."
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

**Bit-field** дозволяє оголосити поле структури з кількістю бітів, наприклад `unsigned mode : 3;`.

Компілятор пакує такі поля в storage unit базового типу, але точний порядок бітів, signedness деяких типів і crossing storage units є implementation-defined. Це зручно для компактних flags, але ризиковано для hardware register layout і wire format.

Правило: bit-fields підходять для internal flags; для hardware/protocol layout їх треба використовувати лише з повним розумінням ABI компілятора.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
