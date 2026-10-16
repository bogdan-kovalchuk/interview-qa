---
id: emb-conn-0011
title: "Що таке MQTT і чому він часто використовується для telemetry та command/control в IoT?"
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

**MQTT** - lightweight publish/subscribe protocol поверх TCP, де clients обмінюються messages через broker. Він зручний для telemetry і command/control через topics, QoS levels, retained messages і last will. Для embedded треба врахувати TLS cost, reconnect behavior, offline queue і обмеження RAM для payload/buffers.[^dou-embedded-interview]

## Detailed explanation

TODO
