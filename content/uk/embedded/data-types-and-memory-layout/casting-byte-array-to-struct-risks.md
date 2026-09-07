---
id: emb-dtypes-0107
title: "Які ризики виникають, якщо привести масив байтів до структури у C?"
description: "Пряме приведення uint8_t* до struct* ризикує порушити alignment, strict aliasing і очікуваний layout з padding. Також frame може мати інший endianness або packed формат. Безпечніше читати поля через memcpy у локальні типи."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Пряме приведення `uint8_t*` до `struct*` ризикує порушити <span class="warn">alignment</span>, strict aliasing і очікуваний layout з padding. Також frame може мати інший endianness або packed формат, ніж ABI компілятора. Безпечніше читати поля через `memcpy` у локальні типи, перевіряти довжину й явно конвертувати byte order.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
