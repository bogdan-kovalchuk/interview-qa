---
id: emb-cppfound-0022
title: "Яку адресу матиме `p` після: `uint16_t arr[4]; uint16_t *p = arr; p += 2;`?"
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

## Short answer

Якщо `arr` за адресою `0x2000` -> `p = 0x2000 + 2 * sizeof(uint16_t) = 0x2000 + 4 = 0x2004`.

Крок pointer arithmetic для `uint16_t*` = 2 байти. `p += 2` -> зсув на 2 елементи × 2 байти = 4 байти.

Тепер `p` вказує на `arr[2]`. Зважай: кроки завжди у "елементах типу", не у байтах.[^embeddedinterviewlab]

## Detailed explanation

TODO
