---
id: emb-structs-0017
title: "What is the safer way to read the bits of a `float` as `uint32_t` in C?"
description: "Via memcpy: uint32t bits; memcpy copies the object representation byte by byte and does not violate strict aliasing."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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

**Via `memcpy`**:

`uint32_t bits; memcpy(&bits, &f, sizeof bits);`

`memcpy` copies the object representation byte by byte without accessing the `float` through an incompatible `uint32_t` lvalue. The resulting integer value depends on both types' sizes and representations and on byte order.[^iso-c-n1570]

For representation copying, `memcpy` is portable with respect to aliasing rules; that does not make the numeric bit value portable across platforms.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
