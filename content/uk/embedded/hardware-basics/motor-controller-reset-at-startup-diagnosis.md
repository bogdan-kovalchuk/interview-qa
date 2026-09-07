---
id: emb-hwbasic-0003
title: "Контролер керує мотором і перезавантажується при старті. Які software, power integrity і hardware причини треба перевірити?"
description: "Software: brown-out/reset flags, watchdog, startup current path, PWM ramp, fault handlers і stack overflow. Power integrity: просадка supply при inrus…"
track: embedded
section: hardware-basics
level: middle
type: pitfall
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
    applicability: "Авторитетне джерело рівня секції для понять розділу hardware-basics; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Software: brown-out/reset flags, watchdog, startup current path, PWM ramp, fault handlers і stack overflow. Power integrity: просадка supply при inrush/stall current, ground bounce, слабкий regulator, погане decoupling і EMI від motor. Hardware: driver shoot-through, flyback/TVS, layout high-current loop; перевірити осцилографом Vcc/reset line саме в момент старту.[^dou-embedded-interview]

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
