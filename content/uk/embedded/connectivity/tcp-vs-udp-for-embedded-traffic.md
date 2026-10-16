---
id: emb-conn-0004
title: "Чим TCP відрізняється від UDP для telemetry, control commands і firmware update?"
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

TCP дає ordered reliable byte stream з retransmission і flow control, тому зручний для firmware update або команд, де важлива цілісність. UDP дає datagrams без гарантії доставки/порядку, зате менший overhead і latency, корисний для частих telemetry samples або real-time data. Якщо UDP використовується для critical command/update, reliability, ordering і authentication треба будувати вище.[^dou-embedded-interview]

## Detailed explanation

TODO
