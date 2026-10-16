---
id: emb-volconst-0039
title: "Trap: is `volatile` enough for a DMA buffer?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
---

## Short answer

<span class="warn">Not always.</span>

`volatile` can make the compiler perform accesses to a descriptor or flag that DMA modifies. But it does not address cache coherency, alignment, ownership, memory barriers, or race conditions. On a Cortex-M7 with D-cache, DMA can write to RAM while the CPU still reads stale cache lines.[^gcc-volatile] [^arm-cortex-m7]

Protection: use non-cacheable memory or cache clean/invalidate in the correct directions, barriers as required by the platform, and a clear ownership protocol between the CPU and DMA.[^arm-cortex-m7]

## Detailed explanation

TODO
