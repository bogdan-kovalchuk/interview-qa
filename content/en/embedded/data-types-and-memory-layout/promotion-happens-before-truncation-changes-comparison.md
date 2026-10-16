---
id: emb-dtypes-0021
title: "Trap: what is actually being compared? `uint8_t a = 200, b = 100; if(a + b > 250)`"
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

`a + b` is promoted to `int`: the result is `300` of type `int`. Therefore `300 > 250` is true. If the sum is first assigned to `uint8_t result`, conversion yields `44`, so `result > 250` is false. Integer promotion happens before the operation; conversion to the narrower type happens at assignment.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO
