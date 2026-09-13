---
id: emb-align-0042
title: "How can `__attribute__((aligned))` and `packed` work together?"
description: "packed reduces padding inside a type while aligned(N) sets the minimum alignment of the object itself; use them together for compact yet properly addressed layouts."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-13
content_revision: 2
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

**`packed` reduces padding within a type, and `aligned(N)` sets the minimum alignment of the object or type.**

That helps for wire headers or DMA (direct memory access) descriptors, where the layout must be compact but the start address must suit the hardware. For MMIO (memory-mapped I/O) register blocks <span class="warn">do not apply `packed` automatically</span>: registers sit at natural 32-bit offsets, and gaps are better described with reserved fields.

Rule: `packed` controls layout, `aligned` the base address; for register maps check access width and `offsetof`.[^embeddedinterviewlab]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
