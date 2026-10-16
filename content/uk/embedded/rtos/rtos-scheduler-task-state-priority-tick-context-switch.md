---
id: emb-rtos-0012
title: "Як працює RTOS scheduler і що означають task state, priority, tick і context switch?"
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

RTOS scheduler вибирає ready task з найвищим priority або за policy для однакового priority. **Task state** описує ready/running/blocked/suspended, **tick** дає системний time base, а **context switch** зберігає registers поточної task і відновлює іншу. Preemption дозволяє вищому priority task витіснити нижчий.[^dou-embedded-interview]

## Detailed explanation

TODO
