---
id: emb-fund-0010
title: "Що таке MMU і чим MCU без MMU відрізняється від Embedded Linux системи?"
description: "<span class=\"key\">MMU</span> транслює virtual addresses у physical addresses і забезпечує page permissions/isolation."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**MMU** транслює virtual addresses у physical addresses і забезпечує page permissions/isolation. Більшість bare-metal MCU не має MMU: код працює в одному address space, без process isolation і demand paging. Embedded Linux зазвичай потребує MMU для processes, virtual memory, mmap і захисту kernel/user space.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

