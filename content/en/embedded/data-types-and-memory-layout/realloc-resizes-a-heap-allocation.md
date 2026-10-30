---
id: emb-memlink-0003
title: "What is realloc used for?"
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

`realloc(ptr, new_size)` resizes a heap block[^dou-embedded-interview]: if space is free next to it the block extends in place, otherwise a new block is allocated, the data copied and the old block freed.

Typical use: dynamic arrays, input buffers, variable-length strings. Use `tmp = realloc(ptr, n); if (tmp) ptr = tmp;`, because on failure `realloc` returns `NULL` and the old `ptr` stays valid. `realloc(NULL, size)` acts like `malloc`; portable code must not rely on `realloc(ptr, 0)`, whose behavior depends on the standard and implementation.

## Detailed explanation

TODO
