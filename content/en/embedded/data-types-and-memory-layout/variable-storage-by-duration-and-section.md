---
id: emb-memlink-0009
title: "Where can a variable be stored?"
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

A variable can reside in different places depending on storage duration and the linker script. Local automatic variables typically live on the **stack**, dynamic objects from `malloc` on the **heap**, globals and `static` in static storage.[^dou-embedded-interview]

Typical sections: `.data` – initialized global/static variables, copied from Flash to RAM; `.bss` – zeroed or uninitialized global/static, zeroed by startup code; `.rodata` – constants; `.text` – machine code. The compiler may also hold values in registers temporarily.

## Detailed explanation

TODO
