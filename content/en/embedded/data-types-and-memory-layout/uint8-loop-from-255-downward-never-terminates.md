---
id: emb-dtypes-0071
title: "Trap: infinite loop? `uint8_t i; for(i = 255; i >= 0; i--)`"
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

<span class="warn">The loop does not terminate.</span> After integer promotion, the comparison is performed as `int`, but after decrementing zero the value is stored back in `uint8_t` as 255.[^iso-c-n1570]

When `i == 0`, `i--` computes `-1` as an `int`; assigning it back to `uint8_t` yields 255, so the next condition is true.[^iso-c-n1570]

For an inclusive countdown from 255 to 0, use a signed type that can hold both bounds, such as `int`, or stop an unsigned counter before decrementing zero.[^iso-c-n1570]

## Detailed explanation

TODO
