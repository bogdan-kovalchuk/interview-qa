---
id: emb-conn-0007
title: "Як працює Wi-Fi на embedded-пристрої і які наслідки мають association, DHCP, TLS і power save modes?"
description: "Embedded Wi-Fi проходить scan/auth/association з AP, отримує IP через DHCP, TLS додає CPU/RAM cost і certificates, а power save modes зменшують споживання але додають latency і складніші reconnect paths."
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

Embedded Wi-Fi проходить scan/auth/association з AP, потім отримує IP через DHCP або static config. TLS додає CPU/RAM cost, certificates, entropy і довгі handshakes, що важливо для small MCU. Power save modes зменшують споживання, але додають latency, buffering у AP і складніші reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
