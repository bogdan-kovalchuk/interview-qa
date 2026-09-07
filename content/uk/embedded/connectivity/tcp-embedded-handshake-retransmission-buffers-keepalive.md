---
id: emb-conn-0009
title: "Як працює TCP у контексті обмеженого embedded-пристрою: handshake, retransmission, buffers і keepalive?"
description: "TCP починається з three-way handshake, потім гарантує ordered byte stream через ACK, retransmission, windowing і congestion control. На embedded важливі RAM buffers, timeout/reconnect logic, partial writes/reads і backpressure."
track: embedded
section: connectivity
level: senior
type: concept
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу connectivity; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

TCP починається з **three-way handshake**, потім гарантує ordered byte stream через ACK, retransmission, windowing і congestion control. На embedded важливі RAM buffers, timeout/reconnect logic, partial writes/reads і backpressure від network stack. <span class="warn">Keepalive не замінює application-level heartbeat, якщо треба швидко виявляти завислий peer.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
