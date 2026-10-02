---
id: emb-dtypes-0083
title: "What does the `.data` section hold, and where do its startup values come from?"
description: ".data holds initialized globals whose startup values startup code copies from Flash (the LMA) into RAM."
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
    applicability: "Explains VMA/LMA and shows startup copying of initialized data from a ROM image to RAM; linker scripts define the actual symbol names."
---

## Short answer

In a typical bare-metal configuration, `.data` contains data that needs initial values in RAM; a linker script can give it an LMA in Flash and a VMA in RAM.[^gnu-ld-lma]

When LMA and VMA differ, startup code copies bytes from the image at the LMA into the RAM range at the VMA; the boundary symbols depend on the linker script.

Startup code commonly zeroes `.bss` afterward and then calls `main()`. The details depend on the runtime and linker script.[^gnu-ld-lma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
