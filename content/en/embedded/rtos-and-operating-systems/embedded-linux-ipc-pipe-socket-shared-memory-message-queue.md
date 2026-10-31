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
  - source_id: linux-man-pipe
    title: "Linux manual page: pipe(7)"
    url: https://man7.org/linux/man-pages/man7/pipe.7.html
  - source_id: linux-man-unix
    title: "Linux manual page: unix(7)"
    url: https://man7.org/linux/man-pages/man7/unix.7.html
  - source_id: linux-man-shm-overview
    title: "Linux manual page: shm_overview(7)"
    url: https://man7.org/linux/man-pages/man7/shm_overview.7.html
  - source_id: linux-man-mmap
    title: "Linux manual page: mmap(2)"
    url: https://man7.org/linux/man-pages/man2/mmap.2.html
  - source_id: linux-man-mq-overview
    title: "Linux manual page: mq_overview(7)"
    url: https://man7.org/linux/man-pages/man7/mq_overview.7.html
  - source_id: linux-man-sem-overview
    title: "Linux manual page: sem_overview(7)"
    url: https://man7.org/linux/man-pages/man7/sem_overview.7.html
---

## Short answer

`pipe` is simple for a stream between related processes, but local and one-way. `socket` is flexible: Unix domain for local IPC or TCP/UDP for network, but has overhead. `shared memory` is fastest for large data but requires synchronization; `message queue` provides message boundaries and priority, but is limited in size by system limits.[^dou-embedded-interview]

## Detailed explanation

TODO
