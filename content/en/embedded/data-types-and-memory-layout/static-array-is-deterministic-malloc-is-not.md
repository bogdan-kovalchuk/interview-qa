---
id: emb-dtypes-0092
title: "What is the difference between `malloc` and a static array for a buffer in embedded?"
description: "A static array has a size known in advance; malloc allocates memory at runtime and can fail."
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

Static arrays have a size and storage duration known in advance; placement in `.bss` or `.data` depends on initialization and the linker script. `malloc(256)` requests a block at runtime and may fail, returning a null pointer that must be checked. Allocator timing and ISR suitability depend on the implementation and timing requirements; safety projects often restrict dynamic memory, but this is not a universal MISRA or IEC 61508 requirement.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
