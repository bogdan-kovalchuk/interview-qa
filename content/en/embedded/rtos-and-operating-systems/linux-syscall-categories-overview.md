---
id: emb-fund-0001
title: "What system calls do you know?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: linux-man-syscalls
    title: "Linux manual page: syscalls(2)"
    url: https://man7.org/linux/man-pages/man2/syscalls.2.html
  - source_id: linux-man-malloc
    title: "Linux manual page: malloc(3)"
    url: https://man7.org/linux/man-pages/man3/malloc.3.html
  - source_id: linux-man-fork
    title: "Linux manual page: fork(2)"
    url: https://man7.org/linux/man-pages/man2/fork.2.html
  - source_id: linux-man-open
    title: "Linux manual page: open(2)"
    url: https://man7.org/linux/man-pages/man2/open.2.html
  - source_id: linux-x86-64-syscall-table
    title: "Linux kernel source: arch/x86/entry/syscalls/syscall_64.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/arch/x86/entry/syscalls/syscall_64.tbl
  - source_id: linux-generic-syscall-table
    title: "Linux kernel source: scripts/syscall.tbl"
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/scripts/syscall.tbl
  - source_id: linux-adding-syscalls
    title: "Linux kernel documentation: Adding a New System Call"
    url: https://docs.kernel.org/process/adding-syscalls.html
  - source_id: linux-man-vdso
    title: "Linux manual page: vdso(7)"
    url: https://man7.org/linux/man-pages/man7/vdso.7.html
  - source_id: linux-man-strace
    title: "Linux manual page: strace(1)"
    url: https://man7.org/linux/man-pages/man1/strace.1.html
---

## Short answer

Main categories:[^dou-embedded-interview]

- **File system**: `open()`, `read()`, `write()`, `close()`, `lseek()`, `stat()`, `unlink()`
- **Processes**: `fork()`, `exec()`, `wait()`, `exit()`, `getpid()`
- **Memory**: `mmap()`, `munmap()`, `brk()`
- **Network**: `socket()`, `bind()`, `connect()`, `send()`, `recv()`
- **Synchronisation**: `futex()`
- **Devices**: `ioctl()`.

Browse them all: `man 2 syscalls` or the file `arch/x86/entry/syscalls/syscall_64.tbl` in the kernel source.

## Detailed explanation

TODO
