---
id: emb-align-0040
title: "Why do single-byte fields need no byte swap when serialising?"
description: "Endianness concerns only the byte order within a multi-byte value; a single byte has no internal order."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Endianness concerns only the byte order within a multi-byte value.**

A single byte has no "internal order", so `uint8_t` is the same on LE and BE and is placed into the buffer as is.

Rule: apply `htonl`/`htons` to 16/32/64-bit fields; no conversion is needed for `uint8_t` and byte arrays.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
