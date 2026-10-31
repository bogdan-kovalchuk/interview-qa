---
id: emb-cppfound-0018
title: "What does this print?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
---

## Question code

```c
uint32_t *p=(uint32_t*)0x2000;
uint8_t *q=(uint8_t*)p;
printf("%zu %zu", sizeof(*p), sizeof(*q));
```

## Short answer

`sizeof(*p)` -> **4**. Dereferencing `uint32_t*` yields an object of type `uint32_t` – 4 bytes.

`sizeof(*q)` -> **1**. Dereferencing `uint8_t*` yields `uint8_t` – 1 byte.

Key point: `sizeof` on a dereferenced operand is determined by the pointer type, not the address – both pointers point to the same address `0x2000`, but sizeof returns different values.[^embeddedinterviewlab]

## Detailed explanation

TODO
