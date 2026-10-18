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
