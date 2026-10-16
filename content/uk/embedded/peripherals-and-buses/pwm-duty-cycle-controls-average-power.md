---
id: emb-periph-0005
title: "Що таке PWM?"
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

**Pulse Width Modulation** – метод управління потужністю через зміну шпаруватості (duty cycle) прямокутного сигналу.[^dou-embedded-interview]

Duty cycle = T_ON / T × 100%, тож при 50% – половина потужності; частота зазвичай фіксована (наприклад 20 kHz для моторів, 50 Hz для серводвигунів).

Застосування: регулювання яскравості LED, керування DC-моторами (через H-міст), серводвигуни, DC/DC-перетворювачі; генерується апаратним таймером MCU – не навантажує CPU; приклад: `TIM3->CCR1 = 500;` при ARR=1000 дає 50% duty.

## Detailed explanation

TODO
