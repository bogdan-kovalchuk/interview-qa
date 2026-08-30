---
id: emb-conn-0013
title: "Які industrial або vision interfaces можуть бути embedded-relevant, але нішевими: EtherCAT, FPD-Link III, MIPI CSI, GigE Vision, USB3 Vision?"
description: "EtherCAT - deterministic industrial Ethernet для motion/control. FPD-Link III і MIPI CSI зустрічаються у camera/display pipelines. GigE Vision і USB3 Vision - machine-vision transports."
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

<span class="key">EtherCAT</span> - deterministic industrial Ethernet для motion/control, часто з dedicated slave controller.<br><span class="key">FPD-Link III</span> і <span class="key">MIPI CSI</span> часто зустрічаються у camera/display pipelines на embedded SoC.<br><span class="key">GigE Vision</span> і <span class="key">USB3 Vision</span> - machine-vision transports, де важливі bandwidth, latency, drivers і buffer handling.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
