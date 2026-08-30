---
id: emb-conn-0002
title: "Як вибрати між MQTT, RabbitMQ і WebSocket для передачі telemetry з IoT-пристрою у хмару?"
description: "MQTT найчастіше підходить device-to-cloud: легкий publish/subscribe, QoS і reconnect model. WebSocket доречний, коли потрібен bidirectional channel із…"
track: embedded
section: connectivity
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
---

## Short answer

<span class="key">MQTT</span> найчастіше підходить device-to-cloud: легкий publish/subscribe, QoS і reconnect model. <span class="key">WebSocket</span> доречний, коли потрібен bidirectional channel із web/backend через HTTP infrastructure. <span class="key">RabbitMQ</span> – broker для backend messaging; напряму на малий device його зазвичай не ставлять, але device може говорити з gateway, який уже публікує в RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
