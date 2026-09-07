---
id: emb-fund-0012
title: "How does user space communicate with kernel space in Embedded Linux through syscalls, ioctl, procfs, or sysfs?"
description: "User space enters the kernel through syscall: read, write, open, mmap, and others."
track: embedded
section: fundamentals
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

User space enters the kernel via `syscall`: `read`, `write`, `open`, `mmap`, and so on. For device-specific control `ioctl` is commonly used; for simple driver attributes – `sysfs`; and `procfs` is mainly for process and kernel diagnostic info. <span class="warn">Do not put an unstable binary protocol into sysfs</span>; it expects simple text attributes.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
