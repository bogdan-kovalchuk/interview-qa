---
id: emb-align-0026
title: "Що робить `_Alignas` / `alignas` і навіщо?"
description: "Задає підвищену вимогу вирівнювання для змінної."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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

## Question code

```c
_Alignas(32) uint8_t dma_buf[256];
```

## Short answer

**Задає підвищену вимогу вирівнювання для змінної.**

Потрібно, коли апаратура цього вимагає: DMA (direct memory access) буфери, cache-line-вирівнювання (32/64 байти) для lock-free структур, спеціальні периферійні блоки.

Правило: вирівнюй DMA/cache-чутливі буфери явно через `_Alignas` (або `__attribute__((aligned(N)))`), не покладайся на «щасливий» layout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
