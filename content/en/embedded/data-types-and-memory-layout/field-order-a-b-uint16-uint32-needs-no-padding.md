---
id: emb-dtypes-0078
title: "How does the compiler lay this out? `struct { uint8_t a; uint8_t b; uint16_t c; uint32_t d; }`"
description: "This field order naturally fills the alignment gaps, so the struct takes 8 bytes with no padding."
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

Optimal layout **with no padding**:
- `a` @ offset 0 (1B)
- `b` @ offset 1 (1B)
- `c` @ offset 2 (2B, aligned to 2) ✓
- `d` @ offset 4 (4B, aligned to 4) ✓

Total: **8 bytes**, no padding! Field order is chosen correctly (a, b -> fill to align 2, c fits, d fits).

General rule: fields from **largest alignment to smallest**. This example is also flawless because the pair of `uint8_t` naturally fills the alignment gap before `uint16_t`. Verify with `sizeof()` and `offsetof()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
