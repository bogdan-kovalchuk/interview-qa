---
id: emb-dtypes-0038
title: "What does startup code do with the `.data` section before calling `main()`?"
description: "In a typical GNU toolchain, startup code copies the initial .data values from Flash (LMA) into RAM (VMA) before main() runs."
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
  - source_id: gnu-ld-lma-vma
    title: "GNU ld documentation: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Defines LMA and VMA and describes a GNU ld example where a section loads from ROM but runs from RAM; it does not prescribe a startup sequence for every MCU."
---

## Short answer

In a typical bare-metal GNU toolchain, startup code copies initial `.data` values from Flash (LMA - Load Memory Address) to RAM (VMA - Virtual Memory Address); this is a common convention, not a universal requirement.[^gnu-ld-lma-vma]

For example, initializer `uint32_t x = 42;` is stored in the program image, then its representation is copied to RAM; byte order is platform-dependent.

A GNU startup file may copy with `memcpy(&_sdata, &_sidata, &_edata - &_sdata);`, then zero `.bss` with `memset(&_sbss, 0, &_ebss - &_sbss);`.[^gnu-ld-lma-vma]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
