---
id: emb-patterns-0015
title: "Trap: why do bit shifts need an unsigned literal rather than `1`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">`1 << 31` is undefined behavior</span>: the literal `1` has type signed `int`, and the result is not representable as `int` on a platform with 32-bit `int`.[^iso-c-n1570]

`1U << 31` is valid only if the left operand's type after integer promotions has at least 32 bits; otherwise the shift count is too large.[^iso-c-n1570]

For 32-bit masks, use `UINT32_C(1) << n` and ensure `n < 32`; for other widths, choose an unsigned type of suitable width and check its limits.[^iso-c-n1570]

## Detailed explanation

TODO
