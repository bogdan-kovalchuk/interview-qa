---
id: emb-memlink-0005
title: "What is the difference between stack and heap?"
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

**Stack** is automatic memory: local variables and function return addresses, managed by the compiler/CPU in LIFO order.[^dou-embedded-interview] Fast access, limited size, freed automatically on function exit.

**Heap** is dynamic memory: allocated manually via `malloc`/`free`. Larger capacity, but slower access and a risk of fragmentation; requires explicit deallocation.

In embedded, the heap is avoided because of nondeterminism: stack and heap bounds are set in the linker script.

## Detailed explanation

TODO
