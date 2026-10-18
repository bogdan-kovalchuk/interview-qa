---
id: emb-cemb-0007
title: "Як відбувається передача параметрів у функцію?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

У C параметри передаються **за значенням**: функція отримує копію аргументу.[^dou-embedded-interview] Якщо передати `int x`, зміна параметра всередині функції не змінить змінну caller-а.

Щоб функція могла змінити об'єкт або не копіювати великий об'єкт, передають адресу: `void f(int *p)` або `void g(struct Big *s)`. Масиви в параметрах фактично перетворюються на вказівник на перший елемент, тому розмір масиву окремо треба передавати явно. У C++ додатково є references: `T&` і `const T&`.

## Detailed explanation

TODO
