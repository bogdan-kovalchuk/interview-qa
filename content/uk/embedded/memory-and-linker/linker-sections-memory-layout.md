---
id: emb-memlink-0015
title: "Що робить linker і як він розміщує секції .text, .rodata, .data, .bss, stack і heap?"
description: "Linker розв'язує symbols і розміщує program sections у Flash та RAM відповідно до linker script."
track: embedded
section: memory-and-linker
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

<span class="key">Linker</span> вирішує symbols/relocations, підтягує потрібні objects з libraries і розміщує sections у memory regions. Зазвичай <code>.text</code>/<code>.rodata</code> ідуть у Flash, <code>.data</code> має load image у Flash і runtime address у RAM, <code>.bss</code> zero-init у RAM. Stack/heap межі задаються linker script або startup code, і помилка тут дає hard fault або corruption.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
