---
id: emb-dtypes-0088
title: "What does this look like in memory? `struct { uint32_t flags:1; uint32_t mode:3; uint32_t value:28; }`"
description: "The three bit-fields pack into a single uint32t, but the bit-packing order is implementation-defined."
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
---

## Short answer

The field widths sum to 32 bits, but the standard does not guarantee that the structure occupies exactly one `uint32_t` or four bytes. Bit-field allocation order, allocation units, and alignment are implementation-defined; even whether fields proceed from the least- or most-significant bit is not portable. For a register or protocol format, use explicit masks and shifts on a fixed-width integer.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
