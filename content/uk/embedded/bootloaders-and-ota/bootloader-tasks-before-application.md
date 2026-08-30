---
id: emb-boot-0004
title: "Що таке bootloader у MCU і які задачі він виконує перед запуском application firmware?"
description: "Bootloader стартує після reset, перевіряє або оновлює image, вибирає slot і передає керування application firmware."
track: embedded
section: bootloaders-and-ota
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

Bootloader – маленький firmware, який стартує першим після reset. Він може перевірити image signature/CRC, вибрати slot, оновити firmware через UART/USB/CAN/BLE, налаштувати vector table і передати керування application. У safety/security системах він також контролює rollback, anti-bricking і chain of trust.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
