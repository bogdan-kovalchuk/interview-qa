---
id: emb-align-0040
title: "Why do single-byte fields need no byte swap when serialising?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-byteorder
    title: "byteorder(3) - Linux manual page"
    url: https://man7.org/linux/man-pages/man3/htonl.3.html
---

## Short answer

**Endianness concerns only the byte order within a multi-byte value.**

A single byte has no "internal order", so `uint8_t` is the same on LE and BE and is placed into the buffer as is.

Rule: apply `htons` to 16-bit and `htonl` to 32-bit values; no conversion is needed for `uint8_t` and byte arrays.[^linux-byteorder]

## Detailed explanation

TODO
