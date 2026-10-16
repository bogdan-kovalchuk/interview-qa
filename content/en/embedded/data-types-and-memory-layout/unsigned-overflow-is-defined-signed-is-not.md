---
id: emb-dtypes-0049
title: "What is unsigned integer overflow, and how does it differ from signed overflow?"
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

Arithmetic in an unsigned type is defined modulo `2^N`, where `N` is that type's width; signed overflow is instead <span class="warn">undefined behavior</span> in C. However, `uint8_t` and often `uint16_t` operands are promoted to `int` first, so the addition `255 + 1` can produce `256`, with zero appearing when the result is converted back to `uint8_t`.[^iso-c-n1570]

## Detailed explanation

TODO
