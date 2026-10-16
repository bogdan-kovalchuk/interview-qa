---
id: emb-align-0029
title: "How do you reorder `uint64_t, uint8_t, uint32_t, uint8_t` to minimise the size?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**From largest alignment to smallest: `uint64_t, uint32_t, uint8_t, uint8_t`.**

For an ABI with alignments `uint64_t` = 8, `uint32_t` = 4, and `uint8_t` = 1 byte, offsets are 0, 8, 12, and 13, followed by 2 padding bytes: 16 bytes total. The original order takes 24 bytes under the same assumptions.[^iso-c-n1570]

Sorting by decreasing alignment often saves space, but does not guarantee the minimum for every ABI and set of types.[^iso-c-n1570]

## Detailed explanation

TODO
