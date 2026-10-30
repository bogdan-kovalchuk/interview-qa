---
id: emb-memlink-0005
title: "What is the difference between stack and heap?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Stack** – automatic memory: local variables and function return addresses, managed by the compiler/CPU with LIFO.[^dou-embedded-interview] Fast access, limited size, freed automatically on function return.

**Heap** – dynamic memory: allocated manually with `malloc`/`free`. Larger capacity, but slower access and fragmentation risk; requires explicit freeing.

In embedded, heap is usually avoided because of non-determinism: stack and heap boundaries are defined in the linker script.

## Detailed explanation

TODO
