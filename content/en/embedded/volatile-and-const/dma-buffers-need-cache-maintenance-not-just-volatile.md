---
id: emb-volconst-0039
title: "Trap: is `volatile` enough for a DMA buffer?"
description: "volatile is not always enough for a DMA buffer."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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
    applicability: "Describes compiler volatile semantics in GCC; it does not describe DMA cache coherency."
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
    accessed: 2026-10-04
    kind: official
    version: "DUI 0646B"
    applicability: "Describes Cortex-M7 D-cache operations and their use to make external DMA data visible; ordering depends on the SoC."
---

## Short answer

<span class="warn">Not always.</span>

`volatile` can make the compiler perform accesses to a descriptor or flag that DMA modifies. But it does not address cache coherency, alignment, ownership, memory barriers, or race conditions. On a Cortex-M7 with D-cache, DMA can write to RAM while the CPU still reads stale cache lines.[^gcc-volatile] [^arm-cortex-m7]

Protection: use non-cacheable memory or cache clean/invalidate in the correct directions, barriers as required by the platform, and a clear ownership protocol between the CPU and DMA.[^arm-cortex-m7]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
