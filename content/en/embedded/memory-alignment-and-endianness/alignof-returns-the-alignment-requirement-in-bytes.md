---
id: emb-align-0025
title: "What does `_Alignof(T)` (C11) / `alignof(T)` return?"
description: "The alignment requirement of the type in bytes, a compile-time value."
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

**The alignment requirement of the type, in bytes.**

`_Alignof(uint32_t)` -> 4, `_Alignof(double)` -> typically 8. It is a compile-time value, useful for layout checks and custom allocators.

Rule: in C11 use `_Alignof` (the `alignof` macro in `<stdalign.h>`); in C++ `alignof` is built-in.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
