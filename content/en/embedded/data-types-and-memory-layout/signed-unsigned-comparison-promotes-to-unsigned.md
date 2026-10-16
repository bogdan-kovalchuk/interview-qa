---
id: emb-dtypes-0003
title: "Why does `if(x < y)` return `false` when `int x = -1` and `unsigned int y = 1`?"
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

This is not an integer promotion: for `int x = -1` and `unsigned int y = 1`, the usual arithmetic conversions convert both operands to `unsigned int` because the types have the same rank. Converting `-1` yields `UINT_MAX`, so `x < y` is false; the numeric value of `UINT_MAX` depends on the width of `unsigned int`.[^iso-c-n1570]

## Detailed explanation

TODO
