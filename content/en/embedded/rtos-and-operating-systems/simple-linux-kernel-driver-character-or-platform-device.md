---
id: emb-fund-0023
title: "How should you approach writing a simple Linux kernel driver for a character device or platform device?"
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

For a character device, define file operations: `open`, `read`, `write`, `ioctl`, plus registration and lifetime cleanup. For a platform driver, implement `probe`/`remove`, take resources from devicetree, map MMIO, register IRQ, and expose the interface. <span class="warn">In a kernel driver you cannot think like in user space: different allocation rules, locking, sleep context, and error handling.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
