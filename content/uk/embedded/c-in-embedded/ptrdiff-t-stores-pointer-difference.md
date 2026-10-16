---
id: emb-cppfound-0033
title: "Що таке `ptrdiff_t` і навіщо він потрібен?"
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

**ptrdiff_t** – знаковий цілочисельний тип для зберігання результату відняття двох вказівників, визначений у `<stddef.h>`. Розмір: відповідає розрядності платформи (32-bit -> 4B, 64-bit -> 8B).

Навіщо: `p - q` дає кількість елементів між вказівниками. Результат – знаковий (може бути від'ємним); Зберігати у `int` може бути недостатньо на 64-bit.

Форматна специфікація: `%td` для `printf`.[^embeddedinterviewlab]

## Detailed explanation

TODO
