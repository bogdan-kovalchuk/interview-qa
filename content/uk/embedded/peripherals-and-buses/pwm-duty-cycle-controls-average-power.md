---
id: emb-periph-0005
title: "Що таке PWM?"
description: "PWM керує середньою потужністю навантаження, змінюючи шпаруватість прямокутного сигналу фіксованої частоти, генерованого апаратним таймером."
track: embedded
section: peripherals-and-buses
level: junior
type: concept
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Pulse Width Modulation** – метод управління потужністю через зміну шпаруватості (duty cycle) прямокутного сигналу.[^dou-embedded-interview]

Duty cycle = T_ON / T × 100%, тож при 50% – половина потужності; частота зазвичай фіксована (наприклад 20 kHz для моторів, 50 Hz для серводвигунів).

Застосування: регулювання яскравості LED, керування DC-моторами (через H-міст), серводвигуни, DC/DC-перетворювачі; генерується апаратним таймером MCU – не навантажує CPU; приклад: `TIM3->CCR1 = 500;` при ARR=1000 дає 50% duty.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
