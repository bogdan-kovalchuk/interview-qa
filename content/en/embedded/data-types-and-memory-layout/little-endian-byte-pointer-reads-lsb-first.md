---
id: emb-dtypes-0090
title: "What does this print on little-endian? `uint32_t x = 0xDEADBEEF; uint8_t *p = (uint8_t*)&x; printf(\"%02X\", p[0]);`"
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

On a little-endian system, `0xDEADBEEF` is stored least-significant byte first, so `p[0]` is `0xEF`. This depends on the target’s byte order. C permits inspecting an object representation through `unsigned char*`; `uint8_t` is optional, and if present should not be assumed to be a character type without checking.[^iso-c-n1570]

## Detailed explanation

TODO
