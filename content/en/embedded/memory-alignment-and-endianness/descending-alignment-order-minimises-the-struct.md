---
id: emb-align-0029
title: "How do you reorder `uint64_t, uint8_t, uint32_t, uint8_t` to minimise the size?"
description: "From largest alignment to smallest: uint64t, uint32t, uint8t, uint8t."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

**From largest alignment to smallest: `uint64_t, uint32_t, uint8_t, uint8_t`.**

This gives: `u64`@0(8) + `u32`@8(4) + `u8`@12 + `u8`@13 + 2 tail -> 16 bytes. The original order would have produced 24 bytes due to padding after `uint8_t`.

Rule: "largest first" almost always yields the minimum size without packed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
