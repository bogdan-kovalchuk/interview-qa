---
id: emb-fund-0012
title: "How does user space communicate with kernel space in Embedded Linux through syscalls, ioctl, procfs, or sysfs?"
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

User space enters the kernel via `syscall`: `read`, `write`, `open`, `mmap`, and so on. For device-specific control `ioctl` is commonly used; for simple driver attributes – `sysfs`; and `procfs` is mainly for process and kernel diagnostic info. <span class="warn">Do not put an unstable binary protocol into sysfs</span>; it expects simple text attributes.[^dou-embedded-interview]

## Detailed explanation

TODO
