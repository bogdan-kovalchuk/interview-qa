---
id: emb-align-0035
title: "What does this code print on a little-endian machine?"
track: embedded
section: memory-alignment-and-endianness
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
uint32_t w = 0x11223344;
uint8_t *p = (uint8_t*)&w;
printf("%02X", (unsigned)p[0]);
```

## Short answer

On little-endian the code prints `44`: the least significant byte `0x44` sits at the lowest address, so `p[0]` reads it. On big-endian it would print `11`; inspecting an object's bytes through `uint8_t*` is allowed because it is a character type.[^iso-c-n1570]

## Detailed explanation

TODO
