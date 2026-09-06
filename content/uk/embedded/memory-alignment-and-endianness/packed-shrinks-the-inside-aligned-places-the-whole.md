---
id: emb-align-0042
title: "Як `__attribute__((aligned))` і `packed` можуть працювати разом?"
description: "packed зменшує padding усередині типу, а aligned(N) задає мінімальне вирівнювання самого об'єкта або типу."
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

**`packed` зменшує padding усередині типу, а `aligned(N)` задає мінімальне вирівнювання самого об'єкта або типу.**

Це може бути корисно для wire headers або DMA (direct memory access) descriptors, де layout має бути щільним, але початкова адреса повинна бути вирівняна для апаратури. Водночас для MMIO (memory-mapped I/O) register blocks не варто автоматично ставити `packed`: регістри зазвичай мають природні 32-bit offsets, а пропуски краще описувати reserved fields.

Правило: `packed` відповідає за layout, `aligned` – за базову адресу; для register maps перевіряй ширину доступу й `offsetof`, а не просто пакуй структуру.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
