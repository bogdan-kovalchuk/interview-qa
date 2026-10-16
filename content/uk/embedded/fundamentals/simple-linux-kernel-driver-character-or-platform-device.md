---
id: emb-fund-0023
title: "Як підходити до написання простого Linux kernel driver для character device або platform device?"
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

Для character device визначають file operations: `open`, `read`, `write`, `ioctl`, плюс registration і lifetime cleanup. Для platform driver реалізують `probe`/`remove`, беруть resources з devicetree, маплять MMIO, реєструють IRQ і exposed interface. <span class="warn">У kernel driver не можна мислити як у user space: інші allocation rules, locking, sleep context і error handling.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
