---
id: emb-align-0036
title: "Чому masks+shifts над `uint32_t` портативніші за union/bitfields для парсингу полів?"
description: "Арифметичні зсуви й маски дають однаковий результат незалежно від endianness і компілятора."
track: embedded
section: memory-alignment-and-endianness
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

**Арифметичні зсуви й маски дають однаковий результат незалежно від endianness і компілятора.**

`(reg >> 4) & 0x7` завжди витягне ті самі логічні біти значення, тоді як union-overlay і bitfields залежать від byte/bit order платформи.

Правило: для register decode і protocol parsing працюй зі значенням через shift/mask, а не з його байтовим layout у пам'яті.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
