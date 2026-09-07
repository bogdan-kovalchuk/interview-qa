---
id: emb-align-0019
title: "Why are hand-written byte-swap functions a fine choice on ARM?"
description: "The compiler recognizes the shift and mask pattern and emits a single REV or REV16 instruction"
track: embedded
section: memory-alignment-and-endianness
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

**The compiler recognizes the shift/mask pattern and generates a single `REV`/`REV16` instruction.**

That is, readable portable C compiles just as efficiently as inline assembly, but works on any toolchain and is easier to maintain.

Rule: start with clear C; reach for intrinsics/asm only if profiling shows a need.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
