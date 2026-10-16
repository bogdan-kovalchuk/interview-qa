---
id: emb-cemb-0006
title: "Який розмір union?"
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

Розмір `union` дорівнює розміру найбільшого його поля плюс можливий padding для виконання найсуворішої вимоги вирівнювання серед полів.[^dou-embedded-interview] Тобто union має бути достатньо великим і правильно вирівняним для будь-якого свого member-а.

Наприклад, `union U { char c[5]; float f; };` може мати розмір 8: найбільше поле займає 5 байтів, але `float` потребує alignment 4, тому додається padding. Точне значення завжди перевіряють через `sizeof(union U)`.

## Detailed explanation

TODO
