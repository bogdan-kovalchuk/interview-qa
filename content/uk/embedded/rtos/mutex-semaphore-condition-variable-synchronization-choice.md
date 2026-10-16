---
id: emb-rtos-0008
title: "Які способи синхронізації потоків застосовують у POSIX/RTOS і коли вибрати mutex, semaphore або condition variable?"
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

`mutex` захищає shared state з одним owner у критичній секції. `semaphore` рахує ресурси або сигналізує event між ISR/task у RTOS-стилі, якщо це дозволено API. `condition variable` будить потоки, які чекають на predicate під mutex; вона не зберігає подію сама по собі.[^dou-embedded-interview]

## Detailed explanation

TODO
