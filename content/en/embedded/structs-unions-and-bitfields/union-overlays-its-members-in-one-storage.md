---
id: emb-structs-0014
title: "What is a `union` in C?"
description: "A union stores several alternative fields in the same memory area; the union size equals the size of the largest member, accounting for alignment."
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

**`union`** stores several alternative fields in the same memory area; the union size equals the size of the largest member, accounting for alignment.

Unlike a struct, union fields do not lie sequentially. All members start at offset 0 and overlap. Writing to one member changes the bytes visible through other members.

Embedded use cases: variant data, register views, protocol payload alternatives, raw byte access with caution about aliasing and endianness.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
