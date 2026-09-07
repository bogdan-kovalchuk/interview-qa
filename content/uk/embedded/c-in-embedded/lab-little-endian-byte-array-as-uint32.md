---
id: emb-cppfound-0068
title: "Що виведе на little-endian?"
description: "How little-endian byte order affects reading a byte array as a 32-bit integer."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
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

## Sources

<!-- generated from frontmatter -->
