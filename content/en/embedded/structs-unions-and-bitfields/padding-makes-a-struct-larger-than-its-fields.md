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
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

Due to padding: a C implementation may insert unused bytes between fields or after the last field, including to satisfy alignment requirements.[^iso-c-n1570]

For example, on a common ABI where `uint32_t` has size and alignment of 4 bytes and `uint8_t` has size and alignment of 1 byte, 3 padding bytes may follow an initial `uint8_t`. Tail padding may make the total size a multiple of the struct's alignment.[^iso-c-n1570]

Embedded rule: never assume a struct's wire or storage layout without checking `sizeof`, `offsetof`, and the compiler/ABI.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
