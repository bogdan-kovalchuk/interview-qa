---
id: emb-hwbasic-0004
title: "Як оцінити signal integrity для довгої лінії або швидкого цифрового інтерфейсу на embedded-пристрої?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

Оцінити довжину лінії відносно rise time: якщо propagation delay значна, лінію треба трактувати як transmission line. Перевірити impedance, termination, return path, ground reference, crosstalk, ringing і overshoot осцилографом з правильним probing. Для довгих/шумних ліній часто краще differential interface типу RS-485/CAN/Ethernet, нижча швидкість або гальванічна ізоляція.[^dou-embedded-interview]

## Detailed explanation

TODO
