---
id: emb-periph-0007
title: "Що таке I2C?"
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

**Inter-Integrated Circuit** – синхронний послідовний інтерфейс.[^dou-embedded-interview] Лише два дроти: `SCL` (clock) і `SDA` (data), обидва з відкритим стоком/open-drain + pull-up резистори.

Ключовий нюанс: пристрої на шині можуть тільки **тягнути лінію вниз**; стан HIGH формується pull-up резистором. Це дозволяє кільком пристроям безпечно ділити одну шину.

Multi-master, multi-slave; Кожен slave має унікальну 7-бітну адресу; Напів-дуплекс; Швидкості: 100 kHz, 400 kHz, 1 MHz; Є ACK/NACK; Типово: датчики, EEPROM, RTC, OLED.

## Detailed explanation

TODO
