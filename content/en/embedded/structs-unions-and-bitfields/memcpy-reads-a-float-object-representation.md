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

**Via `memcpy`**:

`uint32_t bits; memcpy(&bits, &f, sizeof bits);`

`memcpy` copies the object representation byte by byte and does not violate strict aliasing. The optimizer typically converts this into a single load/store without an actual function call when the size is known at compile time.

Embedded rule: for type punning in portable low-level code, `memcpy` is often safer than a pointer cast or a union trick.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
