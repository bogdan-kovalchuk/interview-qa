---
id: emb-fund-0008
title: "В чому полягає різниця між мікропроцесором і мікроконтролером?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Мікропроцесор (MPU)** – переважно CPU, що зазвичай потребує зовнішньої RAM, Flash і периферії.[^dou-embedded-interview] Висока продуктивність, частіше запускає повноцінну ОС; приклади: Intel Core, ARM Cortex-A.

**Мікроконтролер (MCU)** – CPU + Flash + RAM + GPIO/UART/SPI/ADC/таймери на одному кристалі. Низьке споживання, дешевший, детермінована поведінка; багато MCU, наприклад ARM Cortex-M, використовують **modified Harvard architecture**, але не всі MCU треба категорично називати Harvard.

Вибір: MPU – ОС і складні обчислення; MCU – управління апаратурою в реальному часі.

## Detailed explanation

TODO
