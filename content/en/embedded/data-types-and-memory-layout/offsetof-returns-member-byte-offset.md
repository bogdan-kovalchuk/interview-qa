---
id: emb-dtypes-0054
title: "What is `offsetof()` for, and where is it defined?"
description: "offsetof(type, member) returns a field's byte offset from the struct's start and is defined in stddef.h."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`offsetof(type, member)` returns the field's offset from the start of the struct in bytes. Defined in `<stddef.h>`.

Usage:
1. Compile-time layout check: `static_assert(offsetof(CanFrame, crc) == 6, "Wrong layout");`
2. Serialization/deserialization;
3. **container_of** macro (Linux kernel) - obtain a struct* from a member*.

Critical for binary protocol and hardware register mapping.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
