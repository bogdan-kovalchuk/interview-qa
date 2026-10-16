---
id: emb-memlink-0003
title: "What is realloc used for?"
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

`realloc(ptr, new_size)` resizes a heap block[^dou-embedded-interview]: if space is free next to it the block extends in place, otherwise a new block is allocated, the data copied and the old block freed.

Typical use: dynamic arrays, input buffers, variable-length strings. Use `tmp = realloc(ptr, n); if (tmp) ptr = tmp;`, because on failure `realloc` returns `NULL` and the old `ptr` stays valid. `realloc(NULL, size)` acts like `malloc`; portable code must not rely on `realloc(ptr, 0)`, whose behavior depends on the standard and implementation.

## Detailed explanation

TODO
