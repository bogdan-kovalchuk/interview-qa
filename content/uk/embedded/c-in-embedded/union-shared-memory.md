---
id: emb-cemb-0024
title: "Що таке `union`?"
description: "`union` зберігає всі поля в одній області пам'яті, тому запис одного поля перезаписує байти, спільні з іншими полями."
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

<code>union</code> – тип, у якому всі поля ділять одну й ту саму область пам'яті. У кожен момент логічно активним є одне поле, а запис в одне поле перезаписує байти, які могли використовуватись іншими полями.[^dou-embedded-interview]

Приклад: <code>union U { uint32_t word; uint8_t bytes[4]; };</code>. Використовується для економії пам'яті, варіантних даних, низькорівневого доступу до представлення байтів. Треба бути обережним із type punning, endianness, alignment і правилами активного member-а, особливо в C++.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
