---
id: emb-dtypes-0047
title: "What is signed integer overflow in C, and what does the standard say about it?"
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

If the result of signed integer arithmetic is not representable in the result type, C defines the behavior as <span class="warn">undefined behavior</span>; two's complement does not make wraparound guaranteed. Use an unsigned type for defined modular arithmetic, and check a condition such as `x <= INT_MAX - y` before addition when `y >= 0`.[^iso-c-n1570]

## Detailed explanation

TODO
