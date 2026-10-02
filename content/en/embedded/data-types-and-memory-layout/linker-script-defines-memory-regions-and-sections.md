---
id: emb-dtypes-0069
title: "What is a linker script, and what role does it play in placing sections?"
description: "A linker script maps input sections to output sections and memory regions; the actual layout depends on the script and target."
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
  - source_id: gnu-ld-scripts
    title: "GNU ld: Scripts"
    url: https://sourceware.org/binutils/docs/ld/Scripts.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes linker script purpose and MEMORY command; syntax and startup conventions can be toolchain-specific."
  - source_id: gnu-ld-memory
    title: "GNU ld: MEMORY Command"
    url: https://sourceware.org/binutils/docs/ld/MEMORY.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes memory region declarations and placement constraints for GNU ld."
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes mapping input sections to output sections and placing them."
  - source_id: gnu-ld-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes load versus runtime addresses and AT/AT> syntax."
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

**Linker script** (`.ld` file) describes how the linker maps input sections into output sections and controls memory layout; `MEMORY` names available regions and `SECTIONS` places output sections.[^gnu-ld-scripts]

For example, `MEMORY` can describe named memory regions:
`FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K`
`RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K`.

`SECTIONS` defines placement rules:
`.text : { *(.text*) } > FLASH`
`.data : { *(.data*) } > RAM AT> FLASH`

The linker does not automatically generate symbols such as `_sdata`, `_edata`, and `_sidata`; a particular script commonly defines these for startup code that copies `.data` from its load address into RAM.[^gnu-ld-lma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
