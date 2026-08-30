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

<span class="key">Translation unit</span> – результат preprocessing одного <code>.c/.cpp</code> файлу разом з усіма included headers. Якщо header містить non-static object/function definition, вона потрапить у кожну translation unit і linker побачить multiple definitions. У C++ це також може порушити ODR; у headers лишають declarations, <code>inline</code>/<code>constexpr</code> або templates за правилами мови.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
