---
id: emb-memlink-0011
title: "What is the difference between `calloc` and `malloc`?"
track: embedded
section: memory-and-linker
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

`malloc(size)` allocates a block of memory of the given size but <span class="warn">does not initialize</span> it: old bytes may remain. `calloc(n, size)` allocates memory for `n` elements of `size` bytes each and fills it with zeroes.

Another practical difference: a quality `calloc` implementation can check for overflow in the `n * size` multiplication, whereas in a manual `malloc(n * size)` that check is easy to forget. Both functions return `NULL` on failure and the memory must be freed with `free`.[^dou-embedded-interview]

## Detailed explanation

TODO
