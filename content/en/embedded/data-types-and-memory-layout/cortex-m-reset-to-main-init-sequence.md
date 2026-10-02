---
id: emb-dtypes-0007
title: "What is the C runtime init sequence before `main()` on Cortex-M?"
description: "The core obtains reset values from the Vector Table; startup code initializes memory and transfers control to the runtime before main()."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 4
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
  - source_id: cmsis-startup
    title: "CMSIS-Core startup file documentation"
    url: https://github.com/ARM-software/CMSIS_6/blob/main/CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md
    accessed: 2026-10-04
    kind: official
    version: "CMSIS_6 main"
    applicability: "Typical CMSIS startup-file roles: Reset_Handler, MSP, vectors, and transfer to runtime; exact order depends on vendor startup."
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GNU ld example with distinct .data VMA/LMA, copying into RAM, and zeroing .bss; this is linker layout, not a C language requirement."
---

## Short answer

After reset, a Cortex-M core obtains the initial `MSP` and `Reset_Handler` address from the Vector Table’s first entries; their addresses in memory depend on the specific MCU implementation. Startup code performs early system initialization, copies initialized data into RAM, zeroes zero-initialized regions, transfers control to the C/C++ runtime, and the runtime eventually calls `main()`. The exact order and copy tables depend on the startup file and toolchain.[^cmsis-startup] [^gnu-ld-data]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
