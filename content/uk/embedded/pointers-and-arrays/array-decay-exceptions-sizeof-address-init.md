---
id: emb-cppfound-0012
title: "У яких трьох контекстах масив НЕ розпадається (decay) до вказівника?"
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

Масив залишається масивом і **не decay-ується** у трьох випадках:

1. `sizeof(arr)` – повертає загальний розмір масиву у байтах, не розмір вказівника;
2. `&arr` – повертає вказівник на масив `int(*)[N]`, не `int*`;
3. Ініціалізація рядковим літералом: `char arr[] = "hi"` – копіює символи у масив.

Пам'ятай ці три виключення – вони часто зустрічаються на інтерв'ю.[^embeddedinterviewlab]

## Detailed explanation

TODO
