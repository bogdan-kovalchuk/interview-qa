---
id: emb-align-0027
title: "Навіщо вирівнювати буфер по cache line?"
description: "Щоб дані не ділили cache line з іншими – уникнути false sharing і неузгодженості при DMA (direct memory access)."
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

**Щоб дані не ділили cache line з іншими – уникнути false sharing і неузгодженості при DMA (direct memory access).**

На ядрах з кешем (Cortex-M7/A) невирівняний по line буфер може частково кешуватися; при DMA це призводить до читання застарілих даних, якщо не зробити clean/invalidate. Cache-line-aligned буфер спрощує maintenance операції.

Правило: DMA-буфери на кешованих ядрах вирівнюй по cache line (32/64B) і керуй кешем явно.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
