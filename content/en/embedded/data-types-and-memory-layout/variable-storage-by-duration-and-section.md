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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
---

## Short answer

A variable can reside in different places depending on storage duration and the linker script. Local automatic variables typically live on the **stack**, dynamic objects from `malloc` on the **heap**, globals and `static` in static storage.[^dou-embedded-interview]

Typical sections: `.data` – initialized global/static variables, copied from Flash to RAM; `.bss` – zeroed or uninitialized global/static, zeroed by startup code; `.rodata` – constants; `.text` – machine code. The compiler may also hold values in registers temporarily.

## Detailed explanation

TODO
