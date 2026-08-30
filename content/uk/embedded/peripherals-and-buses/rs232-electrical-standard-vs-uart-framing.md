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

RS-232 – це **електричний стандарт сигналів**, а UART – блок/протокол framing даних.[^dou-embedded-interview] Тобто UART і RS-232 не одне й те саме: UART описує кадр, baud rate, start/stop/parity bits; RS-232 описує рівні напруг і фізичний інтерфейс.

Відмінності від TTL UART:
- **Рівні напруг**: логічний 1 = −3 до −15 В; логічний 0 = +3 до +15 В (інверсія!). TTL: 0/3.3–5 В.
- Відстань: до ~15 м (на відміну від TTL ~1 м).
- Роз'єм: DB-9 з лініями `RTS`/`CTS` для flow-control.
- Для підключення MCU до RS-232 потрібен конвертер рівнів, напр. `MAX232`.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
