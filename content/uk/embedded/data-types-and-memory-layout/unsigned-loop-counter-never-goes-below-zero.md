---
id: emb-dtypes-0011
title: "Trap: що відбудеться? `for(uint8_t i = 10; i >= 0; i--)`"
description: "uint8_t беззнаковий, тому i >= 0 завжди true і цикл із декрементом не завершується."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

<span class="warn">Нескінченний цикл!</span> `uint8_t` - беззнаковий тип, тому `i >= 0` завжди `true`.

Коли `i` досягає `0` і виконується `i--` -> значення стає `255` (wraparound), а не `-1`.

Виправлення: `for(int i = 10; i >= 0; i--)` або `do { ... } while(i-- > 0);`. GCC з `-Wtype-limits` попередить про це.[^embeddedinterviewlab]

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
