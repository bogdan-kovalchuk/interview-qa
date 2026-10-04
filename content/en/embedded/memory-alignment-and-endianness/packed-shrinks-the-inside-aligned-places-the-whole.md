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
updated: 2026-10-04
content_revision: 3
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-common-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Documents the GNU packed and aligned attributes; this is GCC documentation, not a portable C standard requirement."
---

## Short answer

**`packed` reduces padding within a type, and `aligned(N)` sets the minimum alignment of the object or type.**

That helps for wire headers or DMA descriptors, where the layout must be compact but the start address must suit the hardware. For MMIO (memory-mapped I/O) register blocks <span class="warn">do not apply `packed` automatically</span>: registers sit at natural 32-bit offsets, and gaps are better described with reserved fields.

Rule: in GCC, `packed` reduces member padding while `aligned(N)` sets minimum alignment; for register maps check access width and `offsetof`.[^gcc-common-attributes]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
