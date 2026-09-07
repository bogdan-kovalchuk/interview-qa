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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Arrange fields from largest alignment to smallest**.

For example, instead of `uint8_t, uint32_t, uint8_t`, prefer `uint32_t, uint8_t, uint8_t`. This does not change semantics as long as the struct is not an external ABI or wire-format contract, but it can significantly reduce the size of an array of structs.

Rule: for internal data structures, optimize field order; for protocol or register layouts, the order must match the specification, even if there is padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
