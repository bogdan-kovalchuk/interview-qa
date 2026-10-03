---
id: emb-volconst-0001
title: "What does the `volatile` qualifier mean in C?"
description: "volatile means the value of an object can change outside the visible program flow, by hardware, ISR, DMA, or another asynchronous mechanism."
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

**`volatile`** qualifies an object whose accesses must be observable to the C implementation according to its rules for volatile accesses.

This usually prevents removal of needed accesses or reuse of a saved value. Exact access semantics depend on the compiler and platform. A memory-mapped register read can return peripheral state, and a write can trigger hardware.

Rule: use `volatile` for objects with externally observable accesses, not as a general synchronisation mechanism or an atomicity guarantee.[^iso-c-n1570]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
