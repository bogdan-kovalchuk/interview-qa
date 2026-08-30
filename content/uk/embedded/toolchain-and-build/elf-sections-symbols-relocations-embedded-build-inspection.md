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

<span class="key">ELF</span> – object/executable формат із headers, sections, symbols, relocations і debug info. В embedded дивляться entry point, section sizes/addresses, symbol table, vector table placement і чи <code>.data/.bss</code> потрапили в правильну RAM. Корисні команди: <code>readelf -S</code>, <code>readelf -s</code>, <code>objdump -d</code>, <code>size</code>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

