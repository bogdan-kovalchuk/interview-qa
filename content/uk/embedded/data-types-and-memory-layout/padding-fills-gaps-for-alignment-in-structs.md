---
id: emb-dtypes-0024
title: "Що таке padding у структурах і звідки він береться?"
description: "Padding - це байти, які компілятор вставляє між полями struct, щоб задовольнити вимоги вирівнювання."
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

**Padding** - невикористані байти, які компілятор вставляє між полями (або в кінці) структури для задоволення вимог вирівнювання.

Правило: поле типу T розміщується за адресою, кратною `alignof(T)`.

Приклад: `struct { char c; int x; }` - після `char` (1B) компілятор додає 3B padding, щоб `int` був на offset 4.

Розмір struct завжди кратний вирівнюванню найбільшого поля.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
