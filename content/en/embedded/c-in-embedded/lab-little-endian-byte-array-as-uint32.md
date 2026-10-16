---
id: emb-cppfound-0068
title: "What does this print on a little-endian system?"
track: embedded
section: c-in-embedded
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
uint8_t arr[4]={0x01,0x02,0x03,0x04};
uint32_t *p=(uint32_t*)arr;
printf("%08X",*p);
```

## Short answer

`04030201`. On little-endian (Cortex-M), bytes in memory: `[01][02][03][04]`. When read as `uint32_t`: the least significant byte comes first in memory – LSB=0x01, then 0x02, 0x03, MSB=0x04; value: `0x04030201`. <span class="warn">Warning</span>: such a cast may be misaligned on MCUs without support; safe approach: `uint32_t val; memcpy(&val, arr, 4);`[^embeddedinterviewlab]

## Detailed explanation

TODO
