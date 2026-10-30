---
id: emb-memlink-0001
title: "How do you free memory in C?"
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

With the `free(ptr)` function from `<stdlib.h>`.[^dou-embedded-interview] After the call, every pointer to that block becomes a <span class="warn">dangling pointer</span>. It is common practice to null out the variable right away: `free(ptr); ptr = NULL;`.

Important caveat: this only helps for that one pointer variable. Other copies of the same address are still dangling, so ownership must be tracked; rules: only free what was allocated via `malloc`/`calloc`/`realloc`; never double free; never free stack or static objects.

## Detailed explanation

TODO
