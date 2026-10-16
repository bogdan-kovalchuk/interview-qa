---
id: emb-memlink-0001
title: "How do you free memory in C?"
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

With the `free(ptr)` function from `<stdlib.h>`.[^dou-embedded-interview] After the call, every pointer to that block becomes a <span class="warn">dangling pointer</span>. It is common practice to null out the variable right away: `free(ptr); ptr = NULL;`.

Important caveat: this only helps for that one pointer variable. Other copies of the same address are still dangling, so ownership must be tracked; rules: only free what was allocated via `malloc`/`calloc`/`realloc`; never double free; never free stack or static objects.

## Detailed explanation

TODO
