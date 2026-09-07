---
id: emb-conn-0003
title: "How does BLE work at the level of advertising, connections, GATT services, and characteristics?"
description: "BLE uses advertising and central-initiated connections, with GATT services grouping characteristics for data exchange."
track: embedded
section: connectivity
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for connectivity concepts; details of specific devices and toolchains can differ."
---

## Short answer

A BLE peripheral broadcasts advertising packets with an address, flags and optional service data, while a central scans and initiates a connection. After the connection the data model is usually GATT: services group characteristics, and a characteristic has a value and properties such as read/write/notify. For low-power telemetry the key parameters are connection interval, MTU, notification rate and sleep between events.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

