---
id: emb-periph-0008
title: "What is UART?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-uart
    title: "Zephyr Project documentation: Universal Asynchronous Receiver-Transmitter (UART)"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html
  - source_id: stm32f4-hal-uart
    title: "STMicroelectronics STM32F4 HAL: stm32f4xx_hal_uart.c (UART driver)"
    url: https://github.com/STMicroelectronics/stm32f4xx-hal-driver/blob/master/Src/stm32f4xx_hal_uart.c
---

## Short answer

**Universal Asynchronous Receiver-Transmitter** – an asynchronous serial interface. Two wires: `TX` (transmit) and `RX` (receive). No shared clock – both devices agree on the **baud rate** in advance (e.g. 115200 baud).[^dou-embedded-interview]

Frame: START bit -> data bits -> parity (optional) -> STOP bit(s); Typically 8 data bits are used, though hardware/configuration may support 5–9; UART describes data framing; electrical levels can be TTL/CMOS, RS-232, RS-485, etc.

## Detailed explanation

TODO
