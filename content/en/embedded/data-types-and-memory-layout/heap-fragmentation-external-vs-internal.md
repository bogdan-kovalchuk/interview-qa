---
id: emb-dtypes-0034
title: "What is heap fragmentation, and why is it critical for embedded systems?"
description: "Heap fragmentation scatters free memory into small blocks; without an MMU live blocks are not relocated, so embedded code often prefers static allocation or memory pools."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Shows adjacent free-block coalescing in heap_4; other allocators may differ."
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
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
---

## Short answer

Heap fragmentation occurs after multiple `malloc`/`free` calls: total free memory may be sufficient, but the largest contiguous block may be too small for a request, so `malloc` can return `NULL`.

**External**: many small free blocks. **Internal**: allocated block is larger than requested (alignment/metadata).

The absence of an MMU does not prevent an allocator from coalescing adjacent free blocks: for example, FreeRTOS `heap_4` does this. Moving live objects to compact memory is a separate allocator feature, and ordinary C pointers make such relocation difficult.[^freertos-heap]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
