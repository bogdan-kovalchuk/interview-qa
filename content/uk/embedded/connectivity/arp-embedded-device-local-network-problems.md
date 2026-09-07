---
id: emb-conn-0008
title: "Що таке ARP і коли embedded-пристрій реально стикається з ARP-проблемами у локальній мережі?"
description: "ARP зіставляє IPv4 address з MAC address у локальному Ethernet/Wi-Fi сегменті. Embedded device стикається з ARP при першому connect, IP conflict, stale ARP cache, link flap або sleep/wake сценаріях."
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

**ARP** зіставляє IPv4 address з MAC address у локальному Ethernet/Wi-Fi сегменті. Embedded device стикається з ARP при першому connect до gateway/peer, IP conflict, stale ARP cache, link flap або sleep/wake сценаріях. Симптоми: ping не проходить у LAN, перший packet губиться, після зміни IP/MAC потрібен gratuitous ARP.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
