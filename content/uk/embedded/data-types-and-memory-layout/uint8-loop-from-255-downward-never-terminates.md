---
id: emb-dtypes-0071
title: "Trap: нескінченний цикл? `uint8_t i; for(i = 255; i >= 0; i--)`"
description: "uint8_t не може бути від'ємним, тож i >= 0 завжди true і цикл ніколи не завершується."
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

<span class="warn">Так, нескінченний цикл!</span> Аналогічно до `i >= 0` для unsigned: `uint8_t` не може бути від'ємним.

Коли `i = 0` -> `i--` -> `i = 255` (wraparound) -> `255 >= 0` -> true. Цикл ніколи не завершується.

Виправлення: `for(int i = 255; i >= 0; i--)`. GCC з `-Wtype-limits` попередить про беззнакове порівняння з нулем.[^embeddedinterviewlab]

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
