---
id: emb-rtos-0003
title: "Що таке atomic operation?"
description: "Atomic operation виконується неподільно, без видимого проміжного стану для інших потоків чи CPU, і потрібна для lock-free синхронізації."
track: embedded
section: rtos
level: junior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? rtos; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

**Atomic operation** – операція, яка виконується неподільно: інші потоки або CPU не бачать проміжного стану.[^dou-embedded-interview] Наприклад, atomic increment не розкладається для інших учасників на окремі read/modify/write.

Типові приклади: atomic load/store, increment/decrement, compare-and-swap (`CAS`). У C++ використовують `std::atomic<T>`.

Atomics потрібні для counters, flags і lock-free synchronization; Але треба розуміти memory ordering: атомарність самої змінної ще не завжди означає правильний порядок доступу до всіх пов'язаних даних.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
