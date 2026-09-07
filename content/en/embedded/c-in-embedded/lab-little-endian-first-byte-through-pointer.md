---
id: emb-cppfound-0073
title: "What is the value of `*(uint8_t*)(&val)` for a little-endian value?"
description: "How a byte pointer exposes the least significant byte on little-endian systems."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**0x78**. The cast `(uint8_t*)(&val)` is a pointer to the first byte of `val` in memory. On little-endian: the LSB is at the lowest address -> `0x78`. Memory layout: `[78][56][34][12]`; next byte: `*((uint8_t*)(&val) + 1) = 0x56`. Access through a byte pointer is allowed for character types (`unsigned char*`); in practice `uint8_t` is typically a typedef for `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
