---
id: emb-dtypes-0106
title: "What are cache coherency and memory barrier in a multi-core MCU, MPU, or Embedded Linux system?"
description: "Cache coherency means data consistency between CPU caches, DMA, and peripheral views; a memory barrier enforces operation order, and DMA often needs cache clean/invalidate to avoid stale data."
track: embedded
section: data-types-and-memory-layout
level: senior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: linux-memory-barriers
    title: "Linux kernel memory barriers"
    url: https://docs.kernel.org/core-api/wrappers/memory-barriers.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains ordering, coherency, and the separate need for DMA cache maintenance in the Linux kernel context; it is not a universal MCU API."
---

## Short answer

**Cache coherency** means consistency of data between CPU caches, DMA, and peripheral views of memory. A **memory barrier** enforces memory-operation order, but does not by itself clean or invalidate the cache. <span class="warn">DMA needs the cache-maintenance operations and barriers specified by the platform; coherent DMA memory also requires correct ordering.</span>[^linux-memory-barriers]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
