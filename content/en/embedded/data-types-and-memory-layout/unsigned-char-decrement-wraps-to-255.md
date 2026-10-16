---
id: emb-dtypes-0045
title: "What happens? `unsigned char x = 0; x--;`"
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

After `x--`, `x` is **255** if `unsigned char` has 8 bits; C does not require it to be 8 bits. Integer promotions apply to the subtraction, then conversion on assignment reduces the result modulo `UCHAR_MAX + 1`.[^iso-c-n1570]

This conversion is defined, not signed overflow. A condition such as `i >= 0` is always true for an unsigned value, so a loop using it will not terminate by decrementing to zero.[^iso-c-n1570]

## Detailed explanation

TODO
