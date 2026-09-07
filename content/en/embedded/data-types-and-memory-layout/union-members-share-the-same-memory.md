---
id: emb-dtypes-0023
title: "What memory layout does this have? `union { uint32_t word; uint8_t bytes[4]; };`"
description: "All union members overlay the same memory, sized to the largest member."
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

All fields occupy **the same memory region**. Size = `max(sizeof(uint32_t), sizeof(uint8_t[4])) = 4` bytes.

On little-endian (Cortex-M): if `word = 0x12345678`, then:
`bytes[0] = 0x78` (LSB), `bytes[1] = 0x56`, `bytes[2] = 0x34`, `bytes[3] = 0x12` (MSB).

Uses: endianness detection, byte-level serialization, IEEE 754 bit inspection.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
