---
id: emb-fund-0020
title: "How do you maintain one codebase for different MCUs, boards, and peripheral configurations?"
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

Separate a **portable core**, MCU-specific drivers, board support package, and configuration data. Describe hardware differences through target-specific build options, linker scripts, pin/clock tables, and devicetree-like configuration rather than chaotic `#ifdef` scattered through the logic. CI should build key variants so divergence is caught early.[^dou-embedded-interview]

## Detailed explanation

TODO
