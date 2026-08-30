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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? peripherals-and-buses; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

RS-232 – це <span class="key">електричний стандарт сигналів</span>, а UART – блок/протокол framing даних. Тобто UART і RS-232 не одне й те саме: UART описує кадр, baud rate, start/stop/parity bits; RS-232 описує рівні напруг і фізичний інтерфейс.<br><br>Відмінності від TTL UART:<br>• <span class="key">Рівні напруг</span>: логічний 1 = −3 до −15 В; логічний 0 = +3 до +15 В (інверсія!). TTL: 0/3.3–5 В.<br>• Відстань: до ~15 м (на відміну від TTL ~1 м).<br>• Роз'єм: DB-9 з лініями <code>RTS</code>/<code>CTS</code> для flow-control.<br>• Для підключення MCU до RS-232 потрібен конвертер рівнів, напр. <code>MAX232</code>.[^dou-embedded-interview]
## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
