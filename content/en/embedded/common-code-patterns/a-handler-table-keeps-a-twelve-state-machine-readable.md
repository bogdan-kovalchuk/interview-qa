---
id: emb-patterns-0032
title: "How does an FSM on a function-pointer table scale?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**A function-pointer table maps each FSM state to its handler; adding a state requires coordinated updates to the enum, table, and transitions.**

This separates dispatch from handler logic, but does not automatically avoid changes elsewhere. Whether a `static const` table resides in Flash depends on the MCU, compiler, and linker script.[^iso-c-n1570]

Validate the state index and ensure the selected handler pointer is non-null before calling it.

## Detailed explanation

TODO
