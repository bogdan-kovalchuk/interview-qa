---
id: emb-dtypes-0059
title: "What does `const` mean in `const uint32_t *p` vs `uint32_t * const p`?"
description: "const before the type protects the pointed-to data; const after the protects the pointer's address itself."
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

`const uint32_t *p` - pointer to **constant uint32_t**: you cannot change `*p`, but you can change `p` (point to a different location).

`uint32_t * const p` - **constant pointer**: the address is fixed, but `*p` can be changed.

`const uint32_t * const p` - both the data and the address are immutable.

Rule: read right to left. For registers: `volatile uint32_t * const REG = (volatile uint32_t*)0x40020000U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
