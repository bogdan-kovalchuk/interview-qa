---
id: emb-fund-0026
title: "Як формулювати interview-питання про networking так, щоб воно перевіряло embedded-практику, а не теоретичне переказування OSI?"
description: "Питай через scenario: device не отримує IP, MQTT reconnect штормить, TCP buffer переповнений, Ethernet DMA бачить stale packet. Кандидат має пояснити, що перевірить на firmware, driver, PHY/MAC, network stack і wire level."
track: embedded
section: fundamentals
level: senior
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? fundamentals; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Питай через scenario: device не отримує IP, MQTT reconnect штормить, TCP buffer переповнений, Ethernet DMA бачить stale packet або ARP cache застарів.<br>Кандидат має пояснити, що перевірить на firmware, driver, PHY/MAC, network stack і wire level.<br><span class="key">Добре питання</span> вимагає diagnosis, trade-offs і constraints MCU/Linux target, а не перелік OSI layers.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
