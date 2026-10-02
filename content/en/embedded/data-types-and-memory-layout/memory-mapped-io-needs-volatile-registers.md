---
id: emb-dtypes-0032
title: "What is memory-mapped I/O, and why do such registers need `volatile`?"
description: "Peripheral registers are accessed like ordinary memory, and volatile stops the compiler from caching or eliding accesses to them."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: gcc-volatiles
    title: "GCC: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains volatile accesses in GCC and their limits; other compilers may differ."
  - source_id: arm-dmb
    title: "Cache Coherency in ARMv7-A and ARMv7-R Systems"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/CacheCoherencyWhitepaper_6June2011.pdf?revision=e5a82cb4-0f87-4f5c-91cf-52b33a5cd1da
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains DMB/DSB ordering visibility; examples and cache behavior depend on the specific system."
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Memory-mapped I/O** – peripheral registers are accessible at addresses in the CPU memory space, but have platform-defined hardware semantics.

`volatile` is required because:
1. Hardware may change a status register between reads.
2. `volatile` marks accesses that the compiler implementation must preserve according to its rules.

`volatile` does not make an access atomic or act as a memory barrier for ordinary writes.[^gcc-volatiles]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
