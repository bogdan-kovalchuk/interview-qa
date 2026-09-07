---
id: emb-memlink-0010
title: "Які типи постійної пам'яті використовуються в Embedded?"
description: "Embedded-системи використовують NOR Flash, NAND Flash, EEPROM та ROM/OTP з різними способами читання, запису, стирання і застосування."
track: embedded
section: memory-and-linker
level: junior
type: comparison
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**NOR Flash** – побайтове читання, XIP (execute-in-place), адресована шина. Використовується для зберігання firmware (MCU вбудована Flash). Повільне стирання блоками (~10K циклів).

**NAND Flash** – висока щільність, дешевший. Лише посторінкове читання, не XIP; SD-карти, eMMC, SSD; Потребує FTL (flash translation layer);

**EEPROM** – байтове стирання/запис, ~1M циклів; Повільний, малий обсяг; Для конфігурацій і налаштувань;

**ROM / OTP** – записується одноразово або при виробництві; Bootloader у деяких MCU.[^dou-embedded-interview]

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
