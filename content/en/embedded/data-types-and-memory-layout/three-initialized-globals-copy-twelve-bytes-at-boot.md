---
id: emb-dtypes-0085
title: "How many bytes does startup code copy for these globals? `int a=1; int b=2; int c=3;`"
description: "All three are initialized globals in .data, so startup code copies 12 bytes (3 sizeof(int)) from Flash to RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
  - source_id: gnu-ld-lma
    title: "GNU ld manual: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains LMA/VMA and startup copying of initialized data; the linker script determines which bytes belong to the section."
---

## Short answer

The exact count depends on the ABI and `.data` contents; with 32-bit `int` and only these three objects, their values occupy 12 bytes.[^iso-c-n1570] [^gnu-ld-lma]

In a typical bare-metal layout, values are copied from an LMA in Flash to a VMA in RAM, but startup code copies the linker-script-defined `.data` range, which need not consist of only these variables or exactly 12 bytes.[^gnu-ld-lma]

Zero-initialized objects are often placed in `.bss`, but this is a toolchain convention, not a C guarantee.[^gnu-ld-lma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
