---
id: emb-cppfound-0068
title: "Що виведе на little-endian?"
track: embedded
section: pointers-and-arrays
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

`04030201`.

На little-endian (Cortex-M) байти у пам'яті: `[01][02][03][04]`. При читанні як `uint32_t`: молодший байт – перший у пам'яті: LSB=0x01, потім 0x02, 0x03, MSB=0x04. Значення: `0x04030201`.

<span class="warn">Увага</span>: такий cast може бути misaligned на MCU без підтримки. Безпечно: `uint32_t val; memcpy(&val, arr, 4);`[^embeddedinterviewlab]

## Detailed explanation

TODO
