---
id: emb-fund-0013
title: "How do blocking operations differ from non-blocking operations in drivers and I/O APIs?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: posix-read
    title: "POSIX.1-2024: read, pread – read from a file"
    url: https://pubs.opengroup.org/onlinepubs/9799919799/functions/read.html
  - source_id: zephyr-uart
    title: "Zephyr Project documentation: Universal Asynchronous Receiver-Transmitter (UART)"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/uart.html
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

A blocking call sleeps or waits until data or a resource becomes available, for example `read` on an empty device queue. A non-blocking call immediately returns `EAGAIN`/`EWOULDBLOCK` if the operation cannot be performed. In drivers this affects wait queues, poll/select/epoll support, timeouts, and whether the API can be called from a given context.[^dou-embedded-interview]

## Detailed explanation

TODO
