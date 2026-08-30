---
id: emb-dtypes-0045
title: "Що станеться? `unsigned char x = 0; x--;`"
description: "Unsigned арифметика визначена як modular, тому 0-1 дає 255, а не undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

`x` стане **255**. Unsigned arithmetic у C **визначений** як modular (wraparound): `0 - 1 = UCHAR_MAX = 255`.

Це **НЕ undefined behavior** (на відміну від signed overflow). Але часто - логічна помилка у циклах:
`for(unsigned char i = n; i >= 0; i--)` - нескінченний цикл.

Правило: завжди думай про wraparound при декременті unsigned типів.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
