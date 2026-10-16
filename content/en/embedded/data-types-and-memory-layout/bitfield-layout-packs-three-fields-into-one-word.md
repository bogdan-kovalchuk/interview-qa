---
id: emb-dtypes-0088
title: "What does this look like in memory? `struct { uint32_t flags:1; uint32_t mode:3; uint32_t value:28; }`"
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

The field widths sum to 32 bits, but the standard does not guarantee that the structure occupies exactly one `uint32_t` or four bytes. Bit-field allocation order, allocation units, and alignment are implementation-defined; even whether fields proceed from the least- or most-significant bit is not portable. For a register or protocol format, use explicit masks and shifts on a fixed-width integer.[^iso-c-n1570]

## Detailed explanation

TODO
