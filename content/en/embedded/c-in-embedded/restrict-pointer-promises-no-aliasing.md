---
id: emb-cppfound-0028
title: "What is `restrict` and why is it useful in embedded systems?"
description: "A C99 pointer qualifier that promises no aliasing, enabling vectorization and register promotion; aliasing through it is undefined behavior."
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

`restrict` (C99) – a pointer qualifier that promises the compiler: through this pointer and through no other pointer in this function **does aliasing occur** (no overlapping memory regions).

Example: `void add(int * restrict dst, const int * restrict src, int n)`.

Gives the compiler freedom for aggressive optimization (vectorization, register promotion). Important for DSP, crypto, memcpy-like functions. If aliasing does occur – undefined behavior.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
