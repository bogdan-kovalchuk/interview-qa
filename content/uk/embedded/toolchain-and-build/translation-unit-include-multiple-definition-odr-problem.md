---
id: emb-build-0015
title: "Що таке translation unit і чому include-файли можуть викликати multiple definition або ODR-проблеми?"
description: "Translation unit – результат preprocessing одного source-файлу разом з included headers; неправильні definitions у header можуть створити multiple definitions."
track: embedded
section: toolchain-and-build
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

**Translation unit** – результат preprocessing одного `.c/.cpp` файлу разом з усіма included headers. Якщо header містить non-static object/function definition, вона потрапить у кожну translation unit і linker побачить multiple definitions. У C++ це також може порушити ODR; у headers лишають declarations, `inline`/`constexpr` або templates за правилами мови.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
