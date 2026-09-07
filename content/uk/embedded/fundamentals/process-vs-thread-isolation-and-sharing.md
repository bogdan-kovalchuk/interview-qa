---
id: emb-fund-0006
title: "Чим відрізняється процес від потоку?"
description: "Процес має власний адресний простір і ізольований від інших, а потоки одного процесу спільно використовують пам'ять, але потребують синхронізації."
track: embedded
section: fundamentals
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Процес** – окрема запущена програма зі своїм адресним простором, ресурсами ОС, таблицею файлових дескрипторів і мінімум одним потоком.[^dou-embedded-interview] Процеси ізольовані: помилка в одному процесі зазвичай не псує пам'ять іншого.

**Потік (thread)** – одиниця виконання всередині процесу. Потоки одного процесу мають спільну пам'ять, heap, globals і файлові дескриптори, але кожен має власний stack, регістри та instruction pointer.

Наслідок: процеси безпечніше ізольовані, але дорожчі для створення й IPC; потоки легші та швидше обмінюються даними, але потребують синхронізації (`mutex`, `semaphore`, `atomic`) через ризик race condition.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
