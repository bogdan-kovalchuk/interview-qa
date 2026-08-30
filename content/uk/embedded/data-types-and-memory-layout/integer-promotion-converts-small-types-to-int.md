---
id: emb-dtypes-0014
title: "Що таке integer promotion у C?"
description: "Integer promotion автоматично перетворює вузькі цілі типи на int перед арифметикою."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Джерело питання і відповіді; відповідь не перевірена незалежно."
---

## Short answer

Integer promotion - **автоматичне перетворення** `char`, `short`, `uint8_t`, `int16_t` та подібних до `int` перед арифметичними операціями (стандарт C §6.3.1.1).

Приклад: `uint8_t a = 200, b = 100;` -> перед `+` обидва стають `int`, сума = 300 (як `int`), потім усікається до `uint8_t` = 44.

Promotion відбувається завжди, незалежно від бажання програміста.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
