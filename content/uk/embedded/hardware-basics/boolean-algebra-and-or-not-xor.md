---
id: emb-hwbasic-0001
title: "Що таке булева алгебра?"
description: "Булева алгебра оперує значеннями істина/хиба через AND, OR, NOT і XOR та лежить в основі логічних вентилів і умов у коді."
track: embedded
section: hardware-basics
level: junior
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу hardware-basics; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Булева алгебра** – математична система для значень істина/хиба або 1/0.[^dou-embedded-interview] Базові операції: AND (`&&` або логічне множення), OR (`||` або логічне додавання), NOT (`!`), а також XOR.

В електроніці вона описує логічні вентилі й цифрові схеми, а в програмуванні – умови, маски, флаги та оптимізацію логічних виразів. Наприклад, закони Де Моргана: `!(A && B) == (!A || !B)` і `!(A || B) == (!A && !B)`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
