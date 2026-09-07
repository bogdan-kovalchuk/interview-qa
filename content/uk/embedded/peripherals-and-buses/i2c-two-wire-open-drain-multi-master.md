---
id: emb-periph-0007
title: "Що таке I2C?"
description: "I2C – синхронна шина на двох open-drain лініях SCL/SDA з pull-up резисторами, підтримує multi-master і 7-бітну адресацію slave-пристроїв."
track: embedded
section: peripherals-and-buses
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
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Inter-Integrated Circuit** – синхронний послідовний інтерфейс.[^dou-embedded-interview] Лише два дроти: `SCL` (clock) і `SDA` (data), обидва з відкритим стоком/open-drain + pull-up резистори.

Ключовий нюанс: пристрої на шині можуть тільки **тягнути лінію вниз**; стан HIGH формується pull-up резистором. Це дозволяє кільком пристроям безпечно ділити одну шину.

Multi-master, multi-slave; Кожен slave має унікальну 7-бітну адресу; Напів-дуплекс; Швидкості: 100 kHz, 400 kHz, 1 MHz; Є ACK/NACK; Типово: датчики, EEPROM, RTC, OLED.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
