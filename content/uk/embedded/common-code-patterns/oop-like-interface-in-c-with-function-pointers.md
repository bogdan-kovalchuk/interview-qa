---
id: emb-cemb-0031
title: "Як реалізувати OOP-подібний інтерфейс у C через struct, function pointers і opaque handles?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Публічний API оголошує opaque тип `typedef struct uart uart_t;`, а реалізація ховає поля struct у `.c`. Методи приймають `uart_t*`, а polymorphism можна зробити через table з function pointers: `read`, `write`, `ioctl`. Так driver API має інкапсуляцію без C++ ABI і без відкриття внутрішнього MMIO/стану.[^dou-embedded-interview]

## Detailed explanation

TODO
