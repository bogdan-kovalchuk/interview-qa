---
id: emb-dtypes-0091
title: "Trap: what happens under the C standard? `int x = INT_MAX; x++;`"
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

**Signed integer overflow in C** during an operation has undefined behavior: the standard guarantees neither a transition to `INT_MIN` nor any other result. Check the limit before incrementing; comparing a value after overflow does not repair the operation. Unsigned arithmetic is computed modulo `MAX + 1`, so `uint32_t` wraps if that type is available.[^iso-c-n1570]

## Detailed explanation

TODO
