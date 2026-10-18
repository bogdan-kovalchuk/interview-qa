---
id: emb-fund-0002
title: "Що таке POSIX?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**POSIX** (Portable Operating System Interface) – стандарт IEEE, що визначає API для сумісності між Unix-подібними ОС.[^dou-embedded-interview] Описує: файловий API (`open`/`read`/`write`/`close`), процеси (`fork`/`exec`), потоки (`pthread`), сигнали, IPC, регулярні вирази.

Мета: код, написаний під POSIX, компілюється і працює на Linux, macOS, FreeBSD, QNX без змін. В Embedded Linux – основа для portability. RTOS-и (Zephyr, FreeRTOS) реалізують підмножини POSIX (pthreads, semaphores) для переносимості коду.

## Detailed explanation

TODO
