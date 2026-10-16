---
id: emb-fund-0021
title: "Як абстрагувати hardware layer без надмірного runtime overhead?"
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

Тримай abstraction тонкою: inline functions, static dispatch, templates у C++, function tables тільки там, де потрібна runtime заміна. **HAL boundary** має приховувати register details, але не маскувати timing, blocking behavior, DMA ownership або interrupt context. <span class="warn">Надто товстий HAL робить driver непередбачуваним і важким для debug на MCU.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
