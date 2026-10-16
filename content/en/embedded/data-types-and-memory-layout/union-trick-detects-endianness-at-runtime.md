---
id: emb-dtypes-0073
title: "How do you detect a platform's endianness at runtime using a union?"
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

The union trick stores a known multi-byte value and checks the first byte: for `0x01020304`, a value of `0x04` indicates little-endian. However, reading a different `union` member depends on implementation rules; a more portable approach copies the representation with `memcpy` into an `unsigned char` array and checks its bytes.[^iso-c-n1570]

## Detailed explanation

TODO
