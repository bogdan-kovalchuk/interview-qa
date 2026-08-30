---
id: emb-dtypes-0021
title: "Trap: що насправді порівнюється? `uint8_t a = 200, b = 100; if(a + b > 250)`"
description: "Проміжний результат a+b обчислюється як int, тож порівняння 300>250 відрізняється від порівняння усіченого uint8_t result."
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

`a + b` промотується до `int`: результат `300` типу `int`. Порівняння `300 > 250` -> `true`.

Але: `uint8_t result = a + b; if(result > 250)` -> result = 44, умова `false`!

<span class="warn">Однаковий вираз - різний результат</span> залежно від того, де зберігається проміжне значення. Promotion відбувається до операції, assignment truncate-ить.[^embeddedinterviewlab]

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
