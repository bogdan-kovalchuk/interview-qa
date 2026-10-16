---
id: emb-dtypes-0020
title: "What happens? `int8_t x = 127; x++;`"
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

In `x++`, integer promotions convert `int8_t` to `int`, so `127 + 1` does not overflow `int`; converting 128 back to `int8_t` has an implementation-defined result or signal, rather than undefined behavior.[^iso-c-n1570]

Common implementations yield `-128`, but this is not portable wraparound; by contrast, signed arithmetic that overflows its own type has undefined behavior.[^iso-c-n1570]

Use `uint8_t` for modulo wraparound, and check `x < INT8_MAX` before incrementing when the value must stay in signed range.[^iso-c-n1570]

## Detailed explanation

TODO
