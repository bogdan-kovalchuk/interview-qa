---
id: emb-conn-0001
title: "Як TCP/IP стек використовується в IoT-пристрої і де проходить межа між firmware, OS і network stack?"
description: "На bare-metal MCU TCP/IP часто дає бібліотека типу lwIP, а firmware напряму керує Ethernet/Wi-Fi driver і sockets-like API. В Embedded Linux kernel мі…"
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

На bare-metal MCU TCP/IP часто дає бібліотека типу lwIP, а firmware напряму керує Ethernet/Wi-Fi driver і sockets-like API. В Embedded Linux kernel містить network stack і drivers, а application працює через socket API. Межа проходить там, де frame від hardware driver стає packet-ом stack-а, а далі application protocol типу MQTT/HTTP працює поверх TCP/TLS.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

