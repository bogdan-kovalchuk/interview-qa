---
id: emb-structs-0029
title: "What is a designated initializer and why is it useful for structs?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

A **designated initializer** explicitly specifies which field is being initialized: `.baud = 115200`.

This makes the code more resilient to field reordering and more readable for configuration structs. Unspecified fields receive zero initialization when the initializer is an aggregate initializer.

Embedded rule: for driver config, `UART_Config cfg = { .baud = 115200, .parity = PARITY_NONE };` is better than a positional initializer with a long list of numbers.[^iso-c-n1570]

## Detailed explanation

TODO
