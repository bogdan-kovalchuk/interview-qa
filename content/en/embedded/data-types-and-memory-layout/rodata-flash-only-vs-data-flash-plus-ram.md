---
id: emb-dtypes-0072
title: "What is the resource difference between `.rodata` in Flash and `.data` in RAM?"
description: "The linker script determines whether constants reside in Flash, while initialized data is often copied from Flash to RAM."
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
  - source_id: gnu-ld
    title: "The GNU linker: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.pdf
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes VMA, LMA, and copying initialized sections in GNU ld linker-script examples; other linkers and memory maps may differ."
---

## Short answer

**`.rodata`** is often placed in Flash by the linker script; the section name alone does not guarantee it. If the CPU reads it directly, the table needs no RAM copy.[^gnu-ld]

For initialized `.data`, startup code often copies initial bytes from Flash (LMA) to RAM (VMA), using space in both memories; the linker script and startup code define this.[^gnu-ld]

`const` does not guarantee Flash placement; check the linker map and MCU capabilities.[^gnu-ld]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
