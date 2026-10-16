---
id: emb-periph-0006
title: "Що таке DMA?"
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

**DMA (Direct Memory Access)** – механізм передачі даних між периферією і пам'яттю або між ділянками пам'яті без постійної участі CPU.[^dou-embedded-interview]

Приклад: UART RX або ADC пише дані прямо в RAM buffer, а CPU лише налаштовує DMA controller: адресу периферії, адресу буфера, розмір, напрямок і режим. Після завершення DMA може згенерувати interrupt.

Переваги: менше навантаження CPU, вища швидкість, стабільніший timing. Типові задачі: SPI/UART/I2C transfers, ADC sampling, audio buffers, display refresh.

## Detailed explanation

TODO
