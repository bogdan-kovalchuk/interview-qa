---
id: emb-conn-0011
title: "Що таке MQTT і чому він часто використовується для telemetry та command/control в IoT?"
description: "MQTT - lightweight publish/subscribe protocol поверх TCP, де clients обмінюються messages через broker. Зручний для telemetry і command/control через topics, QoS levels, retained messages і last will."
track: embedded
section: connectivity
level: senior
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
    applicability: "Авторитетне джерело рівня секції для понять розділу connectivity; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**MQTT** - lightweight publish/subscribe protocol поверх TCP, де clients обмінюються messages через broker. Він зручний для telemetry і command/control через topics, QoS levels, retained messages і last will. Для embedded треба врахувати TLS cost, reconnect behavior, offline queue і обмеження RAM для payload/buffers.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
