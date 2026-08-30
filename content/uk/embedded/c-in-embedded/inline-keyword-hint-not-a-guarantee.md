---
id: emb-cemb-0013
title: "Що означає ключове слово inline?"
description: "inline підказує компілятору підставити тіло функції в місце виклику й дозволяє визначення в header-і, але не зобов'язує до реального inlining."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? c-in-embedded; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

`inline` – підказка й правило linkage/ODR для функції, яку можна визначати в header-і.[^dou-embedded-interview] Оптимізатор може підставити тіло функції в місце виклику, щоб прибрати overhead виклику, але **не зобов'язаний** це робити.

У C/C++ семантика трохи різна, але практична ідея така: маленькі функції, часто helpers або getters, можна робити `static inline` у header-ах. Для великих функцій `inline` зазвичай не допомагає. Важливо не плутати: реальне inlining-рішення приймає компілятор, а keyword ще впливає на допустимість кількох визначень у різних translation units.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
