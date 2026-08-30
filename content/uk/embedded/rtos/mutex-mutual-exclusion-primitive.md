---
id: emb-rtos-0002
title: "Що таке mutex?"
description: "Mutex – примітив синхронізації для взаємовиключного доступу до shared resource, що блокує потік у sleep замість активного очікування."
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

**Mutex** – примітив синхронізації для взаємовиключного доступу до shared resource.[^dou-embedded-interview] Тільки один потік може володіти mutex одночасно; інші потоки мають чекати.

Якщо mutex зайнятий, потік зазвичай блокується і переходить у sleep, тому CPU не витрачається на активне очікування. Це головна відмінність від spinlock, який крутиться в циклі.

Використовується для захисту shared data, наприклад списків, черг, counters або структур стану; Важливо брати й відпускати mutex у зрозумілому порядку, щоб не створити deadlock.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
