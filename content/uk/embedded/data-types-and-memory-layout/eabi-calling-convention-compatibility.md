---
id: emb-dtypes-0101
title: "Що таке EABI і чому ABI важливий при змішуванні object files, libraries і compiler flags?"
description: "EABI фіксує calling convention, layout типів, alignment і floating-point ABI, тому всі firmware objects і libraries мають узгоджуватися."
track: embedded
section: data-types-and-memory-layout
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

<span class="key">EABI</span> – embedded ABI, який фіксує calling convention, object format, type layout, alignment, exception/unwind правила й floating-point ABI. Якщо object files зібрані з різними ABI flags, наприклад soft-float vs hard-float, linker або runtime може зламатися. Для firmware всі libraries мають відповідати target CPU, FPU, endian, ABI і compiler runtime.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
