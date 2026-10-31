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
  - source_id: ostep-limited-direct-execution
    title: "Arpaci-Dusseau, Operating Systems: Three Easy Pieces, ch. 6: Mechanism: Limited Direct Execution"
    url: https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf
  - source_id: linux-man-syscall
    title: "Linux manual page: syscall(2)"
    url: https://man7.org/linux/man-pages/man2/syscall.2.html
  - source_id: linux-man-syscalls
    title: "Linux manual page: syscalls(2)"
    url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - source_id: linux-x86-64-syscall-table
    title: "Linux kernel source: arch/x86/entry/syscalls/syscall_64.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/arch/x86/entry/syscalls/syscall_64.tbl
  - source_id: linux-man-vdso
    title: "Linux manual page: vdso(7)"
    url: https://man7.org/linux/man-pages/man7/vdso.7.html
  - source_id: zephyr-usermode-overview
    title: "Zephyr Project documentation: User Mode Overview"
    url: https://docs.zephyrproject.org/latest/kernel/usermode/overview.html
  - source_id: zephyr-syscalls
    title: "Zephyr Project documentation: System Calls"
    url: https://docs.zephyrproject.org/latest/kernel/usermode/syscalls.html
---

## Short answer

**System call (syscall)** is a mechanism for requesting kernel services from user space.[^dou-embedded-interview] Since user space has no direct access to hardware and kernel resources, a program issues a syscall to switch into kernel mode.

Mechanism (x86-64): the program places the syscall number in `rax`, arguments in `rdi/rsi/rdx...`, and executes the `syscall` instruction. The kernel switches to privileged mode, runs the handler, and returns the result.

It provides isolation: user-space processes cannot corrupt kernel memory or the memory of other processes.

## Detailed explanation

TODO
