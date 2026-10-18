---
id: emb-cppfound-0097
title: "Що таке array of function pointers і де використовується у embedded?"
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

`void (*handlers[8])(void)` – масив із 8 function pointers.

Використання:
- **Software interrupt router**: `handlers[irq_id]();`;
- **State machine**: `state_fn[current_state]();`;
- **Protocol parser**: `cmd_handlers[cmd_id](payload);`;
- **Bootloader jump**: таблиця точок входу у Flash.

Переваги: O(1) dispatch, легко розширювати через зміну таблиці. Cortex-M Vector Table – апаратна реалізація цього паттерну.[^embeddedinterviewlab]

## Detailed explanation

TODO
