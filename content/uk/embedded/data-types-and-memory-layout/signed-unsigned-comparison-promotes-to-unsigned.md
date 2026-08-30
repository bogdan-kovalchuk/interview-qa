---
id: emb-dtypes-0003
title: "Чому `if(x < y)` повертає `false`, якщо `int x = -1` і `unsigned int y = 1`?"
description: "У змішаному виразі signed перетворюється на unsigned, тому -1 стає UINT_MAX."
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

<span class="warn">Integer promotion rule</span>: при змішуванні signed і unsigned в одному виразі, signed перетворюється на unsigned.

`-1` (int) -> `UINT_MAX` (4 294 967 295) при конвертації в `unsigned int`. Тому `UINT_MAX < 1` -> `false`.

Захист: увімкни `-Wsign-compare`, порівнюй однакові типи.[^embeddedinterviewlab]

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
