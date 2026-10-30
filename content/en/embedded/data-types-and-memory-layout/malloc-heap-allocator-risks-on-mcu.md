---
id: emb-memlink-0012
title: "How does malloc work at the heap allocator level, and why is dynamic memory risky on an MCU?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: freertos-heap
    title: "FreeRTOS heap_4 implementation"
    url: https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/portable/MemMang/heap_4.c
  - source_id: misra-c-2023-addendum-2
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
---

## Short answer

`malloc` takes a block from the heap, maintains metadata and searches for a free chunk of sufficient size; `free` returns the block to the allocator. On MCU the heap is small, the allocator can be non-deterministic in time and create fragmentation. <span class="warn">In long-running firmware this is a risk of failure at runtime</span>, so static buffers, pools or arena allocators are often used.[^dou-embedded-interview]

## Detailed explanation

TODO
