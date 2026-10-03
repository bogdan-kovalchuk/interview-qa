---
id: emb-volconst-0002
title: "How does `volatile` affect accesses optimised by the compiler?"
description: "volatile makes accesses to the qualified object observable under the implementation's rules, but is not a general ordering barrier."
track: embedded
section: volatile-and-const
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GCC volatile-access behavior and the lack of a memory-barrier guarantee; other compilers can differ."
---

## Short answer

**`volatile` requires volatile accesses to be handled according to the C implementation's rules, so a compiler usually cannot cache them as ordinary values or remove them.**

Without it, a compiler may reuse an ordinary object's previous value or remove an unobservable store. `volatile` does not order ordinary accesses relative to volatile ones, nor does it prohibit every reordering.[^iso-c-n1570] [^gcc-volatile]

Rule: for precise ordering of peripheral operations, consult the compiler documentation and use the required compiler or hardware barrier.[^gcc-volatile]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
