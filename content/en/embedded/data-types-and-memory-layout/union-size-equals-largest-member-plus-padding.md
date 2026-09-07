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

`sizeof(union)` = **largest member's size** + trailing padding to satisfy alignment.

All union members occupy the same memory region.

Example: `union { char c; int x; double d; }` -> sizeof = 8 (double is the largest, align = 8).

Useful for: type punning, variant types, byte-level inspection. In C++, only one member can be active at a time.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
