---
id: emb-cppfound-0018
title: "Що виведе?"
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
uint32_t *p=(uint32_t*)0x2000;
uint8_t *q=(uint8_t*)p;
printf("%zu %zu", sizeof(*p), sizeof(*q));
```

## Short answer

`sizeof(*p)` -> **4**. Розіменування `uint32_t*` дає об'єкт типу `uint32_t` – 4 байти.

`sizeof(*q)` -> **1**. Розіменування `uint8_t*` дає `uint8_t` – 1 байт.

Важливо: `sizeof` операнда-розіменування визначається типом вказівника, а не адресою – обидва вказівники вказують на ту саму адресу `0x2000`, але sizeof повертає різні значення.[^embeddedinterviewlab]

## Detailed explanation

TODO
