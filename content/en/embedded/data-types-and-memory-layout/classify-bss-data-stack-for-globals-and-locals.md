---
id: emb-dtypes-0028
title: "Where do these live in `.bss`, `.data`, and the stack: `int g1; int g2 = 5; void f(){int l=3;}`?"
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

`int g1;` has static storage duration and is typically placed in **.bss**, with value zero before execution.

`int g2 = 5;` is typically in **.data** RAM; startup code loads its initial value, often from Flash.

`int l = 3;` has automatic storage duration; a typical implementation stores it on the **stack**, though the compiler may keep it in a register or optimize it away.

Machine code for `f()` is typically in `.text`, often mapped to Flash. C does not specify these sections or physical locations.[^iso-c-n1570]

## Detailed explanation

TODO
