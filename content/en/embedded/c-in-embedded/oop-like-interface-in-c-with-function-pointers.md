---
id: emb-cemb-0031
title: "How can an OOP-like interface be implemented in C with structs, function pointers, and opaque handles?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

The public API declares an opaque type `typedef struct uart uart_t;`, and the implementation hides the struct fields in a `.c` file. Methods accept `uart_t*`, and polymorphism can be achieved through a table of function pointers: `read`, `write`, `ioctl`. This way the driver API has encapsulation without C++ ABI and without exposing internal MMIO/state.[^dou-embedded-interview]

## Detailed explanation

TODO
