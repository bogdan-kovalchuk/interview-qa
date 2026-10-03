---
id: emb-structs-0014
title: "What is a `union` in C?"
description: "A union stores several alternative fields in the same memory area; the union size equals the size of the largest member, accounting for alignment."
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

**A `union`** gives several members shared storage, so their values occupy the same memory area. Reading another member reinterprets the stored representation; it does not convert the value between types.[^iso-c-n1570]

Unlike a `struct`, union members overlap and share a starting address. Writing through one member changes shared bytes; reading through another type depends on the object representation and can encounter a trap representation.[^iso-c-n1570]

Embedded code uses unions for variant data and payload representations, but byte access requires care with language rules and endianness.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
