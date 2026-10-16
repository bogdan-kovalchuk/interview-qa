---
id: emb-cemb-0008
title: "Що таке struct?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`struct` – агрегатний тип, який об'єднує кілька полів різних або однакових типів під одним іменем.[^dou-embedded-interview] На відміну від масиву, поля можуть мати різні типи: `struct Point { int x; int y; };`.

Структури використовують для моделювання об'єктів даних, пакетів протоколів, конфігурацій, записів таблиць, descriptor-ів і register map-ів. Доступ до поля: `s.x` для об'єкта і `p->x` для вказівника на структуру. Розмір структури може бути більшим за суму полів через padding і alignment.

## Detailed explanation

TODO
