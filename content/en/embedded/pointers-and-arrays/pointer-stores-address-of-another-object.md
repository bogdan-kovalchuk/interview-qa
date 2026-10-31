---
id: emb-cemb-0014
title: "What is a pointer?"
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

**A pointer** is a variable that stores the address of another object or function in memory.[^dou-embedded-interview] For example: `int x = 10; int *p = &x;`. The `&` operator takes the address, and `*p` dereferences the pointer and provides access to the value.

Pointers are needed for passing objects to functions without copying, working with arrays, dynamic memory, callbacks, data structures, and memory-mapped registers. Dangers: `NULL`, dangling pointer, out-of-bounds array access, incorrect type casting.

## Detailed explanation

TODO
