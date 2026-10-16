---
id: emb-rtos-0003
title: "Що таке atomic operation?"
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

**Atomic operation** – операція, яка виконується неподільно: інші потоки або CPU не бачать проміжного стану.[^dou-embedded-interview] Наприклад, atomic increment не розкладається для інших учасників на окремі read/modify/write.

Типові приклади: atomic load/store, increment/decrement, compare-and-swap (`CAS`). У C++ використовують `std::atomic<T>`.

Atomics потрібні для counters, flags і lock-free synchronization; Але треба розуміти memory ordering: атомарність самої змінної ще не завжди означає правильний порядок доступу до всіх пов'язаних даних.

## Detailed explanation

TODO
