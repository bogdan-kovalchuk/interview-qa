---
id: emb-periph-0003
title: "Як працює комунікація `RS232`?"
description: "RS-232 – електричний стандарт сигналів з інвертованими рівнями й довшою дистанцією, тоді як UART описує кадрування даних; це різні речі."
track: embedded
section: peripherals-and-buses
level: junior
type: comparison
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

RS-232 – це **електричний стандарт сигналів**, а UART – блок/протокол framing даних, тобто це не одне й те саме: UART описує кадр, baud rate, start/stop/parity bits, а RS-232 – рівні напруг і фізичний інтерфейс.

Відмінності від TTL UART:

- **Рівні напруг**: логічний 1 = −3 до −15 В, логічний 0 = +3 до +15 В (інверсія!), тоді як TTL 0/3.3–5 В;
- відстань: до ~15 м (TTL ~1 м);
- роз'єм: DB-9 з лініями `RTS`/`CTS` для flow-control;
- для підключення MCU до RS-232 потрібен конвертер рівнів, напр. `MAX232`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
