---
id: emb-structs-0002
title: "Why can a struct be larger than the sum of its fields?"
description: "Because of padding: the compiler inserts unused bytes between fields or at the end of the struct to satisfy alignment requirements."
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

Due to padding: the compiler inserts unused bytes between fields or at the end of the struct to satisfy alignment requirements.

For example, `uint32_t` often must be aligned to an address that is a multiple of 4. If a `uint8_t` precedes it, the compiler may add 3 bytes of padding. Tail padding is added so that an array of structs has correct alignment for every element.

Embedded rule: never assume the wire or storage layout of a struct without `sizeof`, `offsetof`, and a compiler/ABI check.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
