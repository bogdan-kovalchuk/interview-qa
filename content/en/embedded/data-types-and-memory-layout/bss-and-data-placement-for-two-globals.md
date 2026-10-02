---
id: emb-dtypes-0008
title: "Which memory section: `uint32_t error_count;` (global) and `uint32_t sensor_count = 5;` (global)?"
description: "In a typical linker layout, a zero-initialized global goes in .bss and a nonzero-initialized one in .data."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GNU ld example with distinct .data VMA/LMA, copying into RAM, and zeroing .bss; this is linker layout, not a C language requirement."
---

## Short answer

`error_count` has static storage duration and zero initialization, so it typically goes in `.bss`; startup code sets that region to zero. `sensor_count` has a nonzero initial value, so a common embedded linker layout places it in `.data`: its initial bytes are stored at a load address and copied to its runtime address. The toolchain and linker script define the exact sections and addresses.[^gnu-ld-data]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
