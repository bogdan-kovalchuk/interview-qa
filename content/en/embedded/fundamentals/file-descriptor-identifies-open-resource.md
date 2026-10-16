---
id: emb-fund-0004
title: "What is a file descriptor?"
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

**File descriptor (fd)** is a non-negative integer that identifies an open resource within a process: file, socket, pipe, or device.[^dou-embedded-interview] The kernel maintains an fd table for each process.

Standard ones: `0` = stdin, `1` = stdout, `2` = stderr.

Cycle: `fd = open("file", O_RDONLY);`, then `read(fd, buf, n);`, then `close(fd);`. In Linux "everything is a file" – through an fd you can work with devices (`/dev/gpio`), sysfs, and even timers (`timerfd`).

## Detailed explanation

TODO
