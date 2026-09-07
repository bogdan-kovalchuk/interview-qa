---
id: emb-rtos-0005
title: "Яка різниця між ОС загального призначення та ОС реального часу?"
description: "GPOS оптимізована на throughput і fairness з непередбачуваною latency, а RTOS – на детермінованість: bounded latency і низький jitter."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу rtos; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**GPOS** (Linux, Windows): оптимізована на throughput, fairness і зручність для багатьох процесів; latency може бути непередбачуваною без спеціальної real-time конфігурації.[^dou-embedded-interview]

**RTOS** (FreeRTOS, Zephyr, VxWorks): оптимізована на **детермінованість** – bounded latency і прогнозований worst-case response за правильно спроєктованих пріоритетів, ISR і critical sections. У preemptive RTOS ready task з вищим пріоритетом витісняє нижчий.

Ключова метрика – **jitter** (розкид часу відгуку). Приклади задач RTOS: керування двигуном, ABS, медичні прилади.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
