---
id: emb-cppfound-0005
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
uint8_t *p = (uint8_t*)0x1000;
p++;
printf("%p", (void*)p);
```

## Short answer

`0x1001`.

Pointer arithmetic scales by `sizeof(*p)`. For `uint8_t*`: `sizeof(uint8_t) = 1`, so `p++` -> address + 1 byte.

If `uint32_t *p = (uint32_t*)0x1000; p++;` -> `0x1004` (step of 4 bytes).

Rule: `p + n` = `(char*)p + n * sizeof(*p)`.[^embeddedinterviewlab]

## Detailed explanation

TODO
