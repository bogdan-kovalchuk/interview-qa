---
id: emb-cemb-0034
title: "Чим вказівник відрізняється від масиву у виразах, параметрах функцій і sizeof?"
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

Масив – це об'єкт із N елементів; у більшості виразів він decay-иться до pointer на перший елемент. У параметрі функції `int a[]` фактично є `int *a`, тому довжина не передається автоматично. `sizeof array` у тій самій scope дає весь розмір масиву, а `sizeof pointer` – лише розмір адреси.[^dou-embedded-interview]

## Detailed explanation

TODO
