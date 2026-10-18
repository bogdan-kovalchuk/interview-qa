---
id: emb-memlink-0012
title: "How does malloc work at the heap-allocator level, and why is dynamic memory risky on an MCU?"
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

`malloc` takes a block from the heap, maintains metadata and searches for a free chunk of sufficient size; `free` returns the block to the allocator. On an MCU the heap is small, the allocator can be nondeterministic in time and create fragmentation. <span class="warn">In long-running firmware this is a risk of runtime failure</span>, so static buffers, pools or an arena allocator are often used instead.[^dou-embedded-interview]

## Detailed explanation

TODO
