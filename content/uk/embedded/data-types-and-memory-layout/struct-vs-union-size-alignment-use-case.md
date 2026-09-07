---
id: emb-dtypes-0110
title: "Чим відрізняються struct і union за розміром, alignment і use-case?"
description: "struct зберігає всі поля послідовно з можливим padding, тому її розмір приблизно сума полів плюс вирівнювання. union розділяє одну пам'ять між members, тому розмір дорівнює найбільшому member."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`struct` зберігає всі поля послідовно з можливим padding, тому її розмір приблизно сума полів плюс вирівнювання. `union` розділяє одну пам'ять між members, тому розмір дорівнює найбільшому member з потрібним alignment. Struct підходить для запису стану або register map, union – для взаємовиключних варіантів даних, але не для безпечного парсингу wire format.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
