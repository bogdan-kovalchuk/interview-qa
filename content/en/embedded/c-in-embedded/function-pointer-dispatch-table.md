---
id: emb-cppfound-0057
title: "What is a dispatch table, and how can it be implemented with function pointers?"
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

**Dispatch table** – an array of function pointers for selecting a handler by index. Replaces large `switch` constructs.

```c
typedef void (*handler_t)(void);
handler_t table[16] = {
    isr0, isr1, isr2, ...
};
// Виклик:
table[irq_num]();
```

Advantages: O(1) dispatch, easy to extend, suitable for RTOS task tables, state machines, protocol demultiplexers. In embedded: the Cortex-M Vector Table is a built-in dispatch table in Flash.[^embeddedinterviewlab]

## Detailed explanation

TODO
