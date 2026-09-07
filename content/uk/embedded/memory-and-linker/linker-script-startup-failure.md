---
id: emb-memlink-0016
title: "Що таке linker script і які помилки в ньому можуть зламати firmware startup?"
description: "Linker script задає memory regions і розміщення sections; помилки адрес або startup symbols можуть спричинити reset loop чи HardFault до main."
track: embedded
section: memory-and-linker
level: middle
type: pitfall
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Linker script** описує Flash/RAM regions, entry point, sections, vector table і symbols для startup. Типові помилки: неправильна адреса vector table, overlap `.data/.bss/heap/stack`, неекспортовані `_sidata/_sdata/_edata/_sbss/_ebss`, невірний RAM origin/length. <span class="warn">Такі помилки часто виглядають як reset loop або HardFault до main</span>.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
