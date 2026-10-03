---
id: emb-volconst-0038
title: "Why is `volatile` not a memory barrier?"
description: "volatile constrains optimizations of accesses to volatile objects but is not a full memory barrier for all memory."
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
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents the limits of volatile and its inability to order non-volatile memory accesses in GCC."
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
    accessed: 2026-10-04
    kind: official
    version: "DUI 0646B"
    applicability: "Describes Cortex-M7 cache maintenance and visibility of external DMA data; exact requirements depend on SoC configuration."
---

## Short answer

**`volatile` constrains optimizations of accesses to volatile objects, but it is not a full CPU/compiler memory barrier for all memory.**

`volatile` does not establish a general order between ordinary memory accesses and volatile accesses, nor is it a complete CPU/compiler memory barrier. Exact volatile access rules depend on the language, compiler, and target. Cache synchronization, bus ordering, DMA visibility, and inter-core ordering need separate platform guarantees.

Rule: for required hardware ordering, use architectural primitives such as `__DMB()`, `__DSB()`, `__ISB()` and compiler-specific facilities as required by the platform documentation.[^gcc-volatile]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
