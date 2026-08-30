---
id: emb-periph-0017
title: "Як визначити момент завершення передачі UART/RS485 перед перемиканням драйвера шини на прийом?"
description: "Для перемикання UART/RS485 треба чекати transmission complete, коли спорожніли і TX buffer, і shift register."
track: embedded
section: peripherals-and-buses
level: senior
type: pitfall
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

Чекай не лише empty TX buffer, а <span class="key">transmission complete</span>: shift register теж має бути порожній.<br>Практично це flag на кшталт <code>TC</code>, interrupt/DMA complete плюс перевірка UART TC, або timer guard time для протоколу.<br><span class="warn"><code>TXE</code> часто означає тільки готовність data register, а не завершення останнього bit на дроті.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
