---
id: emb-periph-0002
title: "What is `GPIO`?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

**General Purpose Input/Output** – a software-configurable digital microcontroller pin.

Modes: `Input` (pull-up / pull-down / floating); `Output Push-Pull` – drives HIGH/LOW; `Output Open-Drain` – drives only LOW, HIGH via external pull-up resistor; `Alternate Function` – pin connects to UART/SPI/I2C/Timer.

Register control: `MODER`, `ODR`, `IDR`, `BSRR` (STM32). Atomic write: `BSRR` sets or resets a bit in a single cycle without race conditions.[^dou-embedded-interview]

## Detailed explanation

TODO
