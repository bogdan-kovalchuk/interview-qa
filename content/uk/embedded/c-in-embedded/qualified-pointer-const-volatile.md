---
id: emb-cppfound-0092
title: "Що таке qualified pointer (`volatile`, `const`) і як qualifier поширюється?"
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

Qualifier – частина типу вказівника, що вказує на властивості даних або самого вказівника.

`const int *p` – qualifier на дані: не можна змінити `*p`. Можна дати менш qualified вказівник: `int *p` -> `const int *q = p` (додавання const – OK), зворотне -> warning/error.

`volatile uint32_t *reg` – кожен доступ реально виконується (для registers).

Правило: можна **додавати** qualifier при присвоєнні, але <span class="warn">не знімати</span> без explicit cast.[^embeddedinterviewlab]

## Detailed explanation

TODO
