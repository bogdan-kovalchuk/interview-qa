---
id: emb-conn-0011
title: "What is MQTT and why is it often used for telemetry and command/control in IoT?"
description: "MQTT is a lightweight publish/subscribe protocol over TCP using topics, QoS levels, retained messages and last will; on embedded, TLS cost, reconnect behavior, offline queue and RAM limits must be accounted for."
track: embedded
section: connectivity
level: senior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

**MQTT** is a lightweight publish/subscribe protocol over TCP where clients exchange messages through a broker. It is convenient for telemetry and command/control via topics, QoS levels, retained messages and last will. On embedded, account for TLS cost, reconnect behavior, offline queue and RAM limits for payload/buffers.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
