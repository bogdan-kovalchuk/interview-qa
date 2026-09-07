---
id: emb-conn-0002
title: "How do you choose between MQTT, RabbitMQ, and WebSocket for sending telemetry from an IoT device to the cloud?"
description: "MQTT is usually the device-to-cloud choice, while RabbitMQ stays behind a gateway and WebSocket serves bidirectional web channels."
track: embedded
section: connectivity
level: middle
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

**MQTT** is most often the right choice for device-to-cloud: lightweight publish/subscribe, QoS, and a reconnect model. **WebSocket** is appropriate when a bidirectional channel with web/backend is needed over HTTP infrastructure. **RabbitMQ** is a broker for backend messaging; it is not typically placed directly on a small device, but the device can talk to a gateway that then publishes into RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

