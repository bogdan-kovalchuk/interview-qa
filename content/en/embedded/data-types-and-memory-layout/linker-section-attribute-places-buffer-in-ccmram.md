---
id: emb-dtypes-0050
title: "What does this do? `__attribute__((section(\".ccmram\"))) uint32_t fast_buf[256];`"
description: "The section attribute asks the compiler to put the array in .ccmram; the linker script determines its placement."
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
  - source_id: gcc-common-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains that the section attribute assigns a variable to an object-file section; physical placement and support depend on the linker and platform."
---

## Short answer

GCC's `section(".ccmram")` attribute asks the compiler to put a global array in the named `.ccmram` input section; by itself it assigns no RAM address and guarantees neither speed nor DMA compatibility. The linker script must map that section to available memory, and startup code must handle its initialization correctly.[^gcc-common-attributes]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
