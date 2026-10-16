---
id: emb-macros-0044
title: "Trap: what is wrong with `#define BIT(n) (1 << (n))` at `BIT(31)`?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

On a platform with 32-bit `int`, the literal `1` has type `int`, and `1 << 31` has undefined behavior because the power of two is not representable in the signed result type.[^iso-c-n1570]

On many MCUs it "works" as `0x80000000`, but the standard does not guarantee this, and the compiler may optimize unpredictably.

For an unsigned shift, the result is reduced modulo the type's range, but `n` must still be less than the width of the promoted left operand. For a fixed 32-bit mask, use `UINT32_C(1)` and check `n < 32`.[^iso-c-n1570]

## Detailed explanation

TODO
