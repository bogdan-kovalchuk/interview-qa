---
id: emb-dtypes-0002
title: "Which memory section does this go into? `const uint32_t FIRMWARE_VERSION = 0x0102;`"
description: "A typical layout may place a const object in .rodata, but the compiler and linker script determine its actual location."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "Binutils 2.47"
    applicability: "GNU ld documentation shows how linker scripts map sections to run-time and load addresses; actual placement depends on the target and specific script."
---

## Short answer

A typical embedded layout places `const uint32_t FIRMWARE_VERSION = 0x0102;` in read-only storage, often `.rodata` in Flash. In C, however, `const` prevents modification through that lvalue; it does not instruct the linker to choose `.rodata` or guarantee zero RAM use. Actual placement depends on the compiler, how the object is used, and the linker script.[^embedded-ld-layout]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
