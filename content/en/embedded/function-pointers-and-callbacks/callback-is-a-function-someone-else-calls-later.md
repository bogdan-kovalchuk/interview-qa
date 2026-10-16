---
id: emb-fnptr-0012
title: "What is a callback?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**A callback** is a function whose address is passed to other code so that it can call it later upon a certain event or condition.[^iso-c-n1570]

In C, a callback is most often implemented with a function pointer. For example, a UART driver calls a callback when a byte is received, a timer on timeout, a parser when it finds a frame, and `qsort` when it needs to compare two elements.

Interview rule: a function pointer is the mechanism; a callback is the role or usage pattern of that mechanism.[^iso-c-n1570]

## Detailed explanation

TODO
