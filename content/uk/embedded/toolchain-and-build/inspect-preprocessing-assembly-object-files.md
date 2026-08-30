---
id: emb-build-0012
title: "Як отримати проміжні файли preprocessing, assembly і object file під час компіляції?"
description: "Прапорці GCC і Clang -E, -S та -c дозволяють окремо отримати preprocessing output, assembly і object file."
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

Для GCC/Clang: <code>-E</code> дає preprocessed output, <code>-S</code> – assembly, <code>-c</code> – object file без link. Для аналізу firmware корисні <code>objdump -d</code>, <code>readelf -S</code> і linker map. У CMake ці flags можна тимчасово додати до target або виконати compiler command з <code>compile_commands.json</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
