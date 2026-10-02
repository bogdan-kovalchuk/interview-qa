---
id: emb-dtypes-0052
title: "How much memory does a union take, and how is its size computed?"
description: "A union's size equals its largest member's size plus any padding needed for alignment."
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
  - source_id: gcc-attributes-packed
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes compiler-specific layout attributes; standard union size and alignment rules remain defined by the language implementation."
---

## Short answer

The C standard requires `sizeof(union)` to be sufficient for its largest member, but the exact value and alignment are implementation-defined; do not use a universal “largest plus padding” formula.[^iso-c-n1570]

All union members occupy the same memory region.

For example, `union { char c; int x; double d; }` has size at least `sizeof(double)`, but the claim “exactly 8” depends on the ABI.

At a time, a union stores a value of no more than one member; rules for reading a different member depend on the language and case.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
