---
id: emb-cemb-0033
title: "Чому volatile не замінює atomic operations, mutex або critical section?"
description: "Типова помилка в embedded-коді та її наслідки."
track: embedded
section: c-in-embedded
level: middle
type: pitfall
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
---

## Short answer

<code>volatile</code> лише каже компілятору не прибирати й не кешувати конкретні accesses. Воно <span class="warn">не робить операцію атомарною</span>, не ставить memory barrier між cores/interrupts і не захищає інваріанти структури даних. Для shared state між task/ISR потрібні atomic operations, interrupt lock, mutex або RTOS primitive залежно від контексту.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

