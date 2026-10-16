---
id: emb-memlink-0014
title: "How can ownership and lifetime be implemented for buffers without a heap in embedded C?"
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

Allocate buffers statically or in a pool and define the owner explicitly: driver, task, queue or caller. Pass not a raw resource forever, but a handle or descriptor with a `free/in_use/done` state. For ISR/DMA, ring buffer, double buffer and callback/queue patterns work well, where the lifetime ends after an explicit release.[^dou-embedded-interview]

## Detailed explanation

TODO
