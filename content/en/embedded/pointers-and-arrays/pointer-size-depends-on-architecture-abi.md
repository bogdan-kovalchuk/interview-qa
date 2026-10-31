---
id: emb-cemb-0004
title: "What is the size of a pointer, and what does it depend on?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Short answer

The size of a pointer depends on the architecture's address space and ABI, not on the type it points to.[^dou-embedded-interview] On a 32-bit system, `sizeof(void*) == 4` is typical; on 64-bit – `8`; on 16-bit – `2`.

`int *`, `char *`, and `struct Foo *` usually have the same size within one platform because they all store an address. In embedded, there may be nuances with different memory spaces or function pointers, so the correct answer is to check with `sizeof(pointer)` for the specific compiler and target.

## Detailed explanation

TODO
