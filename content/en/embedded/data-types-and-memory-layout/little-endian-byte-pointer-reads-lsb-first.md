---
id: emb-dtypes-0090
title: "What does this print on little-endian? `uint32_t x = 0xDEADBEEF; uint8_t *p = (uint8_t*)&x; printf(\"%02X\", p[0]);`"
description: "On little-endian the least-significant byte sits at the lowest address, so p[0] gives EF."
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

`EF`: on little-endian (Cortex-M) the LSB is stored at the lowest address, so `0xDEADBEEF` in memory is `[EF][BE][AD][DE]` and `p[0]` = `0xEF` (LSB), `p[1] = 0xBE`, `p[2] = 0xAD`, `p[3] = 0xDE` (MSB).

Access through a byte pointer is allowed for character types (`unsigned char*`), and `uint8_t` is typically a typedef for `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
