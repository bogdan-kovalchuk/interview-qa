---
id: emb-fund-0003
title: "What is a system call?"
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

**System call (syscall)** is a mechanism for requesting kernel services from user space.[^dou-embedded-interview] Since user space has no direct access to hardware and kernel resources, a program issues a syscall to switch into kernel mode.

Mechanism (x86-64): the program places the syscall number in `rax`, arguments in `rdi/rsi/rdx...`, and executes the `syscall` instruction. The kernel switches to privileged mode, runs the handler, and returns the result.

It provides isolation: user-space processes cannot corrupt kernel memory or the memory of other processes.

## Detailed explanation

TODO
