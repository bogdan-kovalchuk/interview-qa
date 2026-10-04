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
updated: 2026-10-04
content_revision: 4
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

**The alignment requirement of the type, in bytes.**

Values for `uint32_t` and `double` depend on the implementation; the often quoted 4 and 8 are not standard guarantees. This compile-time property is useful for layout checks and custom allocators.

Rule: in C11 use `_Alignof` (the `alignof` macro in `<stdalign.h>`); in C++ `alignof` is built-in.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
