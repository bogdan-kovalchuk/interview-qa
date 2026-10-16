---
id: emb-dtypes-0086
title: "Trap: do `int x;` and `static int x;` behave the same on a function's first call?"
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

No. `int x;` has automatic storage duration and an uninitialized value; reading it before assignment is invalid. `static int x;` has static storage duration and is zero-initialized before the first function entry; after assignment, its value persists between calls. Placement in a stack or `.bss` is a common implementation detail, not a language guarantee.[^iso-c-n1570]

## Detailed explanation

TODO
