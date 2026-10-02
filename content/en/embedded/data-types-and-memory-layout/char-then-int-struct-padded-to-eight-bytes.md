---
id: emb-dtypes-0010
title: "Under AAPCS32, what size does `struct { char c; int x; }` have?"
description: "Under AAPCS32, padding before the 4-byte int makes this structure occupy 8 bytes."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
  - source_id: aapcs32-layout
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "current"
    applicability: "Type sizes and alignment of composites under AAPCS32; the struct result applies only to this ABI and without packing overrides."
---

## Short answer

Under AAPCS32, `struct { char c; int x; }` is expected to occupy 8 bytes: `c` has offset 0, `x` offset 4, and there are 0 bytes of trailing padding. This follows from a 1-byte `char`, a 4-byte `int` aligned to 4 bytes, and struct alignment matching its strictest member; this is a target ABI result, not a general C language guarantee. Check the actual layout with `sizeof` and `offsetof`.[^aapcs32-layout]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
