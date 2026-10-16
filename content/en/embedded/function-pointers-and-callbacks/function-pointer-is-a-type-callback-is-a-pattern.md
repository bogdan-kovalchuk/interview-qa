---
id: emb-fnptr-0013
title: "How does a function pointer differ from a callback?"
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

**A function pointer is a type/value; a callback is an architectural pattern.**

A function pointer can sit in a command table, vector table, or vtable-like struct. A callback is when one module registers a function and another module calls it later, usually in response to an event.

Embedded example: `void (*isr)(void)` in a vector table is a function pointer; a user hook `on_rx(ctx, byte)` called by the UART driver is a callback.[^iso-c-n1570]

## Detailed explanation

TODO
