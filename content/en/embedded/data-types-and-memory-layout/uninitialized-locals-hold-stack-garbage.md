---
id: emb-dtypes-0022
title: "Where are local variables stored, and are they initialized automatically?"
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

A local object with automatic storage duration and no explicit initializer has an indeterminate value; C does not require it to reside on the stack. An initializer such as `int x = 0;` gives it a defined initial value, while static-storage objects follow separate zero-initialization rules. Reading an indeterminate value is not a reliable way to obtain leftover stack bytes and can cause undefined behavior, depending on the expression and type.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO
