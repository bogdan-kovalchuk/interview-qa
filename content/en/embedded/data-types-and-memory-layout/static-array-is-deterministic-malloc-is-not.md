---
id: emb-dtypes-0092
title: "What is the difference between `malloc` and a static array for a buffer in embedded?"
description: "A static array is deterministic and fragmentation-free, while malloc is non-deterministic and unsafe in an ISR."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Static array** (`static uint8_t buf[256]`): known at compile time, placed in `.bss`/`.data`, deterministic access, no fragmentation.

**malloc(256)**: runtime allocation, non-deterministic time, heap fragmentation, may return NULL (must be checked), unsafe in ISR.

In safety-critical embedded (MISRA, IEC 61508): <span class="warn">static allocation is mandatory</span>. `malloc` only during initialization – and only before the real-time part of execution.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
