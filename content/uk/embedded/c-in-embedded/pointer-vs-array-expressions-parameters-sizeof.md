---
id: emb-cemb-0034
title: "Чим вказівник відрізняється від масиву у виразах, параметрах функцій і sizeof?"
description: "Практичне питання про embedded-розробку та її обмеження."
track: embedded
section: c-in-embedded
level: middle
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

Масив – це об'єкт із N елементів; у більшості виразів він decay-иться до pointer на перший елемент. У параметрі функції `int a[]` фактично є `int *a`, тому довжина не передається автоматично. `sizeof array` у тій самій scope дає весь розмір масиву, а `sizeof pointer` – лише розмір адреси.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

