---
id: emb-volconst-0003
title: "Name three typical use cases for `volatile` in embedded C."
description: "Typical cases are memory-mapped hardware registers, variables shared with an ISR, and memory modified by DMA; required guarantees depend on the platform."
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

Three typical use cases: memory-mapped hardware registers, variables shared with an ISR, and memory modified by DMA.

In all three cases the compiler does not see an ordinary C write that changes the value. Without `volatile` it may cache the old value or remove the access as redundant.

These are not universally mandatory cases: ISR and DMA rules depend on the compiler and platform, and `volatile` alone does not provide synchronisation.[^iso-c-n1570] [^gcc-volatile]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
