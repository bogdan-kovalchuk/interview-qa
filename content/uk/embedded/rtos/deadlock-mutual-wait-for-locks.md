---
id: emb-rtos-0004
title: "Що таке deadlock?"
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

**Deadlock** – ситуація, коли два або більше потоки взаємно чекають ресурси один одного і ніхто не може продовжити виконання.[^dou-embedded-interview]

Приклад: Thread A взяв `m1` і чекає `m2`, а Thread B взяв `m2` і чекає `m1`. Обидва заблоковані назавжди.

Запобігання: фіксований порядок взяття locks, короткі критичні секції, timeout, lock hierarchy, уникання вкладених locks або використання higher-level primitives.

## Detailed explanation

TODO
