---
id: emb-fund-0015
title: "Що таке socket у Linux і коли embedded-пристрій реально потребує socket API?"
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

**Socket** – file descriptor для endpoint-у network або local IPC. Embedded-пристрій потребує socket API, коли говорить TCP/UDP, Unix domain IPC, Bluetooth sockets або має daemon/client архітектуру. Для простого sensor-to-MCU без OS socket не потрібен; там буде UART/SPI/I2C або lightweight network stack API.[^dou-embedded-interview]

## Detailed explanation

TODO
