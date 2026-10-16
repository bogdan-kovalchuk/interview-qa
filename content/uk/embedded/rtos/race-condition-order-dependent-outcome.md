---
id: emb-rtos-0001
title: "Що таке race condition?"
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

**Race condition** – ситуація, коли результат залежить від порядку виконання потоків, процесів або ISR.[^dou-embedded-interview] Якщо порядок змінюється, програма може іноді працювати правильно, а іноді давати помилку.

Класичний приклад: `counter++` – це не одна атомарна дія, а послідовність read, modify, write; якщо два потоки одночасно читають старе значення, один інкремент може загубитися.

Захист: `mutex`, spinlock, atomic operations, critical section або вимкнення interrupt-ів на короткий час в embedded-коді.

## Detailed explanation

TODO
