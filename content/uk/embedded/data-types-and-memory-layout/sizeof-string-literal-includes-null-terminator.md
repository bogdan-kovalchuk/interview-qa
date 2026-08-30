---
id: emb-dtypes-0015
title: "Що виведе `sizeof(\"hello\")` та `strlen(\"hello\")`?"
description: "sizeof рахує null-термінатор і дає 6, а strlen рахує символи без нього і дає 5."
track: embedded
section: data-types-and-memory-layout
level: junior
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

`sizeof("hello")` -> **6**. Рядковий літерал - масив `{'h','e','l','l','o','\0'}`, 6 байтів. `sizeof` - compile-time, рахує null-terminator.

`strlen("hello")` -> **5**. Рахує символи до (не включаючи) `'\0'` - runtime функція.

Типова помилка: виділити `malloc(strlen(s))` без +1 для `'\0'` -> buffer overflow.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
