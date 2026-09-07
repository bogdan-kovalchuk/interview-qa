---
id: emb-rtos-0004
title: "Що таке deadlock?"
description: "Deadlock виникає, коли два потоки взаємно чекають ресурси один одного; фіксований порядок locks і timeout запобігають цій ситуації."
track: embedded
section: rtos
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для понять розділу rtos; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Deadlock** – ситуація, коли два або більше потоки взаємно чекають ресурси один одного і ніхто не може продовжити виконання.[^dou-embedded-interview]

Приклад: Thread A взяв `m1` і чекає `m2`, а Thread B взяв `m2` і чекає `m1`. Обидва заблоковані назавжди.

Запобігання: фіксований порядок взяття locks, короткі критичні секції, timeout, lock hierarchy, уникання вкладених locks або використання higher-level primitives.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
