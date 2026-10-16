---
id: emb-periph-0002
title: "What is `GPIO`?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

**General Purpose Input/Output** – a general-purpose digital microcontroller pin configured in software.

Modes: `Input` (with pull-up / pull-down / floating); `Output Push-Pull` – drives HIGH/LOW; `Output Open-Drain` – drives only LOW, HIGH via an external resistor; `Alternate Function` – the pin is routed to UART/SPI/I2C/Timer.

Control via registers: `MODER`, `ODR`, `IDR`, `BSRR` (STM32). Atomic write: `BSRR` sets or clears a bit in one cycle with no race-condition risk.[^dou-embedded-interview]

## Detailed explanation

TODO
