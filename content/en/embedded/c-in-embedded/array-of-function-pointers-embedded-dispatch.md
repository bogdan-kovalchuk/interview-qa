---
id: emb-cppfound-0097
title: "What is an array of function pointers and where is it used in embedded systems?"
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

`void (*handlers[8])(void)` – an array of 8 function pointers.

Usage:
- **Software interrupt router**: `handlers[irq_id]();`;
- **State machine**: `state_fn[current_state]();`;
- **Protocol parser**: `cmd_handlers[cmd_id](payload);`;
- **Bootloader jump**: a table of entry points in Flash.

Advantages: O(1) dispatch, easy to extend by changing the table. The Cortex-M Vector Table is a hardware implementation of this pattern.[^embeddedinterviewlab]

## Detailed explanation

TODO
