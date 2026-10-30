---
id: emb-memlink-0014
title: "How can ownership and lifetime be implemented for buffers without a heap in embedded C?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Allocate buffers statically or in a pool and define the owner explicitly: driver, task, queue or caller. Pass not a raw resource forever, but a handle or descriptor with a `free/in_use/done` state. For ISR/DMA, ring buffer, double buffer and callback/queue patterns work well, where the lifetime ends after an explicit release.[^dou-embedded-interview]

## Detailed explanation

TODO
