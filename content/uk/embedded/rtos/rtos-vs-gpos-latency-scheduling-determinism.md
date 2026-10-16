---
id: emb-rtos-0010
title: "Що таке RTOS і чим вона відрізняється від general-purpose OS за latency, scheduling і determinism?"
track: embedded
section: rtos
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

**RTOS** дає bounded interrupt/task latency, priority-based scheduling і primitives для deterministic embedded tasks. General-purpose OS оптимізує throughput, fairness і багатокористувацькі можливості, тому latency може бути менш передбачуваною. RTOS не гарантує «швидко завжди»; вона дає контрольовані worst-case умови, якщо код і пріоритети спроєктовані правильно.[^dou-embedded-interview]

## Detailed explanation

TODO
