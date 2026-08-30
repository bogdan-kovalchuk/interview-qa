---
id: emb-build-0020
title: "Як керувати залежностями у C/C++ firmware без випадкового підтягування непортативного або heap-heavy коду?"
description: "Фіксуй версії залежностей, перевіряй licenses, supported toolchains, heap/RTTI/exceptions usage і footprint у map file.Краще явно додавати маленькі li…"
track: embedded
section: toolchain-and-build
level: senior
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

Фіксуй версії залежностей, перевіряй licenses, supported toolchains, heap/RTTI/exceptions usage і footprint у map file.<br>Краще явно додавати маленькі libraries з known configuration, ніж тягнути generic package з прихованими POSIX, filesystem або allocation assumptions.<br><span class="key">Dependency review</span> для MCU має включати RAM/flash cost і behavior у ISR/RTOS context.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
