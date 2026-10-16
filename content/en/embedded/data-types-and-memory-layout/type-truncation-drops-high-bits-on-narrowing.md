---
id: emb-dtypes-0039
title: "What is type truncation, and when does it happen?"
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

Narrowing an integer can change its value; conversion to an unsigned integer type yields the value modulo `U_MAX + 1`.[^iso-c-n1570] For example, where 8-bit `uint8_t` exists, converting `300` produces `44`, because `300 mod 256 = 44`.[^iso-c-n1570] This conversion can occur on assignment, argument passing, or return when the destination type is narrower. Check the range first when losing value is not intended.

## Detailed explanation

TODO
