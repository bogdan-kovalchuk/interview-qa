---
id: emb-fund-0025
title: "Як вибрати між MCU, DSP, FPGA або аналоговим контролером для задачі керування силовою частиною?"
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

**MCU** підходить для control logic, communication і помірних loops; **DSP** - для швидких чисельних control algorithms. **FPGA** дає паралельність і deterministic sub-microsecond timing, але дорожча у розробці. Аналоговий контролер доречний, коли потрібна проста, дуже швидка або fail-safe regulation без залежності від firmware.[^dou-embedded-interview]

## Detailed explanation

TODO
