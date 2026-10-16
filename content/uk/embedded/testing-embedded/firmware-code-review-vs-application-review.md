---
id: emb-testemb-0001
title: "Як code review для firmware відрізняється від code review звичайного application-коду?"
track: embedded
section: testing-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

**Firmware review** перевіряє не лише логіку, а й взаємодію з MCU: регістри, ISR, DMA, clock/reset, timing, memory layout і power states. Окремо дивляться на undefined behavior, volatile/MMIO, concurrency між ISR і tasks, stack/heap budget, error paths і fail-safe стани. <span class="warn">Код, який виглядає коректно як application logic, може ламати hardware через race, неправильний register sequence або timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
