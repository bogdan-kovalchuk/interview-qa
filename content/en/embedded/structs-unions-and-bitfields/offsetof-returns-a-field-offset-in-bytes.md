---
id: emb-structs-0007
title: "What is `offsetof` and what is it needed for?"
description: "offsetof(T, field) returns the offset of a field inside a struct in bytes."
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

**`offsetof(T, field)`** returns the offset of a field inside a struct in bytes.

This is the standard way to verify layout without manual assumptions. In embedded, it is used for static assertions of register maps, protocol headers, Flash records, and DMA descriptors.

Rule: if the hardware manual says `STATUS` must be at offset `0x10`, verify it with `_Static_assert(offsetof(Type, STATUS) == 0x10, "...")`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
