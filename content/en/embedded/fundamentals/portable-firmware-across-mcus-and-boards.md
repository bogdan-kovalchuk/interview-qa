---
id: emb-fund-0020
title: "How do you maintain one codebase for different MCUs, boards, and peripheral configurations?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: zephyr-devicetree
    title: "Zephyr Project documentation: Devicetree Guide"
    url: https://docs.zephyrproject.org/latest/build/dts/intro.html
  - source_id: arm-cmsis-core
    title: "Arm CMSIS-Core: Peripheral Access and Architecture Documentation"
    url: https://arm-software.github.io/CMSIS_5/Core/html/index.html
---

## Short answer

Separate a **portable core**, MCU-specific drivers, board support package, and configuration data. Describe hardware differences through target-specific build options, linker scripts, pin/clock tables, and devicetree-like configuration rather than chaotic `#ifdef` scattered through the logic. CI should build key variants so divergence is caught early.[^dou-embedded-interview]

## Detailed explanation

TODO
