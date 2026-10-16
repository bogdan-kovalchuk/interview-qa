---
id: emb-memlink-0004
title: "What is the difference between malloc and calloc?"
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

`malloc(size)` allocates `size` bytes and <span class="warn">does not initialize</span> them[^dou-embedded-interview] (one argument), whereas `calloc(n, size)` allocates `n * size` bytes and **initializes them to zero** (two arguments; a good implementation also checks for multiplication overflow).

Example: `int *a = malloc(10 * sizeof(int));` – initial values are indeterminate; `int *b = calloc(10, sizeof(int));` – all elements are 0. Both return `NULL` on failure.

## Detailed explanation

TODO
