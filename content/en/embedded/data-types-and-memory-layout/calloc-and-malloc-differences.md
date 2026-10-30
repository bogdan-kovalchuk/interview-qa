---
id: emb-memlink-0011
title: "What is the difference between `calloc` and `malloc`?"
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

`malloc(size)` allocates a block of memory of the given size but <span class="warn">does not initialize</span> it: old bytes may remain. `calloc(n, size)` allocates memory for `n` elements of `size` bytes each and fills it with zeroes.

Another practical difference: a quality `calloc` implementation can check for overflow in the `n * size` multiplication, whereas in a manual `malloc(n * size)` that check is easy to forget. Both functions return `NULL` on failure and the memory must be freed with `free`.[^dou-embedded-interview]

## Detailed explanation

TODO
