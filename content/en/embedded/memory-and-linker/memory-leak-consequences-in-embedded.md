---
id: emb-memlink-0002
title: "What problems can arise from not freeing memory?"
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

**Memory leak** – allocated memory is not returned to the system even though it is no longer used.[^dou-embedded-interview] Consequences:

- the heap is gradually exhausted, so `malloc` returns `NULL`;
- the system slows down or hangs;
- in embedded (MCU without MMU or OS) this is especially critical: a small heap can run out after hours or days, and the device goes into reset/fault or an incorrect state.

Related problems: <span class="warn">dangling pointer</span> (accessing freed memory), <span class="warn">double free</span> (UB).

## Detailed explanation

TODO
