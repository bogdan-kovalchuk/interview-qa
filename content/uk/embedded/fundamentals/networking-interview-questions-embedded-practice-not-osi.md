---
id: emb-fund-0026
title: "Як формулювати interview-питання про networking так, щоб воно перевіряло embedded-практику, а не теоретичне переказування OSI?"
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

Питай через scenario: device не отримує IP, MQTT reconnect штормить, TCP buffer переповнений, Ethernet DMA бачить stale packet або ARP cache застарів. Кандидат має пояснити, що перевірить на firmware, driver, PHY/MAC, network stack і wire level. **Добре питання** вимагає diagnosis, trade-offs і constraints MCU/Linux target, а не перелік OSI layers.[^dou-embedded-interview]

## Detailed explanation

TODO
