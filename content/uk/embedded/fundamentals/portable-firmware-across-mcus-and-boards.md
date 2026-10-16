---
id: emb-fund-0020
title: "Як підтримувати один codebase для різних MCU, плат і peripheral configurations?"
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

Розділяй **portable core**, MCU-specific drivers, board support package і configuration data. Hardware differences описуй через target-specific build options, linker scripts, pin/clock tables і devicetree-like конфігурацію, а не через хаотичні `#ifdef` по всій логіці. CI має збирати ключові variants, щоб divergence ловився рано.[^dou-embedded-interview]

## Detailed explanation

TODO
