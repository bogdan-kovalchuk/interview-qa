---
id: emb-align-0037
title: "Навіщо під час розробки вмикати `UNALIGN_TRP` на M3/M4?"
description: "Щоб приховані misaligned доступи перетворити на явний fault, а не тихий штраф."
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

**Щоб приховані misaligned доступи перетворити на явний fault, а не тихий штраф.**

За замовчуванням M3/M4 можуть «прощати» частину misaligned access, тож баг, який зламає M0-порт або стане UB (undefined behavior) через typed-pointer cast у C, лишається непоміченим. `UNALIGN_TRP` (біт у `SCB->CCR`, System Control Block -> Configuration and Control Register) робить такі помилки видимими раніше.

Правило: вмикай trap у debug-збірці, щоб ловити переносимі alignment-баги ще до переходу на менше ядро.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
