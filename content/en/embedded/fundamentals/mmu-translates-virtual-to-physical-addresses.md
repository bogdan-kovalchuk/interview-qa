---
id: emb-fund-0010
title: "What is an MMU, and how does an MCU without an MMU differ from an Embedded Linux system?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: arm-memory-management
    title: "Arm: AArch64 Memory Management Guide"
    url: https://developer.arm.com/documentation/101811/latest/
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/e/
  - source_id: linux-nommu-mmap
    title: "The Linux Kernel Documentation: No-MMU memory-mapping support"
    url: https://docs.kernel.org/admin-guide/mm/nommu-mmap.html
---

## Short answer

**MMU** translates virtual addresses into physical addresses and provides page permissions and isolation. Most bare-metal MCUs have no MMU: code runs in a single address space, with no process isolation and no demand paging. Embedded Linux usually needs an MMU for processes, virtual memory, mmap, and kernel/user space protection.[^dou-embedded-interview]

## Detailed explanation

TODO
