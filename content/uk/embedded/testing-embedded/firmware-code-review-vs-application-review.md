---
id: emb-testemb-0001
title: "Як code review для firmware відрізняється від code review звичайного application-коду?"
description: "Firmware review перевіряє не лише логіку, а й взаємодію з MCU: регістри, ISR, DMA, clock/reset, timing, memory layout і power states. Окремо дивляться…"
track: embedded
section: testing-embedded
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу testing-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Firmware review** перевіряє не лише логіку, а й взаємодію з MCU: регістри, ISR, DMA, clock/reset, timing, memory layout і power states. Окремо дивляться на undefined behavior, volatile/MMIO, concurrency між ISR і tasks, stack/heap budget, error paths і fail-safe стани. <span class="warn">Код, який виглядає коректно як application logic, може ламати hardware через race, неправильний register sequence або timing.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
