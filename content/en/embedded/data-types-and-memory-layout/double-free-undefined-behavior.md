---
id: emb-memlink-0008
title: "What happens if `free` is called twice?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
---

## Short answer

A repeated `free(ptr)` on the same allocated block is <span class="warn">double free</span> and undefined behavior.[^dou-embedded-interview] Consequences can vary: crash, heap metadata corruption, random errors later, or a security vulnerability.

Safe pattern: null out the pointer after freeing – `free(ptr); ptr = NULL;`. Calling `free(NULL)` is allowed and does nothing, so nulling reduces the risk of a repeated free. But if there are multiple copies of the same pointer, ownership must be tracked rather than relying on `NULL` alone.

## Detailed explanation

TODO
