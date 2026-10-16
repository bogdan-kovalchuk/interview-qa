---
id: emb-dtypes-0030
title: "What does this return? `uint16_t x = 60000; x += 10000;`"
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

After `x += 10000`, `x` is `4464`: `uint16_t` ranges from `0..65535`, and conversion back reduces 70000 modulo 65536.[^iso-c-n1570]

Unsigned arithmetic is modular, but the path depends on integer promotions: with 32-bit `int`, addition produces 70000 and assignment reduces it; with 16-bit `int`, operands may promote to `unsigned int` and wrap during addition. Either way this yields 4464, not undefined behavior.[^iso-c-n1570]

But if `70000` was expected, it is a bug from the wrong type choice; use `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO
