---
id: emb-dtypes-0014
title: "What is integer promotion in C?"
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

Integer promotion is the **automatic conversion** of an integer type with rank no greater than `int` to `int` or `unsigned int` in expressions where the C standard requires it. If `int` can represent every value of the original type, the result is `int`; otherwise it is `unsigned int`.

For example, `uint8_t` usually promotes to `int`, while a 16-bit `unsigned int` may remain `unsigned int`; this depends on the implementation's ranges.[^iso-c-n1570]

## Detailed explanation

TODO
