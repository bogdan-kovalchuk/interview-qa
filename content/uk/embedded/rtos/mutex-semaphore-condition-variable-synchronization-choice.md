---
id: emb-rtos-0008
title: "Які способи синхронізації потоків застосовують у POSIX/RTOS і коли вибрати mutex, semaphore або condition variable?"
description: "<code>mutex</code> захищає shared state з одним owner у критичній секції."
track: embedded
section: rtos
level: middle
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

<code>mutex</code> захищає shared state з одним owner у критичній секції. <code>semaphore</code> рахує ресурси або сигналізує event між ISR/task у RTOS-стилі, якщо це дозволено API. <code>condition variable</code> будить потоки, які чекають на predicate під mutex; вона не зберігає подію сама по собі.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

