---
id: emb-dtypes-0011
title: "Trap: what happens? `for(uint8_t i = 10; i >= 0; i--)`"
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

<span class="warn">Infinite loop!</span> In `i >= 0`, `uint8_t` undergoes integer promotion to `int`, so the comparison is always true.

After the loop body, decrementing `i` converts the result back to `uint8_t`; decrementing zero wraps to `UINT8_MAX` (255 for an 8-bit type).

To finish the loop, check `i == 0` before decrementing or use a signed type that holds the full range.[^iso-c-n1570]

## Detailed explanation

TODO
