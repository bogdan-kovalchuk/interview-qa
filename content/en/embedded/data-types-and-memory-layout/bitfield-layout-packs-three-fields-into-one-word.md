---
id: emb-dtypes-0088
title: "What does this look like in memory? `struct { uint32_t flags:1; uint32_t mode:3; uint32_t value:28; }`"
description: "The three bit-fields pack into a single uint32t, but the bit-packing order is implementation-defined."
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

Bitfield layout: one `uint32_t` (1+3+28=32 bits). Size: **4 bytes**.

On ARM GCC (from LSB): bits `[0]` -> `flags`, bits `[3:1]` -> `mode`, bits `[31:4]` -> `value`.

<span class="warn">However</span>: bit-packing order is implementation-defined! For hardware registers, explicit masks + shifts on `uint32_t` are safer, or verify the layout with `static_assert`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
