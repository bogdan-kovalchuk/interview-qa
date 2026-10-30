---
id: emb-memlink-0004
title: "What is the difference between malloc and calloc?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`malloc(size)` allocates `size` bytes and <span class="warn">does not initialize</span> them[^dou-embedded-interview] (single argument), while `calloc(n, size)` allocates `n * size` bytes and **initializes them to zero** (two arguments; good implementations also check for multiplication overflow).

Example: `int *a = malloc(10 * sizeof(int));` – initial values are indeterminate; `int *b = calloc(10, sizeof(int));` – all elements = 0. Both return `NULL` on failure.

## Detailed explanation

TODO
