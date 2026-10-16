---
id: emb-patterns-0029
title: "When do you choose enum plus switch and when a function-pointer table for an FSM?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: gcc-warning-options
    title: "GCC 16.1.0: Warning Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**enum+switch** is convenient when transitions are clearer explicitly; a compiler can warn about omitted `enum` cases when the relevant warning option is enabled.[^gcc-warning-options]

Function-pointer table can reduce repetitive dispatch code, but does not by itself guarantee `O(1)` or better speed; validate the index.

Choose based on readability and measurements on the target platform, not a fixed state count.[^iso-c-n1570]

## Detailed explanation

TODO
