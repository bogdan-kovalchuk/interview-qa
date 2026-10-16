---
id: emb-cppfound-0069
title: "Навіщо потрібен cast при роботі з `void*` і які обмеження?"
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

В **C**: присвоєння `void*` до `T*` (і навпаки) не потребує explicit cast – автоматичне перетворення, тож `int *p = malloc(n);` – коректно у C.

В **C++**: <span class="warn">обов'язковий explicit cast</span>: `int *p = (int*)malloc(n);`.

Обмеження void*:
- Не можна розіменувати без cast;
- Не можна pointer arithmetic (стандарт C);
- Не зберігає type-safety.

Перед розіменуванням: `*(int*)vp = 42;`. Це правило зберігає правильний тип доступу.[^embeddedinterviewlab]

## Detailed explanation

TODO
