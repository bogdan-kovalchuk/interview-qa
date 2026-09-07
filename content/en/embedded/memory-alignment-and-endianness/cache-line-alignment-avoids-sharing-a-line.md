---
id: emb-align-0027
title: "Why align a buffer to a cache line?"
description: "To prevent false sharing and DMA incoherency by keeping data off shared cache lines."
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

## Short answer

**So that data does not share a cache line with anything else, avoiding false sharing and DMA incoherency.**

On cores with a cache (Cortex-M7/A), a buffer not aligned to a cache line may be partially cached; during DMA this leads to reading stale data unless you perform clean/invalidate. A cache-line-aligned buffer simplifies maintenance operations.

Rule: on cached cores, align DMA buffers to a cache line (32/64 bytes) and manage the cache explicitly.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
