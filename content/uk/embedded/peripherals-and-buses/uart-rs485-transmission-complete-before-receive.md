---
id: emb-periph-0017
title: "Як визначити момент завершення передачі UART/RS485 перед перемиканням драйвера шини на прийом?"
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

Чекай не лише empty TX buffer, а **transmission complete**: shift register теж має бути порожній. Практично це flag на кшталт `TC`, interrupt/DMA complete плюс перевірка UART TC, або timer guard time для протоколу. <span class="warn">`TXE` часто означає тільки готовність data register, а не завершення останнього bit на дроті.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
