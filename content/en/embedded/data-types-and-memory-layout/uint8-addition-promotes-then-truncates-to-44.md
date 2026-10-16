---
id: emb-dtypes-0005
title: "What is the result? `uint8_t a = 200; uint8_t b = 100; uint8_t result = a + b;`"
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

When `uint8_t` is available, it represents values 0–255, so both operands are promoted to `int`, which can represent that range. Their sum is 300; conversion to `uint8_t` produces the value modulo 256, which is 44.[^iso-c-n1570]

## Detailed explanation

TODO
