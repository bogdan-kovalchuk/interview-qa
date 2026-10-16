---
id: emb-cppfound-0057
title: "Що таке dispatch table і як реалізувати через function pointers?"
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

**Dispatch table** – масив function pointers для вибору обробника за індексом. Замінює великі `switch`-конструкції.

```c
typedef void (*handler_t)(void);
handler_t table[16] = {
    isr0, isr1, isr2, ...
};
// Виклик:
table[irq_num]();
```

Переваги: O(1) dispatch, легко розширити, підходить для RTOS task tables, state machines, protocol demultiplexers. У embedded: Cortex-M Vector Table – вбудований dispatch table у Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO
