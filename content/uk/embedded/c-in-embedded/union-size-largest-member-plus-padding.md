---
id: emb-cemb-0006
title: "Який розмір union?"
description: "Розмір union дорівнює розміру найбільшого поля плюс padding, потрібний для найсуворішої вимоги вирівнювання серед членів."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

Розмір `union` дорівнює розміру найбільшого його поля плюс можливий padding для виконання найсуворішої вимоги вирівнювання серед полів.[^dou-embedded-interview] Тобто union має бути достатньо великим і правильно вирівняним для будь-якого свого member-а.

Наприклад, `union U { char c[5]; float f; };` може мати розмір 8: найбільше поле займає 5 байтів, але `float` потребує alignment 4, тому додається padding. Точне значення завжди перевіряють через `sizeof(union U)`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
