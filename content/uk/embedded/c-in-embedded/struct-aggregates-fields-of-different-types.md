---
id: emb-cemb-0008
title: "Що таке struct?"
description: "struct об'єднує поля різних типів під одним іменем і використовується для об'єктів даних, пакетів протоколів і register map-ів."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`struct` – агрегатний тип, який об'єднує кілька полів різних або однакових типів під одним іменем.[^dou-embedded-interview] На відміну від масиву, поля можуть мати різні типи: `struct Point { int x; int y; };`.

Структури використовують для моделювання об'єктів даних, пакетів протоколів, конфігурацій, записів таблиць, descriptor-ів і register map-ів. Доступ до поля: `s.x` для об'єкта і `p->x` для вказівника на структуру. Розмір структури може бути більшим за суму полів через padding і alignment.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
