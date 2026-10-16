---
id: emb-memlink-0013
title: "What is heap fragmentation, and how does it appear in long-running firmware?"
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

**Heap fragmentation** is a situation where there is enough total free memory, but it is split into small non-contiguous blocks. In firmware this appears as random `malloc` failures after hours or days of operation, especially with varying allocation sizes. Typical countermeasures: fixed-size pools, allocate-on-startup, bounded lifetimes and no heap in ISR.[^dou-embedded-interview]

## Detailed explanation

TODO
