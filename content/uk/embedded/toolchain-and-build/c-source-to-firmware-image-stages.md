---
id: emb-build-0011
title: "Які етапи проходить C-файл від preprocessing до executable або firmware image?"
description: "C-файл проходить preprocessing, compilation, assembly, linking і, для firmware, перетворення у цільовий image."
track: embedded
section: toolchain-and-build
level: middle
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

Спершу preprocessing розкриває <code>#include</code>, <code>#define</code> і conditional compilation. Далі compiler генерує assembly або IR, assembler створює object file, linker об'єднує objects/libraries і розміщує sections. Для firmware часто ще виконують <code>objcopy</code> у <code>.hex</code>/<code>.bin</code> і генерують map-файл.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
