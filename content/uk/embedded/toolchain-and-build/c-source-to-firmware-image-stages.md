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
updated: 2026-09-07
content_revision: 2
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Спершу preprocessing розкриває `#include`, `#define` і conditional compilation. Далі compiler генерує assembly або IR, assembler створює object file, linker об'єднує objects/libraries і розміщує sections. Для firmware часто ще виконують `objcopy` у `.hex`/`.bin` і генерують map-файл.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
