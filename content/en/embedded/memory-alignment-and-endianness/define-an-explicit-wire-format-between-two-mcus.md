---
id: emb-align-0032
title: "How do you correctly send data between two different MCUs?"
description: "Define an explicit wire format and serialize field by field with explicit byte order."
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

**Define an explicit wire format and serialize field by field with explicit byte order.**

This is the canonical interview answer: no raw `memcpy` of structs, because padding and endianness differ. Each multi-byte field goes through `htonl`/`htons` into a fixed offset.

Rule: a documented wire format plus field-by-field (de)serialization gives portability across any platforms.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
