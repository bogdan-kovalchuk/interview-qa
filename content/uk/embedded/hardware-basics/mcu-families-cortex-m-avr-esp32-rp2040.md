---
id: emb-hwbasic-0002
title: "З якими типами мікроконтролерів вам доводилося працювати?"
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

Відповідь індивідуальна, але варто згадати сімейства та їх особливості:[^dou-embedded-interview]

- **ARM Cortex-M**: STM32 (F1/F4/H7) – найпоширеніший у промисловості; HAL і LL бібліотеки, CubeMX.
- **AVR**: ATmega328 (Arduino Uno) – 8-bit, простий старт, добре задокументований.
- **ESP32**: Wi-Fi/BT, dual-core Xtensa LX6, FreeRTOS – IoT застосунки.
- **RP2040**: dual-core ARM M0+, PIO для гнучкої периферії.

На інтерв'ю: назвіть MCU, розкажіть який периферійний блок налаштовували (UART/SPI/DMA/PWM) і з якою задачею.

## Detailed explanation

TODO
