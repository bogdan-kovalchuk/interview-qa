---
id: emb-cppfound-0085
title: "What does void(*isr_table[16])(void) do, and how is an ISR called by index?"
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

`void(*isr_table[16])(void)` – an array of 16 function pointers: each points to a function with no arguments that returns void. Initialization: `isr_table[0] = nmi_handler; isr_table[1] = hardfault_handler;` Call: `isr_table[irq_num]();` or `(*isr_table[irq_num])();` This is a software interrupt controller or event dispatcher pattern; the Cortex-M Vector Table in Flash is the hardware analogue: an array of interrupt handler addresses.[^embeddedinterviewlab]

## Detailed explanation

TODO
