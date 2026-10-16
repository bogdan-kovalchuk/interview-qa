---
id: emb-conn-0002
title: "How do you choose between MQTT, RabbitMQ, and WebSocket for sending telemetry from an IoT device to the cloud?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**MQTT** is most often the right choice for device-to-cloud: lightweight publish/subscribe, QoS, and a reconnect model. **WebSocket** is appropriate when a bidirectional channel with web/backend is needed over HTTP infrastructure. **RabbitMQ** is a broker for backend messaging; it is not typically placed directly on a small device, but the device can talk to a gateway that then publishes into RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

TODO
