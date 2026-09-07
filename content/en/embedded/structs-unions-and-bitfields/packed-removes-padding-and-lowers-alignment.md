---
id: emb-structs-0011
title: "What is a `packed` struct?"
description: "A packed structure asks the compiler not to insert normal padding between fields or to reduce the struct alignment."
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

**Packed structure** asks the compiler not to insert normal padding between fields or to reduce the struct alignment.

This is useful for wire-format headers, on-flash records, or a precisely specified binary layout. But packed can cause unaligned accesses: a `uint32_t` field may end up at offset 1, which on some MCUs is slow or even faults.

Rule: packed is applied at format boundaries, not as a universal way to save RAM. For internal data, it is better to reorder fields.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
