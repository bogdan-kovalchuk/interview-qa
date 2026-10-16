---
id: emb-fnptr-0005
title: "Why do callback APIs often carry a `void *context` parameter?"
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

**`context` gives a callback access to state for a particular instance.**

A C function pointer and a data pointer are distinct types; `void *` here carries the address of an object, such as a state structure, rather than the address of the callback function.[^iso-c-n1570]

The driver stores the callback with that data pointer and passes it when invoking the callback. The same callback code can then serve several independent devices without separate global variables.

## Detailed explanation

TODO
