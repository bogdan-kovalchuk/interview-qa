---
id: emb-align-0026
title: "What does `_Alignas` / `alignas` do and what for?"
description: "Sets an increased alignment requirement for a variable, needed for DMA and cache-line alignment."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
_Alignas(32) uint8_t dma_buf[256];
```

## Short answer

**Sets an increased alignment requirement for a variable.**

Needed when hardware demands it: DMA buffers, cache-line alignment (32/64 bytes) for lock-free structures, special peripheral blocks.

Rule: align DMA and cache-sensitive buffers explicitly via `_Alignas` (or `__attribute__((aligned(N)))`); do not rely on a "lucky" layout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
