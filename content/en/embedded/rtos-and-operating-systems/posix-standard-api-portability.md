---
id: emb-fund-0002
title: "What is POSIX?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-standards
    title: "Linux manual page: standards(7)"
    url: https://man7.org/linux/man-pages/man7/standards.7.html
  - source_id: posix-2024-introduction
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024), Base Definitions: 1. Introduction"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap01.html
  - source_id: posix-2024-unistd-h
    title: "POSIX.1-2024 (IEEE Std 1003.1-2024): <unistd.h>"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/unistd.h.html
  - source_id: zephyr-posix-overview
    title: "Zephyr Project documentation: POSIX Overview"
    url: https://docs.zephyrproject.org/latest/services/portability/posix/overview/index.html
---

## Short answer

**POSIX** (Portable Operating System Interface) is an IEEE standard that defines an API for compatibility between Unix-like operating systems.[^dou-embedded-interview] It describes the file API (`open`/`read`/`write`/`close`), processes (`fork`/`exec`), threads (`pthread`), signals, IPC and regular expressions.

Goal: code written for POSIX compiles and runs on Linux, macOS, FreeBSD and QNX without changes. In Embedded Linux it is the foundation for portability. RTOSes (Zephyr, FreeRTOS) implement POSIX subsets (pthreads, semaphores) for code portability.

## Detailed explanation

TODO
