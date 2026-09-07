---
id: emb-align-0033
title: "Чому `memcpy` для multi-byte доступу безпечніший за typed-pointer cast?"
description: "memcpy не має вимоги вирівнювання для джерела/призначення і не порушує strict aliasing."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 3
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

**`memcpy` не має вимоги вирівнювання** для джерела/призначення і не порушує strict aliasing.

Компілятор оптимізує `memcpy` фіксованого розміру в ефективні load/store (а на M0 – у безпечні побайтові доступи), тож ти отримуєш і коректність, і швидкість.

Правило: для unaligned читання/запису багатобайтових значень `memcpy` – стандартний портативний інструмент.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
