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
  - source_id: linux-man-fork
    title: "Linux manual page: fork(2)"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-page-tables
    title: "Linux kernel: Page Tables"
    url: https://docs.kernel.org/mm/page_tables.html
  - source_id: linux-man-mmap
    title: "Linux manual page: mmap(2)"
    url: https://man7.org/linux/man-pages/man2/mmap.2.html
  - source_id: linux-overcommit-accounting
    title: "Linux kernel: Overcommit Accounting"
    url: https://docs.kernel.org/mm/overcommit-accounting.html
  - source_id: linux-man-mlock
    title: "Linux manual page: mlock(2)"
    url: https://man7.org/linux/man-pages/man2/mlock.2.html
  - source_id: linux-man-vfork
    title: "Linux manual page: vfork(2)"
    url: https://man7.org/linux/man-pages/man2/vfork.2.html
  - source_id: linux-nommu-mmap
    title: "Linux kernel: No-MMU memory mapping support"
    url: https://docs.kernel.org/admin-guide/mm/nommu-mmap.html
---

## Short answer

**Copy-on-write** lets multiple mappings share the same physical pages for reading until someone attempts to write. After `fork`, parent and child initially share pages, and on a write the kernel creates a private copy of the page. This saves RAM and speeds up fork, but the first write may incur page fault latency.[^dou-embedded-interview]

## Detailed explanation

TODO
