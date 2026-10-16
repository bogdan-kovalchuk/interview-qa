---
id: emb-cppfound-0023
title: "Що таке function pointer і який синтаксис його оголошення?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Function pointer** – вказівник на функцію: зберігає адресу коду функції для виклику через нього.

Синтаксис: `return_type (*name)(param_types);` Приклад: `void (*isr)(void) = &my_handler;`

Виклик: `(*isr)();` або просто `isr();` (обидва коректні).

Застосування у embedded: ISR dispatch tables, state machine transitions, RTOS task functions, callback API (`HAL_UART_RegisterCallback`).[^embeddedinterviewlab]

## Detailed explanation

TODO
