---
id: emb-periph-0016
title: "Як працює RS485 half-duplex і як правильно керувати DE/RE pin під час transmit та receive?"
description: "В RS485 half-duplex пристрій перемикає DE/RE між передаванням і прийманням, не обрізаючи останній bit та не затримуючи відповідь."
track: embedded
section: peripherals-and-buses
level: senior
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
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

RS485 half-duplex має спільну differential bus, тому пристрій або передає, або слухає. Перед transmit увімкни driver через `DE`, зазвичай вимкни receiver через `RE` або залиш для echo-check, після повного завершення transmission повернися в receive. <span class="warn">Занадто раннє перемикання обрізає stop bit, занадто пізнє блокує відповідь іншого вузла.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
