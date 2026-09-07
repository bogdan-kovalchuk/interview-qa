---
id: emb-boot-0002
title: "Що таке bootloader?"
description: "Bootloader – невелика програма, що запускається першою після reset, перевіряє й оновлює firmware та передає керування application."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу bootloaders-and-ota; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Bootloader** – невелика програма, яка запускається першою після reset або перед основною firmware.[^dou-embedded-interview] Вона готує систему і вирішує, що запускати далі.

Типові функції: мінімальна ініціалізація hardware, перевірка цілісності firmware, вибір образу, оновлення firmware, запуск main application. Bootloader може підтримувати flashing через UART, USB, CAN, Ethernet або OTA.

У MCU bootloader часто лежить в окремій Flash-області й передає керування application через vector table/reset handler.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
