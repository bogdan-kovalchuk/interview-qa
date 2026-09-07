---
id: emb-align-0012
title: "How does `0xDEADBEEF` sit in memory on a little-endian machine?"
description: "On a little-endian machine the bytes are stored EF BE AD DE from lowest to highest address"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

**`EF BE AD DE`** (from lowest address to highest).

Little-endian places the lowest byte first: `0xEF` @0, `0xBE` @1, `0xAD` @2, `0xDE` @3.

Rule: to "read" an LE dump as a number, read the bytes from right to left.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
