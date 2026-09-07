---
id: emb-conn-0004
title: "Чим TCP відрізняється від UDP для telemetry, control commands і firmware update?"
description: "TCP дає ordered reliable byte stream з retransmission і flow control, тому зручний для firmware update або команд, де важлива цілісність. UDP дає data…"
track: embedded
section: connectivity
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу connectivity; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

TCP дає ordered reliable byte stream з retransmission і flow control, тому зручний для firmware update або команд, де важлива цілісність. UDP дає datagrams без гарантії доставки/порядку, зате менший overhead і latency, корисний для частих telemetry samples або real-time data. Якщо UDP використовується для critical command/update, reliability, ordering і authentication треба будувати вище.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

