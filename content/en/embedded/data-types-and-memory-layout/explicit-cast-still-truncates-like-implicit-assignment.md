---
id: emb-dtypes-0063
title: "What value does this hold? `uint8_t result = (uint8_t)(200 + 100)`"
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

`result = 44`.

`200 + 100` is computed as `int` (integer promotion): `300`; the explicit cast `(uint8_t)` truncates to 8 bits: `300 & 0xFF = 0x2C = 44`.

Difference from implicit: the explicit cast shows awareness of truncation, but the result is the same - 44.

For portable code: check that the value fits in the target type before narrowing.[^iso-c-n1570]

## Detailed explanation

TODO
