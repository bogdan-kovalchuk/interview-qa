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
  - source_id: mqtt-v5
    title: "MQTT Version 5.0, OASIS Standard"
    url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html
  - source_id: lwip-overview
    title: "lwIP 2.1.0: Overview"
    url: https://www.nongnu.org/lwip/2_1_x/index.html
  - source_id: zephyr-net-stack-architecture
    title: "Zephyr Project documentation: Network Stack Architecture"
    url: https://docs.zephyrproject.org/latest/services/connectivity/networking/net-stack-architecture.html
  - source_id: rfc-6455-websocket
    title: "RFC 6455: The WebSocket Protocol"
    url: https://www.rfc-editor.org/rfc/rfc6455.html
  - source_id: rabbitmq-mqtt-plugin
    title: "RabbitMQ documentation: MQTT Plugin"
    url: https://www.rabbitmq.com/docs/mqtt
---

## Short answer

**MQTT** is most often the right choice for device-to-cloud: lightweight publish/subscribe, QoS, and a reconnect model. **WebSocket** is appropriate when a bidirectional channel with web/backend is needed over HTTP infrastructure. **RabbitMQ** is a broker for backend messaging; it is not typically placed directly on a small device, but the device can talk to a gateway that then publishes into RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

TODO
