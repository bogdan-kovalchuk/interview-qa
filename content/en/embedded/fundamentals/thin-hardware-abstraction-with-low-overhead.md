---
id: emb-fund-0021
title: "How do you abstract the hardware layer without excessive runtime overhead?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Keep the abstraction thin: inline functions, static dispatch, templates in C++, function tables only where runtime substitution is needed. **HAL boundary** should hide register details but must not mask timing, blocking behavior, DMA ownership, or interrupt context. <span class="warn">An overly thick HAL makes the driver unpredictable and hard to debug on an MCU.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
