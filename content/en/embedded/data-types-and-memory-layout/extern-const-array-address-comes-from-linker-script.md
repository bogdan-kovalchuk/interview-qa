---
id: emb-dtypes-0093
title: "How does a linker script assign an address to `extern const uint8_t image_data[]`?"
description: "A linker script can place an input data section and export a symbol that C code treats as the array address."
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
  - source_id: gnu-ld-symbols
    title: "GNU ld: Source Code Reference"
    url: https://sourceware.org/binutils/docs/ld/Source-Code-Reference.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Explains that a linker-script-defined symbol is an address without a separate object and how C refers to it; specific to GNU ld."
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
    accessed: 2026-10-04
    kind: official
    version: "2.47"
    applicability: "Describes input/output section mapping and output-section placement in GNU ld; the script specifies the concrete memory map."
---

## Short answer

The declaration `extern const uint8_t image_data[];` does not define the array; the linker resolves the symbol in the linked image. Its physical address and section depend on the linker script and target, so it is not necessarily Flash or `.rodata`. In GNU `ld`, a script-defined symbol is an address without a separate object, so code commonly declares it as an array and reads from that address.[^gnu-ld-symbols]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
