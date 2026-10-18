---
id: emb-cppfound-0023
title: "What is a function pointer and what is its declaration syntax?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Function pointer** – a pointer to a function: it stores the address of the function's code for calling through it.

Syntax: `return_type (*name)(param_types);` Example: `void (*isr)(void) = &my_handler;`

Call: `(*isr)();` or simply `isr();` (both are valid).

Uses in embedded: ISR dispatch tables, state machine transitions, RTOS task functions, callback API (`HAL_UART_RegisterCallback`).[^embeddedinterviewlab]

## Detailed explanation

TODO
