---
id: emb-fund-0016
title: "What is copy-on-write, and where does it appear in Linux fork or memory mapping?"
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

**Copy-on-write** lets multiple mappings share the same physical pages for reading until someone attempts to write. After `fork`, parent and child initially share pages, and on a write the kernel creates a private copy of the page. This saves RAM and speeds up fork, but the first write may incur page fault latency.[^dou-embedded-interview]

## Detailed explanation

TODO
