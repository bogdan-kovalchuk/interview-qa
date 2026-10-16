---
id: emb-fund-0017
title: "How does Harvard architecture differ from von Neumann, and how does this affect Flash/RAM access?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

In **von Neumann**, code and data share one address space/bus. In **Harvard**, instruction and data memories/buses are separate, so Flash and RAM can have different access rules. On some MCUs, reading constants from program memory requires special instructions/API, and self-programming Flash has erase/write and timing limitations.[^dou-embedded-interview]

## Detailed explanation

TODO
