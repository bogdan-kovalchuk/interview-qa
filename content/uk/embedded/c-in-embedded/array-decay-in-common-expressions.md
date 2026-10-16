---
id: emb-cppfound-0009
title: "Що таке array decay і в яких контекстах масив перетворюється на вказівник?"
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

**Array decay** – автоматичне перетворення масиву на вказівник на його перший елемент.

Відбувається у більшості виразів:
- При передачі у функцію: `f(arr)` -> функція отримує `int*`;
- У арифметиці: `arr+1` -> `int*`;
- При присвоєнні: `int *p = arr`.

Наслідок: функція <span class="warn">втрачає інформацію про розмір</span> масиву. Тип стає `int*`, а не `int[N]`.[^embeddedinterviewlab]

## Detailed explanation

TODO
