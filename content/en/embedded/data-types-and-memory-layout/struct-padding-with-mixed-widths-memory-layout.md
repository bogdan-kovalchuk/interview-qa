---
id: emb-dtypes-0018
title: "Draw the memory layout without packing: `struct { uint8_t a; uint32_t b; uint8_t c; }`"
description: "The compiler pads between the uint8_t and uint32_t fields, so the struct takes 12 bytes, not 6."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

For a typical ABI where `uint32_t` has size and alignment 4 bytes: `a` @ offset 0 (1B) -> <span class="warn">3B padding</span> -> `b` @ offset 4 (4B) -> `c` @ offset 8 (1B) -> <span class="warn">3B trailing padding</span>.

Under those assumptions, the total is **12 bytes**. A compiler may add padding to align members and the structure size; exact offsets and `sizeof` depend on the ABI and implementation.[^iso-c-n1570]

Reordering fields often reduces padding on a target ABI, but verify the result with `sizeof` and `offsetof`; the standard does not guarantee that the alternative order is exactly 8 bytes.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
