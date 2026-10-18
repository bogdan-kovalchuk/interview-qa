---
id: emb-cppfound-0043
title: "Яке значення повертає `&arr` і як відрізняється від `arr` якщо `int arr[8]`?"
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

Обидва вирази дають **однакову числову адресу** (адресу першого елемента масиву), але мають різні **типи**:

`arr` -> decay до `int*`. `arr+1` -> +4 байти (один int). `&arr` -> `int(*)[8]` (вказівник на масив). `&arr+1` -> +32 байти (один масив).

Практично: `&arr` використовується для передачі у функцію що очікує `int(*)[8]` – зберігає розмір масиву у типі.[^embeddedinterviewlab]

## Detailed explanation

TODO
