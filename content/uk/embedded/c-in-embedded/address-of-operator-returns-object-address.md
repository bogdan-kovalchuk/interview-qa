---
id: emb-cppfound-0004
title: "Що таке операція взяття адреси `&` і що вона повертає?"
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

Оператор `&` (address-of) повертає **адресу об'єкта** у пам'яті – значення типу "вказівник на тип об'єкта".

`int x = 5; int *p = &x;` – `p` тепер вказує на `x`.

Не можна взяти адресу:
- виразів без lvalue (`&(a+b)` – помилка);
- `register` змінних;
- bit-field полів структури.

Типи: `&int` -> `int*`, `&arr` -> `int(*)[N]` (вказівник на масив, не на елемент).[^embeddedinterviewlab]

## Detailed explanation

TODO
