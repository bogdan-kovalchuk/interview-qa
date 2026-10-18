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
---

## Short answer

**Memory barrier** is an instruction or compiler primitive that constrains reordering of memory operations by the compiler or CPU; it is needed where access order matters: lock-free code, MMIO, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** is consistency between cache copies in different cores, or between cache and memory touched by DMA: after DMA writes a buffer to RAM, the CPU may still see a stale cached copy without invalidate/clean.

In practice: atomics and barriers for shared memory, cache clean/invalidate or non-cacheable buffers for DMA, depending on the MCU/MPU.

## Detailed explanation

TODO
