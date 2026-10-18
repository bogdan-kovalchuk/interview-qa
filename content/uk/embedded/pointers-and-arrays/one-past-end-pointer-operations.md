---
id: emb-cppfound-0087
title: "Що таке \"one-past-the-end\" pointer і які операції з ним дозволені?"
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

**One-past-the-end** – вказівник на елемент одразу після масиву: `int *end = arr + N`. За стандартом C – легальний.

Дозволено:
- **Формувати** (адреса коректна);
- **Порівнювати**: `p != end`, `p <= end`;
- **Віднімати** від іншого вказівника у масиві.

Заборонено:
- <span class="warn">Розіменовувати</span>: `*end` -> UB;
- <span class="warn">Збільшувати далі</span>: `end+1` -> UB.

Стандартний ідіом: `for(int *p=arr; p!=arr+N; p++)`[^embeddedinterviewlab]

## Detailed explanation

TODO
