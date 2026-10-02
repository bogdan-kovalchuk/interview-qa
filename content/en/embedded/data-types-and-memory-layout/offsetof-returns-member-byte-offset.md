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

`offsetof(type, member)` from `<stddef.h>` returns the byte offset of an ordinary structure member from the start; it cannot be applied to a bit-field.[^iso-c-n1570]

Usage:
1. Layout check: `static_assert(offsetof(CanFrame, crc) == 6, "Wrong layout");` (if that is genuinely required by a particular ABI/protocol).
2. Serialization/deserialization;
3. **container_of** macro (Linux kernel) - obtain a struct* from a member*.

The value depends on the implementation's layout; the macro itself does not define a protocol layout.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
