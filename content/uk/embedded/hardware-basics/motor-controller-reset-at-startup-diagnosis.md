---
id: emb-hwbasic-0003
title: "Контролер керує мотором і перезавантажується при старті. Які software, power integrity і hardware причини треба перевірити?"
track: embedded
section: hardware-basics
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

Software: brown-out/reset flags, watchdog, startup current path, PWM ramp, fault handlers і stack overflow. Power integrity: просадка supply при inrush/stall current, ground bounce, слабкий regulator, погане decoupling і EMI від motor. Hardware: driver shoot-through, flyback/TVS, layout high-current loop; перевірити осцилографом Vcc/reset line саме в момент старту.[^dou-embedded-interview]

## Detailed explanation

TODO
