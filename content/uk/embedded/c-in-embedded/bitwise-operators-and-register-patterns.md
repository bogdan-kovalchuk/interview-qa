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
---

## Short answer

Основні побітові оператори: `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` зсув вліво, `>>` зсув вправо.[^dou-embedded-interview]

Типові embedded-патерни: перевірити біт – `reg & (1u << n)`; встановити – `reg |= (1u << n)`; скинути – `reg &= ~(1u << n)`; перемкнути – `reg ^= (1u << n)`; створити маску – `(1u << width) - 1`. Для регістрів бажано використовувати unsigned типи, щоб уникати сюрпризів зі знаковими зсувами.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
