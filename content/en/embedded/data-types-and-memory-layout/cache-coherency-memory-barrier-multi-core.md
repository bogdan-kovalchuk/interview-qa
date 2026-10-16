---
id: emb-dtypes-0106
title: "What are cache coherency and memory barrier in a multi-core MCU, MPU, or Embedded Linux system?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-memory-barriers
    title: "Linux kernel memory barriers"
    url: https://docs.kernel.org/core-api/wrappers/memory-barriers.html
---

## Short answer

**Cache coherency** means consistency of data between CPU caches, DMA, and peripheral views of memory. A **memory barrier** enforces memory-operation order, but does not by itself clean or invalidate the cache. <span class="warn">DMA needs the cache-maintenance operations and barriers specified by the platform; coherent DMA memory also requires correct ordering.</span>[^linux-memory-barriers]

## Detailed explanation

TODO
