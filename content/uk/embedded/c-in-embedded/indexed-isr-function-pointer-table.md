---
id: emb-cppfound-0085
title: "Що робить `void(*isr_table[16])(void)` і як викликати ISR за індексом?"
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

`void(*isr_table[16])(void)` – масив із 16 function pointers: кожен вказує на функцію без аргументів що повертає void.

Ініціалізація: `isr_table[0] = nmi_handler; isr_table[1] = hardfault_handler;`

Виклик: `isr_table[irq_num]();` або `(*isr_table[irq_num])();`

Це паттерн software interrupt controller або event dispatcher. Cortex-M Vector Table у Flash – апаратний аналог: масив адрес обробників переривань.[^embeddedinterviewlab]

## Detailed explanation

TODO
