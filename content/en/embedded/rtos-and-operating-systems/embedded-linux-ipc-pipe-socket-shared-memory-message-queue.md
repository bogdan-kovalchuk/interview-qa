---
id: emb-fund-0014
title: "Which IPC mechanisms are appropriate in Embedded Linux, and what are the trade-offs of pipes, sockets, shared memory, and message queues?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

`pipe` is simple for a stream between related processes, but local and one-way. `socket` is flexible: Unix domain for local IPC or TCP/UDP for network, but has overhead. `shared memory` is fastest for large data but requires synchronization; `message queue` provides message boundaries and priority, but is limited in size by system limits.[^dou-embedded-interview]

## Detailed explanation

TODO
