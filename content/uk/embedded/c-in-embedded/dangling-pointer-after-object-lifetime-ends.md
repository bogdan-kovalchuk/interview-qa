---
id: emb-cppfound-0017
title: "Що таке dangling pointer і коли він виникає?"
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

**Dangling pointer** – вказівник, що вказує на <span class="warn">вже звільнену або знищену</span> пам'ять.

Причини:

1. Повернення адреси локальної змінної: `int* f(){ int x=5; return &x; }` – x знищена при поверненні;
2. Після `free(ptr)` без обнулення: `free(ptr); *ptr = 1;` – undefined behavior (UB);
3. Вказівник на об'єкт, термін дії якого закінчився.

Небезпека: пам'ять <span class="warn">виглядає валідною</span> до її перевикористання. Баги надзвичайно важко відтворити.[^embeddedinterviewlab]

## Detailed explanation

TODO
