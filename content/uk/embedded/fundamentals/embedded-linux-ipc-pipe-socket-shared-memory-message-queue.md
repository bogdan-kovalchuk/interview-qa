---
id: emb-fund-0014
title: "Які IPC-механізми доречні в Embedded Linux і які trade-offs мають pipe, socket, shared memory та message queue?"
description: "<code>pipe</code> простий для stream між related processes, але локальний і односторонній."
track: embedded
section: fundamentals
level: middle
type: concept
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

`pipe` простий для stream між related processes, але локальний і односторонній. `socket` гнучкий: Unix domain для local IPC або TCP/UDP для network, але має overhead. `shared memory` найшвидша для великих даних, проте потребує synchronization; `message queue` дає message boundaries і priority, але обмежена розмірами/лімітами system.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

