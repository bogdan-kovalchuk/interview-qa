---
id: emb-cppfound-0047
title: "What is a flexible array member (FAM) in C99 and where is it stored?"
description: "How C99 flexible array members are laid out and allocated."
track: embedded
section: c-in-embedded
level: junior
type: concept
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

**Flexible Array Member** (FAM) – the last field of a struct with an unspecified size: `struct Packet { uint8_t len; uint8_t data[]; };`

`sizeof(struct Packet)` does not include `data`. The FAM is allocated together with the struct: `malloc(sizeof(Packet) + n)` – then `data` occupies `n` bytes immediately after the struct fields.

It is stored in the same memory block as the struct (heap or static). It cannot be the only member of a struct and cannot be in an array.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
