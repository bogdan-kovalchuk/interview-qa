---
id: emb-structs-0004
title: "How do you reduce padding in a struct without `packed`?"
description: "Arrange fields from largest alignment to smallest."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Group fields by alignment, often from larger to smaller**.

For example, placing `uint32_t` before two `uint8_t` fields is often more space-efficient than `uint8_t, uint32_t, uint8_t`. Exact padding and size depend on the ABI; field order also changes offsets and can therefore break an ABI or data format.

For internal structures, choose an order that accounts for alignment when compatible with how the structure is used. A protocol or register map follows its specification, not a memory optimization.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
