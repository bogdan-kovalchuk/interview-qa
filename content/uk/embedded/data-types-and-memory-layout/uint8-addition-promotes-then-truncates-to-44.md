---
id: emb-dtypes-0005
title: "Яким буде результат? `uint8_t a = 200; uint8_t b = 100; uint8_t result = a + b;`"
description: "Перед додаванням uint8_t промотуються до int, тому 200+100 дає 300, а присвоєння усікає його до 44."
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

`result = 44`.

Перед додаванням `a` і `b` **промотуються до `int`**: `200 + 100 = 300` (як `int`). При присвоєнні до `uint8_t` -> truncation: `300 % 256 = 44`.

Це комбінація integer promotion + type truncation. Якщо очікувалось переповнення - код правильний; якщо очікувалось 300 - баг.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
