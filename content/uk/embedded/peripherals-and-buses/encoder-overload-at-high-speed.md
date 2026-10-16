---
id: emb-periph-0013
title: "Енкодер генерує багато імпульсів і MCU зависає на високих обертах. Як оцінити interrupt rate, debounce, timer capture і CPU load?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

Порахувати edge rate: pulses per revolution × RPM × edges per pulse, і порівняти з часом ISR. Якщо ISR на кожен edge забирає значну частину CPU, перейти на timer encoder mode/input capture, DMA або hardware counter. <span class="warn">Debounce у ISR delays тільки погіршує ситуацію</span>; для механічного енкодера потрібен hardware/filter або state-machine без blocking.[^dou-embedded-interview]

## Detailed explanation

TODO
