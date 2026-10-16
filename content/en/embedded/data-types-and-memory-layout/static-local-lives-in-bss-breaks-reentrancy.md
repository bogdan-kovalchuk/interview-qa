---
id: emb-dtypes-0013
title: "Where is a `static` local variable stored, and how long does it live?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

An uninitialized local variable declared `static` has static storage duration, starts with a zero value, and is placed according to the implementation.

Its value persists between function calls. If multiple contexts modify it without synchronization, the shared state can break reentrancy and cause a race.[^iso-c-n1570]

## Detailed explanation

TODO
