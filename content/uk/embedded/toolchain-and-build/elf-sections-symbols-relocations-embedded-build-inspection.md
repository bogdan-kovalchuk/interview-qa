---
id: emb-build-0014
title: "Що таке ELF-файл і яку інформацію в ньому корисно дивитися для embedded build?"
description: "<span class=\"key\">ELF</span> – object/executable формат із headers, sections, symbols, relocations і debug info."
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

**ELF** – object/executable формат із headers, sections, symbols, relocations і debug info. В embedded дивляться entry point, section sizes/addresses, symbol table, vector table placement і чи `.data/.bss` потрапили в правильну RAM. Корисні команди: `readelf -S`, `readelf -s`, `objdump -d`, `size`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

