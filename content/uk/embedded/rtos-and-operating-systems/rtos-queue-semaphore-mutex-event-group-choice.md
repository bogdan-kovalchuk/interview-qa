---
id: emb-rtos-0014
title: "Які synchronization primitives є в RTOS і коли використовувати queue, semaphore, mutex або event group?"
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

**Queue** передає дані між ISR/tasks або tasks, **semaphore** сигналізує подію чи рахує ресурси. **Mutex** захищає shared resource і бажано має пріоритетне успадкування (priority inheritance). **Event group** зручний для набору flags, коли task чекає одну або кілька умов.[^dou-embedded-interview]

## Detailed explanation

TODO
