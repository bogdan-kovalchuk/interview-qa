---
id: emb-fund-0028
title: "Як оцінити, чи має проблему вирішувати firmware, hardware design або system architecture?"
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

Спочатку визнач симптом, constraint і failure mode: timing, noise margin, resource limit, protocol mismatch чи requirement gap. Firmware доречний для sequencing, filtering, diagnostics і policy; hardware - для signal integrity, protection, analog limits і deterministic safety cutoff. **System architecture** потрібна, коли проблема виникає з невірного розподілу відповідальності між blocks або неможливих requirements.[^dou-embedded-interview]

## Detailed explanation

TODO
