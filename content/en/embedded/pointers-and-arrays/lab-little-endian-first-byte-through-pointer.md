---
id: emb-cppfound-0073
title: "What is the value of `*(uint8_t*)(&val)` for a little-endian value?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**0x78**. The cast `(uint8_t*)(&val)` is a pointer to the first byte of `val` in memory. On little-endian: the LSB is at the lowest address, which is `0x78`. Memory layout: `[78][56][34][12]`; next byte: `*((uint8_t*)(&val) + 1) = 0x56`. Access through a byte pointer is allowed for character types (`unsigned char*`); in practice `uint8_t` is typically a typedef for `unsigned char`.[^embeddedinterviewlab]

## Detailed explanation

TODO
