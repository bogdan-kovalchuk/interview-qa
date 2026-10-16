---
id: emb-structs-0015
title: "What is the typical size of the union?"
track: embedded
section: structs-unions-and-bitfields
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
union U {
    uint8_t  b;
    uint16_t h;
    uint32_t w;
};
```

## Short answer

Typically `sizeof(union U) == 4` if `uint32_t` has size 4 and the union's alignment does not add trailing padding beyond 4 bytes.[^iso-c-n1570]

All members start at the same address, but which bytes of a numeric value are observed depends on endianness. The implementation providing `uint32_t` determines its availability and alignment.

The union must be large enough for its largest member; its size is not the sum of member sizes.[^iso-c-n1570]

## Detailed explanation

TODO
