---
id: emb-dtypes-0099
title: "Why use `static_assert` when working with structs in embedded systems?"
description: "staticassert checks sizeof and offsetof of structs at compile time, guaranteeing they match the protocol."
track: embedded
section: data-types-and-memory-layout
level: middle
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

`static_assert` (C11 `_Static_assert`, C++ `static_assert`) checks a condition **at compile time** -> error if false.

For embedded: `static_assert(sizeof(CanFrame) == 13, "Wrong CAN frame size");`
`static_assert(offsetof(UartPacket, crc) == 6, "CRC offset mismatch");`

Guarantees that the struct layout matches the protocol or hardware register map regardless of compiler, ABI, or flag changes.

Best practice: every protocol struct should have `static_assert` on `sizeof` and `offsetof`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
