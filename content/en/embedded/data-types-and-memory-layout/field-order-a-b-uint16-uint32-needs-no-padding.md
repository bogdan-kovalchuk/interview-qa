---
id: emb-dtypes-0078
title: "How does the compiler lay this out? `struct { uint8_t a; uint8_t b; uint16_t c; uint32_t d; }`"
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

On a common ABI where `uint16_t` has alignment 2 and `uint32_t` alignment 4, the structure can have offsets 0, 1, 2, and 4 and a size of 8 bytes.[^iso-c-n1570] However, C leaves member alignment to the implementation, so the standard does not guarantee this layout or the absence of padding on every platform. Check `sizeof` and `offsetof` with the target toolchain.[^iso-c-n1570]

## Detailed explanation

TODO
