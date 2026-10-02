---
id: emb-dtypes-0004
title: "What is the `.bss` section and how does it differ from `.data`?"
description: "In a typical embedded layout, startup code zeros .bss in RAM and copies .data initial values from Flash."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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
    applicability: "GNU ld documentation describes section mapping and the conventional startup copy/zero operations; exact names and mappings are target-specific."
---

## Short answer

In a typical embedded image, `.bss` describes global or `static` objects whose initial value is zero, while `.data` holds objects with nonzero initial values. Startup code commonly zeroes the `.bss` range in RAM and copies `.data` initial bytes from ROM/Flash into RAM; the linker script defines the exact layout.[^embedded-ld-layout]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
