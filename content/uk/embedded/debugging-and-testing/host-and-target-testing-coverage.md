---
id: emb-testemb-0002
title: "Як тестувати embedded C-код на host і на target, і що саме має покривати кожен рівень?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

**Host tests** покривають чисту логіку: state machines, parsers, protocol framing, boundary cases, mocks для HAL/MMIO. **Target tests** перевіряють те, що залежить від заліза: clocks, drivers, DMA, ISR latency, buses, power states і real timing. HIL або board tests мають ловити інтеграційні дефекти, які unit tests на PC не бачать.[^dou-embedded-interview]

## Detailed explanation

TODO
