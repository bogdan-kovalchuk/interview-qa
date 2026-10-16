---
id: emb-dtypes-0023
title: "What memory layout does this have? `union { uint32_t word; uint8_t bytes[4]; };`"
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

Union members overlap the same storage, and the union is large enough for its largest member, with implementation-defined layout and possible padding. On a platform where `uint32_t` is four bytes, this example needs at least four bytes. Reading the bytes after writing `word` exposes a platform representation: byte order is not specified by the union or by C, so the shown sequence applies only to a little-endian target.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO
