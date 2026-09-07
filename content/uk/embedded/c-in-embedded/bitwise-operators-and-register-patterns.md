---
id: emb-cemb-0009
title: "Які є бітові операції?"
description: "Побітові оператори & | ^ ~ << >> дають типові embedded-патерни для перевірки, встановлення, скидання й перемикання бітів у регістрах."
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

Основні побітові оператори: `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` зсув вліво, `>>` зсув вправо.[^dou-embedded-interview]

Типові embedded-патерни: перевірити біт – `reg & (1u << n)`; встановити – `reg |= (1u << n)`; скинути – `reg &= ~(1u << n)`; перемкнути – `reg ^= (1u << n)`; створити маску – `(1u << width) - 1`. Для регістрів бажано використовувати unsigned типи, щоб уникати сюрпризів зі знаковими зсувами.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
