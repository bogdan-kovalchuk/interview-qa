---
id: emb-dtypes-0095
title: "What value does this hold? `int x = (int)(3.7);`"
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

`x` has the value `3`: converting a finite `double` to `int` discards the fractional part toward zero rather than rounding. For example, `-3.7` becomes `-3`. If the integral part is outside the range of `int`, the behavior is undefined.[^iso-c-n1570]

## Detailed explanation

TODO
