---
id: emb-rtos-0007
title: "What are a memory barrier and cache coherence?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
  - source_id: linux-memory-barriers
    title: "Linux kernel memory barriers"
    url: https://docs.kernel.org/core-api/wrappers/memory-barriers.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cmsis-core-intrinsics
    title: "CMSIS-Core (Cortex-M): Intrinsic Functions for CPU Instructions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__intrinsic__CPU__gr.html
  - source_id: cmsis-core-cache
    title: "CMSIS-Core (Cortex-M): Cache Functions (Level-1)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__cache__functions__m7.html
  - source_id: cmsis-core-dcache
    title: "CMSIS-Core (Cortex-M): D-Cache Functions"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Dcache__functions__m7.html
  - source_id: linux-dma-api-howto
    title: "Linux kernel: Dynamic DMA mapping Guide"
    url: https://docs.kernel.org/core-api/dma-api-howto.html
---

## Short answer

**Memory barrier** is an instruction or compiler primitive that constrains reordering of memory operations by the compiler or CPU; it is needed where access order matters: lock-free code, MMIO, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** is consistency between cache copies in different cores, or between cache and memory touched by DMA: after DMA writes a buffer to RAM, the CPU may still see a stale cached copy without invalidate/clean.

In practice: atomics and barriers for shared memory, cache clean/invalidate or non-cacheable buffers for DMA, depending on the MCU/MPU.

## Detailed explanation

TODO
