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

**`offsetof(T, field)`** returns the offset of a field inside a struct in bytes.

This standard macro from `<stddef.h>` can verify layout without manual counting. In embedded, it is used in static assertions for register maps, protocol headers, Flash records, and DMA descriptors.

If the hardware manual specifies `STATUS` at offset `0x10`, this can be checked with `_Static_assert(offsetof(Type, STATUS) == 0x10, "...")`. `offsetof` must not be used with bit-field members.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
