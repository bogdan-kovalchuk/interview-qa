---
id: emb-fund-0002
title: "Що таке POSIX?"
description: "POSIX – стандарт IEEE для сумісності API між Unix-подібними ОС, чиї підмножини реалізують і RTOS для переносимості коду."
track: embedded
section: fundamentals
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**POSIX** (Portable Operating System Interface) – стандарт IEEE, що визначає API для сумісності між Unix-подібними ОС.[^dou-embedded-interview] Описує: файловий API (`open`/`read`/`write`/`close`), процеси (`fork`/`exec`), потоки (`pthread`), сигнали, IPC, регулярні вирази.

Мета: код, написаний під POSIX, компілюється і працює на Linux, macOS, FreeBSD, QNX без змін. В Embedded Linux – основа для portability. RTOS-и (Zephyr, FreeRTOS) реалізують підмножини POSIX (pthreads, semaphores) для переносимості коду.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
