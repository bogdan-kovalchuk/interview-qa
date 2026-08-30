---
id: emb-conn-0010
title: "Що таке Ethernet frame і які поля важливі при роботі з raw Ethernet, AVB або industrial Ethernet?"
description: "Ethernet frame містить destination/source MAC, EtherType або length, payload і FCS; VLAN tag може додати priority/VID. Для raw Ethernet важливі MAC filtering, MTU, padding і EtherType. Для AVB/industrial Ethernet критичні timestamping, priority/QoS, deterministic latency."
track: embedded
section: connectivity
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
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? connectivity; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<span class="key">Ethernet frame</span> містить destination/source MAC, EtherType або length, payload і FCS; VLAN tag може додати priority/VID.<br>Для raw Ethernet важливі MAC filtering, MTU, padding і EtherType.<br>Для AVB/industrial Ethernet критичні timestamping, priority/QoS, deterministic latency і взаємодія MAC/PHY/driver.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
