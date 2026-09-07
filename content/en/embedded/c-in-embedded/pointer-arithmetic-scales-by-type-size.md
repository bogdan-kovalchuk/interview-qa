---
id: emb-cppfound-0007
title: "How does pointer arithmetic work and why does it scale by sizeof(T)?"
description: "Pointer arithmetic advances by sizeof(T) per step so p++ always reaches the next element; this scaling is critical in embedded when iterating register banks and DMA buffers."
track: embedded
section: c-in-embedded
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

Pointer arithmetic always accounts for the **size of the element type**:

`T *p; p + n` -> physically: `(char*)p + n * sizeof(T)`

Examples:
- `uint8_t *p; p+1` -> +1 byte
- `uint16_t *p; p+1` -> +2 bytes
- `uint32_t *p; p+1` -> +4 bytes

This allows iterating arrays naturally: `p++` moves to the next element regardless of size. Critical in embedded when working with register banks and DMA buffers.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
