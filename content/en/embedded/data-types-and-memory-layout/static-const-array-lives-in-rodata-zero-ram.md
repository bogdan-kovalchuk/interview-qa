---
id: emb-dtypes-0068
title: "Where is this stored inside a function? `static const uint16_t lookup[] = {1, 2, 3};`"
description: "static const sets storage duration and const qualification; the compiler and linker determine the actual memory placement."
track: embedded
section: data-types-and-memory-layout
level: junior
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
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes input/output section mapping and placement; section placement for a C declaration depends on the toolchain and linker script."
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

Inside a function, `static` gives the array static storage duration, while `const` prevents modification through that name; neither keyword alone guarantees `.rodata` placement or zero RAM use.[^iso-c-n1570] The compiler and linker script determine sections and addresses, so check the linker map.[^gnu-ld-sections]

On a typical embedded layout, an initialized read-only table can reside in Flash, while writable initialized data is copied from its load image into RAM at startup. The actual result depends on the compiler, linker script, and MCU memory map.[^gnu-ld-sections]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
