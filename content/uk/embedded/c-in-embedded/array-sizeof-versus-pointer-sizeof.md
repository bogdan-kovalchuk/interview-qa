---
id: emb-cppfound-0010
title: "Що поверне `sizeof(arr)` vs `sizeof(p)` якщо `int arr[8]; int *p = arr;`?"
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

## Short answer

`sizeof(arr)` -> **32** (8 елементів × 4 байти = 32B). `sizeof` на справжньому масиві повертає загальний розмір у байтах.

`sizeof(p)` -> **4** (або 8 на 64-bit). Вказівник зберігає лише адресу – його розмір = розрядність архітектури.

Ключова відмінність: масив і вказівник мають однаковий тип елементів, але `sizeof` дає зовсім різні результати.[^embeddedinterviewlab]

## Detailed explanation

TODO
