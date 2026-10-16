---
id: emb-fund-0002
title: "What is POSIX?"
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

**POSIX** (Portable Operating System Interface) is an IEEE standard that defines an API for compatibility between Unix-like operating systems.[^dou-embedded-interview] It describes the file API (`open`/`read`/`write`/`close`), processes (`fork`/`exec`), threads (`pthread`), signals, IPC and regular expressions.

Goal: code written for POSIX compiles and runs on Linux, macOS, FreeBSD and QNX without changes. In Embedded Linux it is the foundation for portability. RTOSes (Zephyr, FreeRTOS) implement POSIX subsets (pthreads, semaphores) for code portability.

## Detailed explanation

TODO
