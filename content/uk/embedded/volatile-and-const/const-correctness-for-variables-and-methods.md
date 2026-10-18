---
id: emb-cemb-0015
title: "Як опрацьовується константність змінних?"
track: embedded
section: volatile-and-const
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Константність – це частина типу, яку компілятор враховує під час перевірки доступу.[^dou-embedded-interview] Якщо об'єкт або параметр оголошений `const`, запис через цей шлях заборонений: `void f(const int *p)` може читати `*p`, але не змінювати його.

У C++ `const` також використовується для методів: `int get() const` означає, що метод не змінює логічний стан об'єкта. Можна зняти const через cast, але якщо початковий об'єкт був реально const, запис призводить до undefined behavior. Добра практика: ставити `const` на вхідні дані, які функція не змінює.

## Detailed explanation

TODO
