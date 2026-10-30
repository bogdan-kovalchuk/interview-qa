---
id: emb-memlink-0013
title: "What is heap fragmentation, and how does it appear in long-running firmware?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
  - source_id: misra-c-2023-addendum-2
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

**Heap fragmentation** is a situation where there is enough total free memory, but it is split into small non-contiguous blocks. In firmware this appears as random `malloc` failures after hours or days of operation, especially with varying allocation sizes. Typical countermeasures: fixed-size pools, allocate-on-startup, bounded lifetimes and no heap in ISR.[^dou-embedded-interview]

## Detailed explanation

TODO
