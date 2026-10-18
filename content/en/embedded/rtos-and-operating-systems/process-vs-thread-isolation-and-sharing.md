---
id: emb-fund-0006
title: "What is the difference between a process and a thread?"
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

**Process** is a separate running program with its own address space, OS resources, file descriptor table and at least one thread.[^dou-embedded-interview] Processes are isolated: a fault in one usually does not corrupt another's memory.

**Thread** is a unit of execution inside a process; threads share memory, heap, globals and descriptors, but each has its own stack, registers and instruction pointer.

Consequence: processes isolate more safely but cost more to create and need IPC; threads are lighter and share data faster, yet need synchronization (`mutex`, `semaphore`, `atomic`) against race conditions.

## Detailed explanation

TODO
