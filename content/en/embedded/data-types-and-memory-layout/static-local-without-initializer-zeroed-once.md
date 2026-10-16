---
id: emb-dtypes-0041
title: "Trap: is this zero-initialized inside a function? `static int x;`"
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

**Yes.** A block-scope `static int x;` has static storage duration and is implicitly initialized to zero before program execution; this does not happen on every function call.[^iso-c-n1570]

`static int x = 5;` is initialized to 5 once, and subsequent changes persist between calls.

A <span class="warn">regular</span> uninitialized local `int x;` has an indeterminate value; do not assume it is zero.[^iso-c-n1570]

## Detailed explanation

TODO
