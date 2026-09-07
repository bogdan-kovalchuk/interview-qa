---
id: emb-cemb-0028
title: "Які існують бітові операції?"
description: "Побітові AND, OR, XOR, NOT і зсуви використовують для перевірки, встановлення, скидання та перемикання бітів у регістрах."
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

`&` AND – скидання біта: `reg &= ~(1<<n)` `|` OR – встановлення біта: `reg |= (1<<n)` `^` XOR – інвертування: `reg ^= (1<<n)` `~` NOT – побітова інверсія `<<` зсув вліво: `x << 3` = x × 8 `>>` зсув вправо: `x >> 1` = x / 2.

Типові патерни в Embedded: Перевірити біт: `if (reg & (1<<n))` Встановити: `reg |= (1<<n)` Скинути: `reg &= ~(1<<n)` Перемкнути: `reg ^= (1<<n)`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
