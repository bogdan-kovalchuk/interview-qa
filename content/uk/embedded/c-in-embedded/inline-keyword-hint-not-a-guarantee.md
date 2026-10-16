---
id: emb-cemb-0013
title: "Що означає ключове слово inline?"
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

`inline` – підказка й правило linkage/ODR для функції, яку можна визначати в header-і.[^dou-embedded-interview] Оптимізатор може підставити тіло функції в місце виклику, щоб прибрати overhead виклику, але **не зобов'язаний** це робити.

У C/C++ семантика трохи різна, але практична ідея така: маленькі функції, часто helpers або getters, можна робити `static inline` у header-ах. Для великих функцій `inline` зазвичай не допомагає. Важливо не плутати: реальне inlining-рішення приймає компілятор, а keyword ще впливає на допустимість кількох визначень у різних translation units.

## Detailed explanation

TODO
