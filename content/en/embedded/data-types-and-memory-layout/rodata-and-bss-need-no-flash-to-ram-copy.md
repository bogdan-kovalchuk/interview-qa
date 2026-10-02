---
id: emb-dtypes-0048
title: "Which sections need a Flash-to-RAM copy at boot, and which don't?"
description: "In a typical bare-metal layout, startup code copies .data to RAM and zeros .bss; .rodata placement depends on the linker script."
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
  - source_id: embedded-gnu-ld
    title: "GNU ld: Using LD"
    url: https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_chapter/ld_3.html
    accessed: 2026-10-04
    kind: official
    version: "2.9.1 manual"
    applicability: "The linker script example explains LMA/VMA, copying initialized data, and zeroing .bss; actual startup behavior depends on the target system."
---

## Short answer

In a typical bare-metal layout, `.data` has initial values in the Flash image and a runtime address in RAM, so startup code copies its bytes; `.bss` reserves RAM that startup code zeros. Placement of `.rodata` and `.text` depends on the linker script and MCU capabilities, so section names alone do not guarantee Flash reads or execute-in-place behavior.[^embedded-gnu-ld]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
