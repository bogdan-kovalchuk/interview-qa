---
id: emb-testemb-0001
title: "How does firmware code review differ from ordinary application-code review?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

**Firmware review** checks not only logic but also interaction with the MCU: registers, ISRs, DMA, clock/reset, timing, memory layout, and power states. It also covers undefined behavior, volatile/MMIO, concurrency between ISR and tasks, stack/heap budget, error paths, and fail-safe states. <span class="warn">Code that looks correct as application logic can break hardware through a race, an incorrect register sequence, or timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
