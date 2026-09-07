---
id: emb-dtypes-0018
title: "Draw the memory layout without packing: `struct { uint8_t a; uint32_t b; uint8_t c; }`"
description: "The compiler pads between the uint8t and uint32t fields, so the struct takes 12 bytes, not 6."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

`a` @ offset 0 (1B) -> <span class="warn">3B padding</span> -> `b` @ offset 4 (4B) -> `c` @ offset 8 (1B) -> <span class="warn">3B trailing padding</span>

Total: **12 bytes**. Trailing padding ensures correct alignment in an array: `arr[1].b` will also be at an address divisible by 4.

Optimization: `struct { uint32_t b; uint8_t a; uint8_t c; }` -> 8 bytes with no internal padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
