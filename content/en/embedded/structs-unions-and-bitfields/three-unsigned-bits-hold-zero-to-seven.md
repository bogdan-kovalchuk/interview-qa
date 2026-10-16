---
id: emb-structs-0021
title: "What is the range of `unsigned mode : 3`?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**From `0` to `7`**.

Three bits in an `unsigned int` bit-field represent `2^3 = 8` values, from `0` to `7`. On assignment, a value outside this range is converted to the unsigned bit-field modulo `2^3`; this conversion is not a substitute for validating input.[^iso-c-n1570]

Check the allowed range before assignment, especially when the value comes from a protocol or other external input.[^iso-c-n1570]

## Detailed explanation

TODO
