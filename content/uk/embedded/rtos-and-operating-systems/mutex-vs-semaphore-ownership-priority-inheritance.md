---
id: emb-rtos-0009
title: "Чим mutex відрізняється від semaphore у потоках і RTOS tasks?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

`mutex` має ownership: той task/thread, що lock-нув, має unlock-нути, і часто підтримує priority inheritance (успадкування пріоритету). `semaphore` – лічильник permits/events без такого ownership, тому його можна give/take для ресурсів або сигналізації. Для захисту shared data вибирають mutex; для producer-consumer сигналу або pool count – semaphore.[^dou-embedded-interview]

## Detailed explanation

TODO
