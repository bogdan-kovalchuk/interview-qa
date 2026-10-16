---
id: emb-fund-0014
title: "Які IPC-механізми доречні в Embedded Linux і які trade-offs мають pipe, socket, shared memory та message queue?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

`pipe` простий для stream між related processes, але локальний і односторонній. `socket` гнучкий: Unix domain для local IPC або TCP/UDP для network, але має overhead. `shared memory` найшвидша для великих даних, проте потребує synchronization; `message queue` дає message boundaries і priority, але обмежена розмірами/лімітами system.[^dou-embedded-interview]

## Detailed explanation

TODO
