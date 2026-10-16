---
id: emb-conn-0002
title: "Як вибрати між MQTT, RabbitMQ і WebSocket для передачі telemetry з IoT-пристрою у хмару?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**MQTT** найчастіше підходить device-to-cloud: легкий publish/subscribe, QoS і reconnect model. **WebSocket** доречний, коли потрібен bidirectional channel із web/backend через HTTP infrastructure. **RabbitMQ** – broker для backend messaging; напряму на малий device його зазвичай не ставлять, але device може говорити з gateway, який уже публікує в RabbitMQ.[^dou-embedded-interview]

## Detailed explanation

TODO
