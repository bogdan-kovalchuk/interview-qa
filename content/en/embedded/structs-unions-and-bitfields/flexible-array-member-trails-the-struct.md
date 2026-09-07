---
id: emb-structs-0032
title: "What is a flexible array member?"
description: "A flexible array member is the last struct field with an incomplete size, such as uint8t data[]."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

A **flexible array member** is the last field of a struct with an incomplete size, for example `uint8_t data[];`.

It allows allocating a single memory block: header plus variable-length payload. `sizeof(struct Packet)` does not include the payload bytes, only the header and any padding before the flexible array.

Rule: a flexible array member must be the last field, and the struct must have at least one other named field.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
