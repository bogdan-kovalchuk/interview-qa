---
id: emb-structs-0042
title: "Що робить `alignas`/`_Alignas` або compiler-specific alignment attribute?"
description: "Встановлює або підсилює вимогу вирівнювання об'єкта чи типу."
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

**Встановлює або підсилює вимогу вирівнювання об'єкта чи типу**.

У embedded це потрібно для DMA buffers, cache line alignment, vector tables або периферійних вимог. Наприклад, DMA descriptor може вимагати 16-byte alignment; cache maintenance на Cortex-M7 часто працює по cache lines.

Правило: alignment – частина hardware contract. Перевіряй адресу runtime або compile-time і описуй вимогу в типі/attribute/linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
