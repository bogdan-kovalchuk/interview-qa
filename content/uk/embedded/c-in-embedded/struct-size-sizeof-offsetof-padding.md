---
id: emb-cemb-0005
title: "Як визначити розмір структур?"
description: "Розмір структури дає `sizeof`, а внутрішній layout і padding між полями показує `offsetof`; точне значення залежить від ABI й порядку полів."
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

Розмір структури визначають оператором `sizeof(struct_type)` або `sizeof variable`.[^dou-embedded-interview] Він включає всі поля, внутрішній padding між ними й можливий trailing padding у кінці, щоб масив таких структур мав правильне вирівнювання кожного елемента.

Для аналізу layout використовують `offsetof(struct_type, field)` з `<stddef.h>`. Приклад: `struct S { char c; int x; };` часто має розмір 8, а не 5, бо `int` вирівнюється на 4 байти. Точний розмір залежить від ABI, компілятора, packing options і порядку полів.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
