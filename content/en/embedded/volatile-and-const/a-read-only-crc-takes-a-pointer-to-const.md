---
id: emb-volconst-0051
title: "Which declaration is better for a CRC function that only reads the data?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
uint32_t crc32(? data, size_t len);
```

## Short answer

Better: `uint32_t crc32(const uint8_t *data, size_t len);`[^iso-c-n1570]

CRC does not modify the buffer, so the pointer must point to const data. This allows computing CRC over a RAM buffer, Flash table, firmware image slice, or string literal without losing type safety.

Embedded rule: `const` prevents this function from modifying elements through this pointer, but does not guarantee that the data physically resides in Flash or that another alias cannot change it.[^iso-c-n1570]

## Detailed explanation

TODO
